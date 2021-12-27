
"""
File Name: 2042_numbers_in_ascending.py
Leetcode Problem: Check if Numbers Are Ascending in a Sentence
Refer: https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

A sentence is a list of tokens separated by a single space with no leading or
trailing spaces. Every token is either a positive number consisting of digits
0-9 with no leading zeros, or a word consisting of lowercase English letters.

Given a string s representing a sentence, you need to check if all the numbers
in s are strictly increasing from left to right (i.e., other than the last
number, each number is strictly smaller than the number on its right in s).

Return true if so, or false otherwise.

Example:
    Input: s = "hello world 5 x 5"
    Output: false
"""

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s_list = s.split(" ")
        digits = []

        for item in s_list:
            if item.isnumeric():
                digits.append(int(item))
        sorted_digits = sorted(digits)
        print(sorted_digits)
        print(digits)
        if (digits == sorted_digits) and (len(digits) == len(set(digits))):
            return True
