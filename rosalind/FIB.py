#!/usr/bin/env python3

"""
File name: FIB.py
Rabbits and Recurrence Relations
Refer: http://rosalind.info/problems/fib/

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months,
if we begin with 1 pair and in each generation, every pair of reproduction-age
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""

def get_rabbit_count(months, offsprings):
    """
    :param months: Number of months
    :param offsprings: Number of pairs of rabbits reproduced by each pair
    :return: Total number of rabbits pairs for a given month
    """
    parent, child = 1, 1
    for i in range(months-1):
        child, parent = parent, parent + (child * offsprings)
    return child

# Test:
print(get_rabbit_count(5, 3))
