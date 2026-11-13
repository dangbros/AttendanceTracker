from datetime import date


def mark_attendance(employee_id: int, status: str = "present") -> dict:
    """Record attendance for an employee on today's date."""
    record = {
        "employee_id": employee_id,
        "date": date.today().isoformat(),
        "status": status,
    }
    return record
