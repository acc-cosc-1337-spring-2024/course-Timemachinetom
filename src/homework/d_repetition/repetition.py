# Homework 3

def get_factorial(num):
    factorial = 1
    for n in range(1, num+1):
        factorial = factorial * n
    return factorial

def sum_odd_numbers(num):
    sum = 0
    n = 0
    while n < num+1:
        if n % 2 == 0:
            n += 1
        else:
            sum = sum + n
            n += 1
    return sum




