from datetime import datetime, timedelta

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def find_next_weekday(start_date, weekday):
       
    if (weekday-start_date.weekday())<=0:
        days_aheads=(weekday-start_date.weekday()+7)
    else:
        days_aheads=(weekday-start_date.weekday())
        
    return start_date + timedelta(days=days_aheads)

start_date= string_to_date("2024.03.26")
next_monday= find_next_weekday(start_date, 0)
print(next_monday)
next_friday = find_next_weekday(start_date, 4) 
print(next_friday)    
   