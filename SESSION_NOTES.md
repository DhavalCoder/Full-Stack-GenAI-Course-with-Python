# 🐍 What Kiro Did — Session Notes
> A beginner-friendly explanation of everything done in this session, so you can learn from it!

---

## 🎯 Goal
Automatically push your Python course files from your laptop to GitHub — every time you save a file, and also every day at 12:00 PM.

---

## ✅ Step 1 — Checked if Git is Installed

### Command Used:
```bash
git --version
```

### What it does:
- `git` is a tool that tracks changes in your files (like a save history).
- `--version` just asks "hey, are you installed and what version are you?"
- Output was: `git version 2.55.0` → Git is installed ✅

---

## ✅ Step 2 — Initialized a Git Repository

### Command Used:
```bash
git init
```

### What it does:
- Run inside your folder `C:\Users\Dhawal\Desktop\Dhaval Python`
- Creates a hidden `.git` folder inside your project
- This `.git` folder is where Git stores all the history of your files
- Think of it like: "This folder is now being tracked by Git"

---

## ✅ Step 3 — Created a README.md File

### What is README.md?
- A `README.md` is a special file that GitHub shows on your repo's homepage
- Written in **Markdown** (a simple formatting language — like this file!)
- We added a title and a short description of your course

### Markdown Basics (useful for Python devs!):
```markdown
# Big Heading
## Smaller Heading
**Bold Text**
- Bullet point
> Quote block
```

---

## ✅ Step 4 — Staged and Committed Files

### Commands Used:
```bash
git add .
git commit -m "Initial commit"
```

### What it does:
- `git add .` → Stages ALL files in the folder (the `.` means "everything")
- `git commit -m "message"` → Takes a snapshot of all staged files
  - `-m` means "message" — always write what you changed
  - Think of a commit like hitting **Save Game** in a video game

### Python Analogy:
```python
# git add . is like putting items in a list
files_to_save = ["file1.py", "file2.py", "all files..."]

# git commit is like saving that list permanently
save_snapshot(files_to_save, message="Initial commit")
```

---

## ✅ Step 5 — Connected to GitHub

### Commands Used:
```bash
git remote add origin https://github.com/DhavalCoder/Full-Stack-GenAI-Course-with-Python.git
git branch -M main
git push -u origin main
```

### What each line does:
| Command | Meaning |
|---|---|
| `git remote add origin <url>` | Links your local folder to GitHub repo |
| `git branch -M main` | Renames the default branch to `main` |
| `git push -u origin main` | Uploads all your commits to GitHub |

- **remote** = the GitHub server (it's "remote" because it's online, not on your PC)
- **origin** = a nickname for your GitHub URL
- **main** = the name of your main branch (like the main timeline of your code)
- **push** = send local commits → GitHub

---

## ✅ Step 6 — Created the Auto-Push Watcher Script

### File: `auto_push.py`

```python
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
```

### What each import does:
| Import | Purpose |
|---|---|
| `time` | Built-in Python module — used for `time.sleep(2)` to pause |
| `subprocess` | Built-in Python module — lets Python run terminal commands |
| `watchdog` | External library — watches your folder for file changes |

---

### The Handler Class:

```python
class AutoPushHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        ...
```

