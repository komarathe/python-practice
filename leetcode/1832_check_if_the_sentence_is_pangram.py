# Refer: https://leetcode.com/problems/check-if-the-sentence-is-pangram/

# A pangram is a sentence where every letter of the English alphabet appears
# at least once.
# Given a string sentence containing only lowercase English letters, return
# true if sentence is a pangram, or false otherwise.

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                     "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                     "y", "z"]
        counter = 0
        for item in alphabets:
            # Check if a alphabet is not present in a given string
            if item not in sentence:
                counter += 1
        return counter == 0
