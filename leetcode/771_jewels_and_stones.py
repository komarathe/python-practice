class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        :param jewels: upper and lower case character string without spaces
        :param stones: upper and lower case character string without spaces
        :return: Total number of times each character in jewels appeared in
        stones.
        """
        jewel_chars = list(jewels)
        stone_count = 0
        for char in jewel_chars:
            stone_count = stone_count + stones.count(char)
        return stone_count
