"""
https://leetcode.com/problem-list/hash-table
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number
"""


class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations = [""]

        for digit in digits:
            new_combinations = []
            for combination in combinations:
                for letter in phone_map[digit]:
                    new_combinations.append(combination + letter)
            combinations = new_combinations
        return combinations