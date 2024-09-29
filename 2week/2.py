"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/multiply-strings
"""


class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                mul = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                p1 = i + j
                p2 = i + j + 1
                total = mul + result[p2]
                result[p2] = total % 10
                result[p1] += total // 10

        result_str = "".join(map(str, result))

        return result_str.lstrip("0")
