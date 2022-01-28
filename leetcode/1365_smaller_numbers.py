
"""
File names: 1365_smaller_numbers.py
Leetcode problem: 1365.How Many Numbers Are Smaller Than the Current Number
Refer: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

Given the array nums, for each nums[i] find out how many numbers in the array
are smaller than it. That is, for each nums[i] you have to count the number of
valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:
    Input: nums = [8,1,2,2,3]
    Output: [4,0,1,1,3]

Example 2:
    Input: nums = [6,5,4,8]
    Output: [2,1,0,3]
"""


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_list = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            count_list.append(count)
        return count_list
