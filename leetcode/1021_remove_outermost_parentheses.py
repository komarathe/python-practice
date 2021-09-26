
"""
Leetcode problem no. 1021
Title: Remove Outermost Parenthesis
Refer: https://leetcode.com/problems/remove-outermost-parentheses/

Given a valid parentheses string s, consider its primitive decomposition:
s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in
the primitive decomposition of s.

Example 1:
    Input: s = "(()())(())"
    Output: "()()()"

Example 2:
    Input: s = "(()())(())(()(()))"
    Output: "()()()()(())"
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        counter = 0
        parenthesis = []

        for i in range(len(s)):
            if s[i] == "(" and counter == 0:
                counter += 1
            elif s[i] == "(" and counter != 0:
                parenthesis.append(s[i])
                counter += 1
            elif s[i] == ")" and counter != 1:
                parenthesis.append(s[i])
                counter -= 1
            else:
                counter -= 1

        return "".join(parenthesis)
