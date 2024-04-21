from datetime import datetime, timedelta

def get_days_from_today(date):
    date = datetime.strptime(date, "%Y.%m.%d").date()
    current_date = datetime.today().date()
    diff = (current_date-date)
    return diff.days
date = ("2024.10.09")
print(get_days_from_today(date))

