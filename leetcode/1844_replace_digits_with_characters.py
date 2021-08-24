# Refer: https://leetcode.com/problems/replace-all-digits-with-characters/

# You are given a 0-indexed string s that has lowercase English letters in
# its even indices and digits in its odd indices.

# There is a function shift(c, x), where c is a character and x is a digit,
# that returns the xth character after c.

# For every odd index i, you want to replace the digit s[i] with
# shift(s[i-1], s[i]).
# Return s after replacing all digits. It is guaranteed that shift(s[i-1],
# s[i]) will never exceed 'z'.

class Solution:
    def replaceDigits(self, s: str) -> str:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        s_list = []
        for i in range(len(s)):
            if i % 2 == 0:
                s_list.append(s[i])
            else:
                alphabet_index = alphabets.find(s[i - 1])
                s_list.append(alphabets[int(s[i]) + alphabet_index])
        return "".join(s_list)
