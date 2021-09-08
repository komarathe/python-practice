
"""
Leetcode problem no. 557
Title: Reverse Words in a String III
Refer: https://leetcode.com/problems/reverse-words-in-a-string-iii/
Given a string s, reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.

Example:
    Input: s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

"""


class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(" ")
        reversed_words = []

        for word in word_list:
            reversed_words.append(word[::-1])

        return " ".join(reversed_words)
