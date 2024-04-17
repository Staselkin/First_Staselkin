from datetime import datetime, timedelta

start_date = datetime.now().date()
print(start_date)
current_date = datetime.now()
day_of_week = current_date.weekday()
print(day_of_week)

print(start_date.year)

#def string_to_date(date_string):
 #   return datetime.strptime(date_string, "%Y.%m.%d").date()


#def find_next_weekday(start_date, weekday):
    