# Refer: https://leetcode.com/problems/truncate-sentence/

# A sentence is a list of words that are separated by a single space with no
# leading or trailing spaces. Each of the words consists of only uppercase and
# lowercase English letters (no punctuation).

# You are given a sentence s and an integer k.
# Truncate s such that it contains only the first k words.
# Return s after truncating it.

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        word_list = s.split(" ")
        # Use slicing to get the substring of length k
        sentence = " ".join(word_list[:k])
        return sentence
