import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

FOLDER_PATH = r"C:\Users\Dhawal\Desktop\Dhaval Python"

class AutoPushHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        # Ignore hidden files, __pycache__, and the script itself
        if any(skip in event.src_path for skip in ['.git', '__pycache__', 'auto_push.py']):
            return
        if event.is_directory:
            return

        print(f"\n📁 Change detected: {event.src_path}")
        try:
            subprocess.run(["git", "add", "."], cwd=FOLDER_PATH, check=True)
            result = subprocess.run(
                ["git", "commit", "-m", "auto: saved changes"],
                cwd=FOLDER_PATH, capture_output=True, text=True
            )
            if "nothing to commit" in result.stdout:
                print("⚠️  Nothing new to commit.")
                return
            subprocess.run(["git", "push"], cwd=FOLDER_PATH, check=True)
            print("✅ Pushed to GitHub successfully!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    print(f"👀 Watching folder: {FOLDER_PATH}")
    print("📤 Any file changes will be auto-pushed to GitHub.")
    print("Press Ctrl+C to stop.\n")

    event_handler = AutoPushHandler()
    observer = Observer()
    observer.schedule(event_handler, FOLDER_PATH, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Watcher stopped.")
    observer.join()
