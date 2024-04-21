from datetime import datetime

users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    { "name": "Steve Jobs", "birthday": "1955.3.21"},
    { "name": "Jinny Lee", "birthday": "1956.3.22"},
    { "name": "John Doe", "birthday": "1985.01.23"},
    { "name": "Jane Smith", "birthday": "1990.01.27"}
]  
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def prepare_user_list(user_data):
    for user in user_data:
        user["birthday"] = string_to_date(user["birthday"])
    return user_data
prepared_users = prepare_user_list(users)
print(prepared_users)

#[{'name': 'Bill Gates', 'birthday': datetime.date(1955, 3, 25)},
 #{'name': 'Steve Jobs', 'birthday': datetime.date(1955, 3, 21)},
 #{'name': 'Jinny Lee', 'birthday': datetime.date(1956, 3, 22)}, 
 #{'name': 'John Doe', 'birthday': datetime.date(1985, 1, 23)}, 
 #{'name': 'Jane Smith', 'birthday': datetime.date(1990, 1, 27)}]

current_day = datetime.now()
current_year = current_day.year

for user in prepared_users:

    month_day = user["birthday"].replace(year=current_year)
    user["birthday"] = month_day

print(prepared_users)
