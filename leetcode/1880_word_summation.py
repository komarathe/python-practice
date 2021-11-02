
"""
Leetcode Problem no. 1880
Refer: https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

The letter value of a letter is its position in the alphabet starting from 0
(i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).

The numerical value of some string of lowercase English letters s is the
concatenation of the letter values of each letter in s, which is then converted
into an integer.

For example, if s = "acb", we concatenate each letter's letter value, resulting
in "021". After converting it, we get 21.
You are given three strings firstWord, secondWord, and targetWord, each
consisting of lowercase English letters 'a' through 'j' inclusive.

Return true if the summation of the numerical values of firstWord and secondWord
equals the numerical value of targetWord, or false otherwise.

Example 1:
    Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
    Output: true
    Explanation:
        The numerical value of firstWord is "acb" -> "021" -> 21.
        The numerical value of secondWord is "cba" -> "210" -> 210.
        The numerical value of targetWord is "cdb" -> "231" -> 231.
        We return true because 21 + 210 == 231.
"""


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str,
                   targetWord: str) -> bool:
        alphabets = "abcdefghijklmnopqrstuvwxyz"

        first_word_list = list(firstWord)
        second_word_list = list(secondWord)
        target_word_list = list(targetWord)

        first_letter_value = ""
        second_letter_value = ""
        target_letter_value = ""

        for letter in first_word_list:
            place = alphabets.index(letter)
            first_letter_value = first_letter_value + str(place)

        for letter in second_word_list:
            place = alphabets.index(letter)
            second_letter_value = second_letter_value + str(place)

        for letter in target_word_list:
            place = alphabets.index(letter)
            target_letter_value = target_letter_value + str(place)

        total_letter_value = int(first_letter_value) + int(second_letter_value)

        if total_letter_value == int(target_letter_value):
            return True


