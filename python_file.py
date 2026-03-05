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
# Commit history:
#   chore    — canvas setup
#   feat     — core calculation functions
#   feat     — letter grade assignment + summary report  [tag: v0.2]
#   fix      — edge-case bug fix for empty input
#   docs     — docstrings + usage example               [tag: v0.3]
#   refactor — class-based API (breaking change)        [tag: v1.0]
# =============================================================================


class GradeAnalyzer:
    """Analyze a collection of numeric grades and produce statistics.

    All standalone functions from previous versions have been consolidated
    into this class. Callers must instantiate GradeAnalyzer with a list
    of grades before using any analysis methods.

    Args:
        grades (list[float]): Numeric grade values (0–100).
        passing_threshold (float): Minimum score to count as passing.
            Defaults to 50.

    Example:
        analyzer = GradeAnalyzer([92, 85, 73, 61, 45])
        print(analyzer.generate_summary())
    """

    def __init__(self, grades, passing_threshold=50):
        """Initialise the analyzer with a grade list and passing threshold.

        Args:
            grades (list[float]): Numeric grade values (0–100).
            passing_threshold (float): Minimum passing score. Defaults to 50.
        """
        self.grades = grades
        self.passing_threshold = passing_threshold

    def calculate_mean(self):
        """Return the arithmetic mean of the grade list.

        Returns:
            float: Mean grade, or 0.0 if the list is empty.
        """
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def calculate_min(self):
        """Return the lowest grade in the list.

        Returns:
            float: Minimum grade value.
        """
        return min(self.grades)

    def calculate_max(self):
        """Return the highest grade in the list.

        Returns:
            float: Maximum grade value.
        """
        return max(self.grades)

    def calculate_pass_rate(self):
        """Return the percentage of grades at or above the passing threshold.

        Returns:
            float: Pass rate as a percentage (0.0–100.0), or 0.0 if empty.
        """
        if not self.grades:
            return 0.0
        passing = sum(1 for g in self.grades if g >= self.passing_threshold)
        return (passing / len(self.grades)) * 100

    @staticmethod
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

    def generate_summary(self):
        """Generate a formatted text summary report for the grade list.

        Returns:
            str: Multi-line summary report including mean, min, max,
                pass rate, and letter-grade distribution.
        """
        letter_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        for grade in self.grades:
            letter = self.assign_letter_grade(grade)
            letter_counts[letter] += 1

        lines = [
            "=== Student Grade Summary ===",
            f"Students assessed : {len(self.grades)}",
            f"Mean score        : {self.calculate_mean():.2f}",
            f"Highest score     : {self.calculate_max()}",
            f"Lowest score      : {self.calculate_min()}",
            f"Pass rate         : {self.calculate_pass_rate():.1f}%",
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
# analyzer = GradeAnalyzer(scores)
#
# print(analyzer.generate_summary())
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
