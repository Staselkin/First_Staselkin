import random
from random import sample

min=1
max=49
quantity=6

def get_numbers_ticket(min, max, quantity):
    numbers = random.sample(range(min, max), quantity)
    return numbers

ticket = sorted(list(get_numbers_ticket(min, max, quantity)))
print("Лотерейний квиток:", ticket)

#/////
