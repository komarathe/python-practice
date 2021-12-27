
"""
File Name: 1935_max_words.py
Leetcode Problem Number: 1935
Topic: Maximum Number of Words You Can Type
Refer: https://leetcode.com/problems/maximum-number-of-words-you-can-type/

There is a malfunctioning keyboard where some letter keys do not work. All other
keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing
spaces) and a string brokenLetters of all distinct letter keys that are broken,
return the number of words in text you can fully type using this keyboard.

Example 1:
    Input: text = "hello world", brokenLetters = "ad"
    Output: 1

Example 2:
    Input: text = "leet code", brokenLetters = "lt"
    Output: 1
"""

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        words2 = words.copy()
        broken_letters_list = list(brokenLetters)

        for letter in broken_letters_list:
            for word in words:
                if (letter in word) and (word in words2):
                    words2.remove(word)
        return len(words2)
