#!/usr/bin/env python3

"""
File name: FIBO.py
Refer: http://rosalind.info/problems/fibo/
Algorithmic Heights: Fibonacci numbers
Given: A positive integer n≤25.
Return: The value of Fn
"""

def fibonacci_numbers(number):
    """
    :param number: Number(position) in the Fibonacci sequence
    :return: The integer present at a given position in the Fibonacci sequence
    """
    if number == 0:
        return 0
    if number == 1:
        return 1

    fib_seq = [0, 1]
    for i in range(2, number+1):
        current = fib_seq[i-2] + fib_seq[i-1]
        fib_seq.append(current)
    return fib_seq[number]


# Test:
print("For input number {}, fib output is {}".format(0, fibonacci_numbers(0)))
print("For input number {}, fib output is {}".format(1, fibonacci_numbers(1)))
print("For input number {}, fib output is {}".format(8, fibonacci_numbers(8)))
