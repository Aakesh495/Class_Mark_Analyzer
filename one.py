"""Interactive class marks analyzer using NumPy."""

import math

import numpy as np


PASSING_MARK = 40


def get_marks():
    """Read, validate, and return a list of marks entered by the user.

    The function raises ``ValueError`` with a clear message when the input is
    empty, contains text, contains a non-finite number, or is out of range.
    """
    user_input = input("Enter marks separated by spaces: ").strip()

    if not user_input:
        raise ValueError("No marks entered. Please enter at least one mark.")

    marks = []
    for value in user_input.split():
        try:
            mark = float(value)
        except ValueError:
            raise ValueError(f"Invalid marks '{value}'. Enter numbers only.") from None

        if not math.isfinite(mark):
            raise ValueError("Marks must be finite numbers. NaN and infinity are not allowed.")
        if not 0 <= mark <= 100:
            raise ValueError("Marks must be between 0 and 100.")

        marks.append(mark)

    return marks


def analyze_marks(marks):
    """Calculate class statistics and performance counts for validated marks."""
    marks_array = np.array(marks, dtype=float)
    mean_mark = np.mean(marks_array)
    passed_students = int(np.sum(marks_array >= PASSING_MARK))
    total_students = len(marks_array)

    return {
        "mean" : float(mean_mark),
        "median": float(np.median(marks_array)),
        "maximum": float(np.max(marks_array)),
        "minimum": float(np.min(marks_array)),
        "standard_deviation": float(np.std(marks_array, ddof=0)),
        "passed": passed_students,
        "failed": total_students - passed_students,
        "pass_percentage": (passed_students / total_students) * 100,
        "above_average": int(np.sum(marks_array > mean_mark)),
    }


def display_report(results):
    """Print the analysis results in a neat, consistent report."""
    print("\n--- Class Marks Analysis Report ---")
    print(f"Mean                           : {results['mean']:.2f}")
    print(f"Median                         : {results['median']:.2f}")
    print(f"Maximum                        : {results['maximum']:.2f}")
    print(f"Minimum                        : {results['minimum']:.2f}")
    print(f"Population Standard Deviation  : {results['standard_deviation']:.2f}")
    print(f"Passed Students                : {results['passed']}")
    print(f"Failed Students                : {results['failed']}")
    print(f"Pass Percentage                : {results['pass_percentage']:.2f}%")
    print(f"Above-Average Students         : {results['above_average']}")


def main():
    """Run the interactive marks collection, analysis, and reporting process."""
    try:
        marks = get_marks()
        results = analyze_marks(marks)
        display_report(results)
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
