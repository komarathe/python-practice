
"""
Leetcode Problem No. 1941
Refer: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

Given a string s, return true if s is a good string, or false otherwise.
A string s is good if all the characters that appear in s have the same number
of occurrences (i.e., the same frequency).

Example 1:
    Input: s = "abacbc"
    Output: true
    Explanation: The characters that appear in s are 'a', 'b', and 'c'.
    All characters occur 2 times in s.

"""

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        char_dict = {}
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 0

        return len(set(char_dict.values())) == 1
