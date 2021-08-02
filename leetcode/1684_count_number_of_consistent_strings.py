Refer: https://leetcode.com/problems/count-the-number-of-consistent-strings/

# You are given a string allowed consisting of distinct characters and an
# array of strings words. A string is consistent if all characters in the string
# appear in the string allowed.

# Return the number of consistent strings in the array words.

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        counter = 0
        for word in words:
            word_set = set(word)
            # Remove the items present in both the sets from word set
            word_set.difference_update(allowed_set)
            if len(word_set) == 0:
                counter += 1
        return counter
