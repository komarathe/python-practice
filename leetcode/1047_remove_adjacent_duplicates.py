
"""
Leetcode problem no. 1047
Title: Remove All Adjacent Duplicates In String
Refer: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

Given a string s consisting of lowercase English letters. A duplicate removal
consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.
It can be proven that the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"

Example 2:
Input: s = "azxxzy"
Output: "ay"
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        char_stack = []
        for char in s:
            if char_stack and char == char_stack[-1]:
                char_stack.pop()
            else:
                char_stack.append(char)
        return "".join(char_stack)

