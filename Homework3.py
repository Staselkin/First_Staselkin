from datetime import datetime


def string_to_date(date_string):
    return datetime.strptime(date_string, '%Y.%m.%d').date()
date_string = "2024.01.01"
converted_date = string_to_date(date_string)
print (converted_date)


def date_to_string(date):
    return date.strftime('%Y.%m.%d')
date = datetime(2024,1,1).date()
newdate = date_to_string(date)
print (newdate)
