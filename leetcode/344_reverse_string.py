
"""
Leetcode problem: 344. Reverse String
Refer: https://leetcode.com/problems/reverse-string/
Write a function that reverses a string. The input string is given as an array
of characters s.
Example:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
