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
    if number == 0 or number == 1:
        return 1
    else:
        old, new = 1, 1
        for i in range(number -1):
            new, old = old, old + new
        return new

# Test:
print(fibonacci_numbers(6))
