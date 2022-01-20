
"""
File name: 2114_max_words.py
Leetcode Problem No. 2114
Title: Maximum Number of Words Found in Sentences
Refer: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

Given: An array of strings sentences, where each sentences[i] represents a
single sentence.

Return: The maximum number of words that appear in a single sentence.

Example 1:
sentences = ["alice and bob love leetcode", "i think so too", "this is great
thanks very much"]
Expected Output: 6

"""

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_sen_len = max([len(item.split(" ")) for item in sentences])
        return max_sen_len

