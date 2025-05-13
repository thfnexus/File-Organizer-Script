"""
📁 Project 1: File Organizer Script
👨‍💻 Created by: Hashir Adnan
🌐 Website: www.techthf.xyz
🗓️ Date: [Insert today's date]

🧠 Description:
This Python script helps organize a folder by automatically sorting files into 
subfolders based on their file extensions (e.g., Images, Documents, Videos, Music). 
It's a simple utility project to practice file handling using Python's built-in modules.

📦 Features:
- Detects all files in the specified folder
- Moves files into categorized folders like 'Images', 'Documents', etc.
- Skips unknown file types and existing folders
- Auto-creates target folders if they don't exist

🧰 Tools & Modules Used:
- os: to navigate and interact with file system
- shutil: to move files from one place to another

💡 How to Use:
1. Change the value of `folder_path` to the folder you want to organize.
2. Run the script.
3. Files will be sorted into folders based on type.

✅ Example:
Before: py/image1.png, document.pdf, song.mp3  
After:  py/Images/image1.png, py/Documents/document.pdf, py/Music/song.mp3

"""

import os
import shutil

folder_path = r"c:\Users\ads\Desktop\py"

file_types = {
    'Images': ['.jpg', '.png', '.jpeg', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Music': ['.mp3', '.wav'],
}

print(f"🔍 Scanning folder: {folder_path}\n")

files = os.listdir(folder_path)

if not files:
    print("⚠️ No files found in the folder.")
else:
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            found = False
            for folder, extensions in file_types.items():
                if ext.lower() in extensions:
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, file))
                    print(f"✅ Moved: {file} → {folder}/")
                    found = True
                    break
            if not found:
                print(f"❌ Unrecognized file type: {file} ({ext})")
        else:
            print(f"📁 Skipped folder: {file}")
