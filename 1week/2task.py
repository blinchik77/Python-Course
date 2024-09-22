"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/integer-to-roman
"""


class Solution(object):
    def intToRoman(self, num):
        res = ""
        while num > 0:
            if num >= 1000:
                res += "M"* (num//1000)
                num -= 1000 * (num//1000)
            elif num >= 900:
                res += "CM"
                num -= 900
            elif num >= 500:
                res += "D" * (num // 500)
                num -= 500 * (num // 500)
            elif num >= 400:
                res += "CD"
                num -= 400
            elif num >= 100:
                res += "C" * (num // 100)
                num -= 100 * (num // 100)
            elif num >= 90:
                res += "XC"
                num -= 90
            elif num >= 50:
                res += "L" * (num // 50)
                num -= 50 * (num // 50)
            elif num >= 40:
                res += "XL"
                num -= 40
            elif num >= 10:
                res += "X" * (num // 10)
                num -= 10 * (num // 10)
            elif num >= 9:
                res += "IX"
                num -= 9
            elif num >= 5:
                res += "V" * (num // 5)
                num -= 5 * (num // 5)
            elif num >= 4:
                res += "IV"
                num -= 4
            else:
                res += "I" * num
                num = 0
        return res

solution = Solution()
