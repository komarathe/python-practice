# Refer: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

# Given a Valid Parentheses String represented as string s, return the nesting
# depth of s.

class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = 0
        max_depth = 0
        char_list = list(s)
        for char in char_list:
            if char == "(":
                current_depth += 1
            if char == ")":
                current_depth -= 1
            if current_depth > max_depth:
                max_depth = current_depth
        return max_depth