- **Class** = A blueprint (you'll learn this in OOP!)
- `FileSystemEventHandler` is a class from `watchdog` that we **inherit** from
- `on_any_event` is a **method** (function inside a class) that runs whenever a file changes
- It receives an `event` object that tells us what changed

---

### Filtering Unwanted Events:

```python
if any(skip in event.src_path for skip in ['.git', '__pycache__', 'auto_push.py']):
    return
```

- We don't want to push `.git` folder changes, cache files, or the script itself
- `any(...)` checks if any of the skip words appear in the file path
- `return` exits the function early — like saying "ignore this, do nothing"

---

### Running Git Commands from Python:

```python
subprocess.run(["git", "add", "."], cwd=FOLDER_PATH, check=True)
subprocess.run(["git", "commit", "-m", "auto: saved changes"], ...)
subprocess.run(["git", "push"], cwd=FOLDER_PATH, check=True)
```

- `subprocess.run()` runs a terminal command from inside Python
- `cwd=FOLDER_PATH` means "run this command in this folder"
- `check=True` means "if something goes wrong, raise an error"
- The command is passed as a **list of strings** — each word is a separate item

---

### The Observer (the actual watcher):

```python
observer = Observer()
observer.schedule(event_handler, FOLDER_PATH, recursive=True)
observer.start()
```

- `Observer()` creates a watcher object
- `.schedule(...)` tells it: watch this folder, use this handler, go into subfolders too (`recursive=True`)
- `.start()` begins watching

---

### The Infinite Loop:

```python
while True:
    time.sleep(2)
```

- Keeps the script running forever
- `time.sleep(2)` pauses for 2 seconds between each check — saves CPU
- `while True` = loop that never stops on its own
- Stopped by pressing `Ctrl+C` which triggers `KeyboardInterrupt`

---

## ✅ Step 7 — Installed the watchdog Library

### Command Used:
```bash
pip install watchdog
```

### What is pip?
- `pip` is Python's **package manager** — it downloads and installs libraries
- Like an app store for Python code
- `watchdog` is a library that monitors file system changes

---

## ✅ Step 8 — Set Up Windows Task Scheduler (Auto-run at 12 PM)

### Commands Used (PowerShell):
```powershell
$action = New-ScheduledTaskAction -Execute "python.exe" -Argument '"C:\Users\Dhawal\Desktop\Dhaval Python\auto_push.py"'
$trigger = New-ScheduledTaskTrigger -Daily -At "12:00PM"
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Hours 23) -MultipleInstances IgnoreNew
Register-ScheduledTask -TaskName "AutoPushPython" -Action $action -Trigger $trigger -Settings $settings
```

### What each part means:
| Part | Meaning |
|---|---|
| `New-ScheduledTaskAction` | What to run → `python.exe auto_push.py` |
| `New-ScheduledTaskTrigger -Daily -At "12:00PM"` | When to run → every day at noon |
| `-StartWhenAvailable` | If missed (laptop was off) → run when laptop turns on |
| `-ExecutionTimeLimit (New-TimeSpan -Hours 23)` | Let it run for up to 23 hours |
| `Register-ScheduledTask` | Actually creates the task in Windows |

### The Key Setting — `-StartWhenAvailable`:
This is the magic flag! It tells Windows:
> "If 12 PM passed and the laptop was off or sleeping, run the task as soon as the laptop is available."

---

## 📦 Libraries Used

| Library | Type | Purpose |
|---|---|---|
| `time` | Built-in | Pausing the script |
| `subprocess` | Built-in | Running terminal commands from Python |
| `watchdog` | External (pip) | Watching folder for file changes |

---

## 🔁 Full Flow Summary

```
You save a .py file
       ↓
watchdog detects the change
       ↓
on_any_event() runs
       ↓
subprocess runs: git add . → git commit → git push
       ↓
Files appear on GitHub ✅
```

And every day at 12 PM (or when laptop wakes up):
```
Windows Task Scheduler triggers
       ↓
Runs: python auto_push.py
       ↓
Watcher starts watching your folder
```

---

## 💡 Python Concepts You Just Saw in Real Use

- ✅ **Importing modules** (`import time`, `import subprocess`)
- ✅ **Classes and inheritance** (`class AutoPushHandler(FileSystemEventHandler)`)
- ✅ **Methods** (`def on_any_event(self, event)`)
- ✅ **If conditions** (`if any(...): return`)
- ✅ **While loop** (`while True`)
- ✅ **Try / Except** (error handling with `try: ... except CalledProcessError`)
- ✅ **f-strings** (`f"Change detected: {event.src_path}"`)
- ✅ **Lists** (`["git", "add", "."]`)
- ✅ **String methods** (`"nothing to commit" in result.stdout`)

---

*Keep coding, Dhaval! Every file you save is now automatically backed up on GitHub. 🚀*
