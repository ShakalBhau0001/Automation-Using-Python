import os
import shutil
from pathlib import Path


SOURCE_DIR = Path(r"C:\Users\Admin\Downloads") 
DEST_DIR = Path(r"C:\Users\Admin\Downloads\download-sorting")

EXTENSIONS = {
    "images": [".jpg", ".png", ".jpeg", ".gif"],
    "videos": [".mp4", ".mkv"],
    "music": [".mp3", ".wav"],
    "zip": [".zip", ".tgz", ".rar", ".tar"],
    "documents": [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls"],
    "setup": [".msi", ".exe"],
    "programs": [".py", ".c", ".cpp", ".php", ".C", ".CPP"],
    "design": [".xd", ".psd"],
}


def get_category(file_name: str):
    ext = Path(file_name).suffix.lower()
    for category, ext_list in EXTENSIONS.items():
        if ext in ext_list:
            return category
    return "others"


def ensure_folders():
    for folder in list(EXTENSIONS.keys()) + ["others"]:
        (DEST_DIR / folder).mkdir(parents=True, exist_ok=True)


def auto_sort():
    ensure_folders()

    files = [f for f in os.listdir(SOURCE_DIR) if os.path.isfile(SOURCE_DIR / f)]

    for file in files:
        category = get_category(file)
        src_path = SOURCE_DIR / file
        dest_path = DEST_DIR / category / file

        try:
            shutil.move(str(src_path), str(dest_path))
            print(f"Moved: {file}  →  {category}/")
        except shutil.Error:
            print(f"Skipped (exists): {file}")


if __name__ == "__main__":
    auto_sort()
