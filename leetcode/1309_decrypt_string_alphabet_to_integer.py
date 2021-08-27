
"""
Leetcode
1309. Decrypt String from Alphabet to Integer Mapping
Refer: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

Given a string s formed by digits ('0' - '9') and '#'.
We want to map s to English lowercase characters as follows:
Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.

Return the string formed after mapping.
"""

class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(26, 0, -1):
            if i > 9:
                s = s.replace(str(i) + "#", chr(96 + i))
            else:
                s = s.replace(str(i), chr(96 + i))
        return s
