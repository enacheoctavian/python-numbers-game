import random


def getrandomnumber():
    random.randint(1, 100)


def compare(mynumber, guess):
    if mynumber == guess:
        return 1
    if mynumber > guess:
        return 0
    if mynumber < guess:
        return 2
