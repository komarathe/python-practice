
"""
Leetcode Problem No. 657
Refer: https://leetcode.com/problems/robot-return-to-origin/

There is a robot starting at the position (0, 0), the origin, on a 2D plane.
Given a sequence of its moves, judge if this robot ends up at (0, 0) after it
completes its moves.

You are given a string moves that represents the move sequence of the robot
where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left),
 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its
moves, or false otherwise.

Example 1:
    Input: moves = "UD"
    Output: true
    Explanation: The robot moves up once, and then down once. All moves have the
    same magnitude, so it ended up at the origin where it started. Therefore,
    we return true.
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        a = 0
        b = 0
        for char in moves:
            if char == "U":
                a += 1
            if char == "D":
                a -= 1
            if char == "R":
                b += 1
            if char == "L":
                b -= 1
        return a == 0 and b == 0
