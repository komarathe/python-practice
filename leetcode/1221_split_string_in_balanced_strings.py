# Refer: https://leetcode.com/problems/split-a-string-in-balanced-strings/

# Balanced strings are those that have an equal quantity of 'L' and 'R'
# characters. Given a balanced string s, split it in the maximum amount of
# balanced strings.
# Return the maximum amount of split balanced strings.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        main_count = 0
        letter_count = 0
        for i in range(len(s)):
            if s[i] == "R":
                letter_count += 1
            if s[i] == "L":
                letter_count -= 1
            if letter_count == 0:
                main_count += 1
        return main_count
