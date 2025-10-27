# file_carver.py
import os
import shutil
import hashlib
import logging

# Logging setup
logging.basicConfig(
    filename="activity_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

SUPPORTED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.pdf','.doc', '.docx', '.ppt', '.pptx')

def hash_file(path):
    """Generate SHA256 hash for a file (optional, for integrity)."""
    sha = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            sha.update(chunk)
    return sha.hexdigest()

def recover_files(source_folder, recovery_folder):
    """
    Copy supported files from source_folder to recovery_folder.
    Logs every recovered file.
    Returns a list of recovered files.
    """
    os.makedirs(recovery_folder, exist_ok=True)
    recovered = []

    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(SUPPORTED_EXTENSIONS):
                src_path = os.path.join(root, file)
                dst_path = os.path.join(recovery_folder, file)

                # Avoid overwriting existing recovered files
                if not os.path.exists(dst_path):
                    shutil.copy2(src_path, dst_path)
                    logging.info(f"Recovered file: {file}")
                    print(f"[+] Recovered: {file}")

                recovered.append({
                    "filename": file,
                    "path": src_path,
                    "hash": hash_file(src_path)
                })
