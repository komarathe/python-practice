# Refer: https://leetcode.com/problems/sorting-the-sentence/

# A sentence is a list of words that are separated by a single space with no
# leading or trailing spaces. Each word consists of lowercase and
# uppercase English letters.

# A sentence can be shuffled by appending the 1-indexed word position to each
# word then rearranging the words in the sentence.
# Given a shuffled sentence s containing no more than 9 words,
# reconstruct and return the original sentence.

# Solution 1:
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        word_dict = {}
        for word in words:
            word_dict[int(word[-1])] = word[:-1]
        sorted_dict_list = sorted(word_dict.items())

        word_list = []
        for _, val in sorted_dict_list:
            word_list.append(val)

        return " ".join(word_list)

# Solution 2:
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        word_dict = {}
        for word in words:
            word_dict[int(word[-1])] = word[:-1]
        sorted_dict_list = sorted(word_dict.items())

        word_list = []
        for _, val in sorted_dict_list:
            word_list.append(val)

        return " ".join(word_list)
