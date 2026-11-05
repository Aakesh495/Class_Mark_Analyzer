# ClassMarksAnalyzer

An interactive command-line application that analyzes a set of class marks using NumPy.

## Features

- Calculates mean, median, minimum, maximum, and population standard deviation.
- Counts passing (40 or above), failing, and above-average students.
- Rejects empty input, non-numeric marks, NaN, infinity, and values outside 0-100.

## Prerequisites

- Windows PowerShell
- [uv](https://docs.astral.sh/uv/)
- Python 3.14 (uv will use the version declared by this project)

## Setup

From the project directory, create the environment and install the locked dependencies:

```powershell
uv sync
```

To activate it manually:

```powershell
.\\.venv\\Scripts\\Activate.ps1
```

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process Bypass` for the current shell, then retry.

## Run

```powershell
uv run python class_marks_analyzer.py
```

Enter marks separated by spaces, for example: `35 40 50 75 90`.

## Dependencies

NumPy is declared in both `pyproject.toml` and `requirements.txt` with the same version constraint. The lockfile is authoritative for reproducible `uv sync` installs.

Install the requirements file into the project interpreter when needed:

```powershell
uv pip install --python .venv\\Scripts\\python.exe -r requirements.txt
```

Add future dependencies through uv, which updates the project metadata and lockfile:

```powershell
uv add <package>
```

## Troubleshooting

`ModuleNotFoundError: No module named 'numpy'` means the program is running with a different interpreter. Run it with `uv run python class_marks_analyzer.py`, or select `.venv\\Scripts\\python.exe` in VS Code. Do not install packages into a uv-managed global Python installation.

## Clone on another computer

```powershell
git clone <repository-url>
cd ClassMarksAnalyzer
uv sync
uv run python class_marks_analyzer.py
```

VS Code detects the project interpreter through `.vscode/settings.json`. Install the Microsoft Python and Pylance extensions for the best editor experience.


NAME:Aakesh kumar singh
ERP:00669