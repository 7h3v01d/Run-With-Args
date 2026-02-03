import subprocess
import sys
import os
from tkinter import Tk, simpledialog, messagebox

def main():
    Tk().withdraw()

    script_path = sys.argv[1] if len(sys.argv) > 1 else simpledialog.askstring("Script Path", "Enter path to Python script:")
    if not script_path or not os.path.isfile(script_path):
        messagebox.showerror("Error", "Invalid or missing script path.")
        return

    args = simpledialog.askstring("Arguments", "Enter CLI arguments (optional):")
    cmd = f'python "{script_path}" {args or ""}'

    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = result.stdout + "\n" + result.stderr
        messagebox.showinfo("Execution Result", output if output.strip() else "Script ran with no output.")
    except Exception as e:
        messagebox.showerror("Execution Failed", str(e))

if __name__ == "__main__":
    main()
