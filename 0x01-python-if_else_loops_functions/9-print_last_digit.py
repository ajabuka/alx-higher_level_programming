#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        l_digit = number % 10
    else:
        l_digit = 0 - (number * - 1) % 10

    print("{:d}".format(l_digit), end='')
    return (l_digit)
