
"""
File Name: 1512_good_pairs.py
Leetcode Problem: 1512
Title: Number of Good Pairs
Refer: https://leetcode.com/problems/number-of-good-pairs/

Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example:
    Input: nums = [1,2,3,1,1,3]
    Expected Output: 4
    Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5)
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = []
        for i, num in enumerate(nums):
            for j, num in enumerate(nums):
                if (i < j) and (nums[i] == nums[j]):
                    # Create tuple of the good pair
                    good_pair = (nums[i], nums[j])
                    good_pairs.append(good_pair)
        return len(good_pairs)

