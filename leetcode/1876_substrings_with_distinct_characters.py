
"""
File Name: 1876_substrings_with_distinct_characters.py
Leetcode Problem: 1876. Substrings of Size Three with Distinct Characters
Refer: https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

A string is good if there are no repeated characters.
Given a string s, return the number of good substrings of length three in s.
Note that if there are multiple occurrences of the same substring,
every occurrence should be counted.
A substring is a contiguous sequence of characters in a string.

Example 1:
    Input: s = "xyzzaz"
    Output: 1

Example 2:
    Input: s = "aababcabc"
    Output: 4
"""


class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        substrings_list = []

        for i in range(0, len(s) - 2):
            substring = s[i:i + 3]
            if len(set(substring)) == 3:
                substrings_list.append(substring)

        return len(substrings_list)
