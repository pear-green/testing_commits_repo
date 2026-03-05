# =============================================================================
# python_file.py — Development Canvas
# =============================================================================
#
# This file serves as the incremental development canvas for the
# Student Grade Analyzer project. It will grow commit-by-commit to
# demonstrate proper Git commit conventions including type prefixes,
# past-tense titles, What/How/Why bodies, co-author footers, and
# semantic version tags at meaningful milestones.
#
# Project: Student Grade Analyzer
# Purpose: Accept a list of numeric grades and produce statistics
#          and letter-grade breakdowns.
#
# Commit history will show:
#   chore  — canvas setup (this commit)
#   feat   — core calculation functions
#   feat   — letter grade assignment + summary report  [tag: v0.2]
#   fix    — edge-case bug fix for empty input
#   docs   — docstrings + usage example               [tag: v0.3]
#   refactor — class-based API (breaking change)      [tag: v1.0]
# =============================================================================


def calculate_mean(grades):
    """Return the arithmetic mean of a list of numeric grades.

    Args:
        grades (list[float]): Numeric grade values (0–100).

    Returns:
        float: Mean of the grades, or 0.0 if the list is empty.
    """
    if not grades:
        return 0.0
    return sum(grades) / len(grades)


def calculate_min(grades):
    """Return the lowest grade in the list.

    Args:
        grades (list[float]): Numeric grade values (0–100).

    Returns:
        float: Minimum grade value.
    """
    return min(grades)


def calculate_max(grades):
    """Return the highest grade in the list.

    Args:
        grades (list[float]): Numeric grade values (0–100).

    Returns:
        float: Maximum grade value.
    """
    return max(grades)


def calculate_pass_rate(grades, passing_threshold=50):
    """Return the percentage of grades at or above the passing threshold.

    Args:
        grades (list[float]): Numeric grade values (0–100).
        passing_threshold (float): Minimum score to count as passing.
            Defaults to 50.

    Returns:
        float: Pass rate as a percentage (0.0–100.0), or 0.0 if empty.
    """
    if not grades:
        return 0.0
    passing = sum(1 for g in grades if g >= passing_threshold)
    return (passing / len(grades)) * 100


def assign_letter_grade(score):
    """Map a numeric score to an A–F letter grade.

    Uses a standard 10-point scale:
        A: 90–100, B: 80–89, C: 70–79, D: 60–69, F: 0–59

    Args:
        score (float): Numeric score (0–100).

    Returns:
        str: Letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def generate_summary(grades, passing_threshold=50):
    """Generate a formatted text summary report for a list of grades.

    Computes mean, min, max, pass rate, and letter-grade distribution,
    then returns them as a multi-line string.

    Args:
        grades (list[float]): Numeric grade values (0–100).
        passing_threshold (float): Minimum score to count as passing.
            Defaults to 50.

    Returns:
        str: Multi-line summary report.
    """
    letter_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for grade in grades:
        letter = assign_letter_grade(grade)
        letter_counts[letter] += 1

    lines = [
        "=== Student Grade Summary ===",
        f"Students assessed : {len(grades)}",
        f"Mean score        : {calculate_mean(grades):.2f}",
        f"Highest score     : {calculate_max(grades)}",
        f"Lowest score      : {calculate_min(grades)}",
        f"Pass rate         : {calculate_pass_rate(grades, passing_threshold):.1f}%",
        "",
        "Letter grade breakdown:",
    ]
    for letter, count in letter_counts.items():
        lines.append(f"  {letter}: {count}")

    return "\n".join(lines)


# =============================================================================
# Usage example
# =============================================================================
#
# scores = [92, 85, 73, 61, 45, 88, 79, 95, 52, 67]
#
# print(generate_summary(scores))
#
# Output:
#   === Student Grade Summary ===
#   Students assessed : 10
#   Mean score        : 73.70
#   Highest score     : 95
#   Lowest score      : 45
#   Pass rate         : 80.0%
#
#   Letter grade breakdown:
#     A: 2
#     B: 2
#     C: 2
#     D: 2
#     F: 2
# =============================================================================
