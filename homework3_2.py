import random
from random import sample

min=1
max=49
quantity=6

def get_numbers_ticket(min, max, quantity):
    if min_num < 1:
        return []

    if max_num > 1000:
        return []

    if min_num >= max_num:
        return []

    if quantity < 1:
        return []

    if quantity > (max_num - min_num + 1):
        return []

    numbers = random.sample(range(min, max+1), quantity)
    return numbers

ticket = sorted(list(get_numbers_ticket(min, max, quantity)))
print("Лотерейний квиток:", ticket)
