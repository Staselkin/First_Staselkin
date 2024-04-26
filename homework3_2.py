import random
from random import sample

min=1
max=10
quantity=6

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    if min >= max:
        return []

    numbers = random.sample(range(min, max+1), quantity)
    return numbers

ticket = sorted(list(get_numbers_ticket(min, max, quantity)))
print("Лотерейний квиток:", ticket)
