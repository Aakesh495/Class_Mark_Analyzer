## Author
NAME : Aakesh kumar singh
ERP : RU-26-00669


# Class Marks Analyzer

A simple, interactive Python program that summarizes student marks using NumPy. It calculates class statistics and reports pass and fail counts, pass percentage, and the number of students scoring above the class average.

## Features

- Accepts multiple marks entered on one line, separated by spaces.
- Validates that marks are finite numbers from 0 to 100, inclusive.
- Calculates the mean, median, highest mark, lowest mark, and population standard deviation.
- Classifies marks of 40 or higher as passing; marks below 40 are failing.
- Displays a formatted report with statistics to two decimal places.
- Shows a clear error and skips the report when input is invalid or empty.

## Requirements

- Python 3
- NumPy

Install NumPy if needed:

```bash
python -m pip install numpy
```

## Run the program

From the project directory, run:

```bash
python class_marks_analyzer.py
```

When prompted, enter marks separated by spaces. For example:

```text
Enter marks separated by spaces: 40 50 60 70 80
```

The program prints a report containing the mean, median, maximum, minimum, population standard deviation, passed students, failed students, pass percentage, and above-average students.

## Calculation rules

- **Pass:** mark is greater than or equal to 40.
- **Fail:** mark is less than 40.
- **Pass percentage:** passed students divided by total students, multiplied by 100.
- **Above average:** mark is strictly greater than the class mean. A mark equal to the mean is not counted.
- **Standard deviation:** population standard deviation, calculated with NumPy's `ddof=0` convention.

## Input validation

The program rejects empty input, non-numeric text, non-finite values such as `NaN` or `inf`, and marks outside the 0–100 range. It does not remove invalid entries or generate a report for invalid input.

## Example test inputs

| Input | Expected highlights |
| --- | --- |
| `40 50 60 70 80` | Mean 60.00; 5 passed; 0 failed |
| `75` | Mean 75.00; standard deviation 0.00 |
| `25 50 75 100` | Mean 62.50; 3 passed; 1 failed; pass percentage 75.00% |
| `50 abc 70` | Rejected with an invalid-mark message |
| `50 105 70` | Rejected because marks must be between 0 and 100 |

## Project file

- `class_marks_analyzer.py` — contains input handling, validation, NumPy analysis, and report display.

- ## Project Mentor

*Mentored by:* [Mr. Satyaprakash Sethy](https://github.com/SATYAPRAKASHSETHY)

*GitHub:* [@SATYAPRAKASHSETHY](https://github.com/SATYAPRAKASHSETHY)

*Role:* Python Mentor / Technical Guide


VS Code detects the project interpreter through `.vscode/settings.json`. Install the Microsoft Python and Pylance extensions for the best editor experience.


NAME:Aakesh kumar singh
ERP:00669
