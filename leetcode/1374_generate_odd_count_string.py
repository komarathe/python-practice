
"""
Leetcode problem no. 1374
Title: Generate a String With Characters That Have Odd Counts
Given an integer n, return a string with n characters such that each character
in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are
multiples valid strings, return any of them.

Example:
    Input: n = 4
    Output: "pppz"

"""


class Solution:
    def generateTheString(self, n: int) -> str:
        a = "a"
        b = "b"

        if n % 2 == 0:
            return (n - 1) * a + b
        else:
            return n * a
