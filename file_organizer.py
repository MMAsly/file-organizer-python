import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, extension = os.path.splitext(filename)
            category = get_category(extension)
            category_folder = os.path.join(folder_path, category)

            os.makedirs(category_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(category_folder, filename))
            print(f"Moved: {filename} -> {category}/")

if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ").strip()
    organize_folder(folder)
