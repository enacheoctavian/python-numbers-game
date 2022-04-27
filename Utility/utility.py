import random


def getrandomnumber():
    return random.randint(1, 100)


def compare(mynumber, guess):
    if mynumber == guess:
        return 1
    if mynumber > guess:
        return 0
    if mynumber < guess:
        return 2


def validator(number):
    if 0 < number < 101:
        return 1
    return 0

