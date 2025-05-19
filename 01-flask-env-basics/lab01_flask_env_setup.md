
# 🧪 Lab 01: Flask Virtual Environment Setup on Windows (Git Bash & PowerShell)

## 🎯 Objective

Set up and activate a Python virtual environment using `venv`, install Flask, and run a basic web app.  
This guide includes instructions for **both Git Bash** and **PowerShell** on Windows.

---

## 🖥️ Prerequisites

- [Python 3.x](https://www.python.org/downloads/) installed  
  ✔ Ensure "Add Python to PATH" is checked during installation  
- One of the following terminals:
  - Git Bash (from [Git for Windows](https://git-scm.com))
  - PowerShell (built into Windows)

---

## 📁 Project Structure

```
01-flask-env-basics/
├── docs/
│   └── screenshot.png
├── src/
│   └── app.py
├── setup.sh / setup.ps1
├── requirements.txt
├── README.md
└── env/ (created automatically by venv)
```

---

## 🧭 Example Navigation

**Git Bash**
```bash
cd /c/Repo/Lab_Projects/lab-roadmap/01-flask-env-basics
```

**PowerShell**
```powershell
cd C:\Repo\Lab_Projects\lab-roadmap\01-flask-env-basics
```

---

## ⚙️ Setup Guide

### ✅ Step 1: Create Virtual Environment

**Git Bash / PowerShell**
```bash
python -m venv env
```

---

### ✅ Step 2: Activate Virtual Environment

**Git Bash**
```bash
source env/Scripts/activate
```

**PowerShell**
```powershell
. .\env\Scripts\Activate.ps1
```

---

### ✅ Step 3: Install Flask

```bash
pip install flask
pip freeze > requirements.txt
```

---

### ✅ Step 4: Add a Minimal Flask App

📄 `src/app.py`:
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world! Flask is working."

if __name__ == "__main__":
    app.run(debug=True)
```

---

### ✅ Step 5: Run the App

```bash
python src/app.py
```

Visit `http://127.0.0.1:5000` in your browser.  
You should see: **"Hello, world! Flask is working."**

Take a screenshot and save it as:
```
docs/screenshot.png
```

---

### ✅ Step 6: Deactivate the Environment

```bash
deactivate
```

---

## 📌 .gitignore Setup

Add this to your `.gitignore`:
```
env/
__pycache__/
*.pyc
*.log
.DS_Store
Thumbs.db
```

---

## 🧠 Summary

| Item | Purpose |
|------|---------|
| `venv` | Isolates dependencies per project |
| `requirements.txt` | Freezes exact package versions |
| `activate` | Enables project-specific Python environment |
| `deactivate` | Returns to global environment |

---

## 🆘 PowerShell Execution Policy Fix

If you see:
> `.\env\Scripts\Activate.ps1 is not digitally signed...`

Run this once in PowerShell to temporarily allow scripts:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

---

## ✅ Next Steps

- Commit your work to Git:
  ```bash
  git add .
  git commit -m "Add Lab 01: Flask virtual environment setup (Bash + PowerShell)"
  git push origin main
  ```

- Move to Lab 02: Git commit practice

---
