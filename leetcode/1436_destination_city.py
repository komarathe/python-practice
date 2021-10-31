
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
        # Create a list of cities the path starts from
        from_cities = []
        # Create a list of destination cities
        to_cities = []

        for item in paths:
            # Add first city in the path to from cities
            from_cities.append(item[0])
            # Add second city in the path to destination cities
            to_cities.append(item[1])

        for item in to_cities:
            # Get the city from which there is no path that goes to any other
            # city
            if item not in from_cities:
                return item
