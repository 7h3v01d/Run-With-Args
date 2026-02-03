# 🪟 Run With Args — Native Windows Context Menu Execution for Python (Archived)

**Run With Args** is a small but deliberate experiment in making **Python scripts behave like native Windows tools**.

Instead of living in terminals or IDEs, Python utilities become:
- right-click actions
- argument-aware
- OS-integrated
- executable like any other Windows command

This project is archived, but the idea is fully realized.

---

## 🚀 What problem does this solve?

Python is powerful — but on Windows, it often feels *second-class* at the OS level.

Common friction:
- scripts require a terminal
- arguments are awkward to pass from Explorer
- batch files feel brittle
- PowerShell is overkill for small tools
- Python utilities never feel “native”

This project asked a simple question:

> **Why can’t a Python script behave like a real Windows command?**

---

## 🧠 The idea (this is the unique part)

**Run With Args** bridges Python and the Windows shell by combining:

- a compiled executable wrapper (via PyInstaller)
- Windows Registry context menu integration
- clean argument forwarding
- zero terminal interaction

The result:

> **Right-click → Run Python Tool → Arguments passed → Done**

No console juggling. No shell setup. No hacks at runtime.

---

## ✨ What it does

- Registers a **custom right-click context menu entry** in Windows Explorer
- Launches a **compiled Python executable**
- Forwards selected file paths and arguments correctly
- Handles quoting, spacing, and working directory issues
- Allows Python scripts to feel like native OS utilities

This is not a batch-file workaround — it’s proper shell integration.

---

## 🧩 Why this is unusual

The pieces individually exist:
- Python scripts
- PyInstaller executables
- Registry edits
- Argument passing

But very few tools combine them into a **reusable, ergonomic pattern**.

This project lives in the gap between:
- developer tooling
- OS-level UX
- automation ergonomics

Most people accept the friction.
This project removes it.

---

## 🗂️ Project contents

- `run_with_args.py`  
  Core Python logic for argument handling and execution

- `run_with_args.spec`  
  PyInstaller build configuration for creating a standalone executable

- `Registry Entry.reg`  
  Windows Registry file to install the right-click context menu entry

- `README.md`  
  Project documentation

- `notes.txt`  
  Design notes and observations from development

---

## ▶️ How it works (high level)

1. Python script is compiled into a standalone `.exe`
2. Windows Registry entry registers a context menu command
3. Explorer passes selected file(s) as arguments
4. Executable receives and processes arguments normally
5. Script runs exactly as if invoked from CLI — but without a terminal

---

## ⚠️ Project status

**Archived / Complete**

- Core functionality works
- No active development
- No installer beyond the `.reg` file
- Preserved as a reference implementation

This project does exactly what it set out to do.

---

## 💡 Why it still matters

This pattern is useful for:
- developer utilities
- file processing tools
- automation scripts
- internal workflows
- “one-click” Python tooling on Windows

It demonstrates how Python can be elevated from *script* to *first-class OS tool*.

---

## 📜 License

Unlicensed (personal archive).

---

## 🏷️ Status

Archived — small, intentional, and quietly powerful.
