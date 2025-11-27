from datetime import datetime, timedelta

def get_next_workdays(start_date: datetime, next_days_number: int):
    days = []
    next_day = start_date

    while next_days_number > 0:
        next_day += timedelta(days=1)

        if next_day.weekday() < 5:
            days.append(next_day)
            next_days_number -= 1

    return days