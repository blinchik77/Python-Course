"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/largest-number
"""


class Solution(object):
    def largestNumber(self, nums):
        nums = list(map(str, nums))  # поделил на строки
        nums.sort(
            key=lambda x: x * 10, reverse=True
        )  # сорт по первой, затем второй и т.д
        res = ""
        for i in range(len(nums)):
            if (
                nums[i] == "0" and nums[i - 1] not in "123456789"
            ):  # костыль на ласт тесты
                res += str(nums[i])
                return res
            else:
                res += str(nums[i])

        return res


solution = Solution()
