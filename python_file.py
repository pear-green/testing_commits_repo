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
    if not grades:
        return 0.0
    return sum(grades) / len(grades)


def calculate_min(grades):
    return min(grades)


def calculate_max(grades):
    return max(grades)


def calculate_pass_rate(grades, passing_threshold=50):
    if not grades:
        return 0.0
    passing = sum(1 for g in grades if g >= passing_threshold)
    return (passing / len(grades)) * 100


def assign_letter_grade(score):
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
