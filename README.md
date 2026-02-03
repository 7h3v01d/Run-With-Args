# Run With Args (Archived)
### Making Python Tools Feel Native on Windows

**Run With Args** is a small systems-level utility that integrates Python scripts directly into the Windows shell, allowing them to be executed from the right-click context menu with full argument support.

This project demonstrates cross-domain thinking across **Python, Windows internals, and developer workflows**.

---

## What problem does this solve?

On Windows, Python scripts typically require:
- opening a terminal
- navigating directories
- manually passing arguments

This creates friction for tools that are otherwise simple and useful.

**Run With Args removes that friction** by treating Python scripts as first-class OS commands.

---

## Key ideas

- Python scripts compiled into standalone executables
- Windows Registry integration for context menu commands
- Clean argument forwarding from Explorer to Python
- No terminal interaction required

The result:  
**Right-click → Run Python tool → Done**

---

## Why this matters

This project shows:
- Systems-level problem solving
- Comfort working across language, OS, and tooling boundaries
- Attention to workflow ergonomics, not just code correctness
- Ability to identify and remove everyday developer friction

The solution is small, intentional, and complete.

---

## Status

Archived.  
Preserved as a reference implementation of OS-integrated Python tooling.
