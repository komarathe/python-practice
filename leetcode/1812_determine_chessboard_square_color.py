
"""
Leetcode Problem no. 1812
Title: Determine Color of a Chessboard Square
Refer: https://leetcode.com/problems/determine-color-of-a-chessboard-square/

You are given coordinates, a string that represents the coordinates of a
square of the chessboard. Below is a chessboard for your reference.
Return true if the square is white, and false if the square is black.
The coordinate will always represent a valid chessboard square.
The coordinate will always have the letter first, and the number second.

"""


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        alphabets = ["a", "b", "c", "d", "e", "f", "g", "h"]
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        co_ord = list(coordinates)

        if (alphabets.index(co_ord[0]) + int(co_ord[1])) % 2 == 0:
            return True
