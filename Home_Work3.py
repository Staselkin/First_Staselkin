from datetime import datetime, timedelta

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

current_date = datetime.today().date()
start_date= string_to_date("2024.03.26")
print (current_date)
print (start_date)
diff = (current_date-start_date)
print ("Різниця у днях:", diff.days)

#def get_days_from_today(current_date, start_date):
 #   return current_date-start_date

#print (get_days_from_today)


