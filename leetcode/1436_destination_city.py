
"""
Leetcode problem 1436
File name: 1436_destination_city.py
Refer: https://leetcode.com/problems/destination-city/

You are given the array paths, where paths[i] = [cityAi, cityBi] means there
exists a direct path going from cityAi to cityBi. Return the destination city,
that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop,
therefore, there will be exactly one destination city.
"""


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        list1 = []
        list2 = []
        for item in paths:
            list1.append(item[0])
            list2.append(item[1])
        for item in list2:
            if item not in list1:
                return item
