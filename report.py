import csv
from datetime import date


def export_report(records: list, path: str = "report.csv") -> str:
    """Export attendance records to a CSV file."""
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["employee_id", "date", "status"])
        writer.writeheader()
        writer.writerows(records)
    return path
