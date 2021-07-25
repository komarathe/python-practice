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
