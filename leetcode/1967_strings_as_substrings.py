
"""
Leetcode problem no. 1967
Title: Number of Strings That Appear as Substrings in Word
Refer: https://leetcode.com/problems/number-of-strings-that-appear-as
-substrings-in-word/

Given an array of strings patterns and a string word, return the number of
strings in patterns that exist as a substring in word.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3

Example 2:
Input: patterns = ["a","b","c"], word = "aaaaabbbbb"
Output: 2
"""


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        counter = 0
        for pattern in patterns:
            if pattern in word:
                counter = counter + 1
        return counter


