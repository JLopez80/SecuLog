# file_carver.py
import os
import hashlib
import shutil

SUPPORTED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.pdf')

def hash_file(path):
    """Generate SHA256 hash for a file."""
    sha = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            sha.update(chunk)
    return sha.hexdigest()

def recover_files(source_folder, recovery_folder):
    """Copy supported files from source_folder to recovery_folder."""
    os.makedirs(recovery_folder, exist_ok=True)
    recovered = []

    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(SUPPORTED_EXTENSIONS):
                src = os.path.join(root, file)
                dst = os.path.join(recovery_folder, file)
                # Copy only if it doesn't already exist in recovery
                if not os.path.exists(dst):
                    shutil.copy2(src, dst)
                recovered.append({
                    "filename": file,
                    "path": src,
                    "hash": hash_file(src)
                })

    return recovered
