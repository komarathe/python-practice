class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        mid = len(s) // 2
        vowel_count1 = 0
        vowel_count2 = 0

        for i in range(mid):
            if s[i] in vowels:
                vowel_count1 += 1
            if s[i + mid] in vowels:
                vowel_count2 += 1

        return vowel_count1 == vowel_count2
