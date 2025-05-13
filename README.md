# 📁 Project 1: File Organizer Script

👨‍💻 **Created by:** Hashir Adnan  
🌐 **Website:** [www.techthf.xyz](https://www.techthf.xyz)  
🗓️ **Date:** May 13, 2025

---

## 🧠 Description

This Python script helps organize a folder by automatically sorting files into subfolders based on their file extensions (e.g., Images, Documents, Videos, Music).  
It's a simple utility project to practice file handling using Python's built-in modules.

---

## 📦 Features

- ✅ Detects all files in the specified folder  
- 📂 Moves files into categorized folders like `Images`, `Documents`, etc.  
- 🚫 Skips unknown file types and existing folders  
- 🛠️ Auto-creates target folders if they don't exist  

---

## 🧰 Tools & Modules Used

| Module   | Purpose                                 |
|----------|-----------------------------------------|
| `os`     | Navigate and interact with the file system |
| `shutil` | Move files from one place to another     |

---

## 💡 How to Use

1. Change the value of `folder_path` in the script to the folder you want to organize.
2. Run the script using any Python environment.
3. Files will be automatically sorted into folders based on type.

---

## ✅ Example Output

**Before:**
image1.png  
document.pdf  
song.mp3  
```

**After:**
```
Images/image1.png  
Documents/document.pdf  
Music/song.mp3  
```

---

> ⚠️ Tip: Use this script only in folders where you’ve backed up your important data, just in case!
