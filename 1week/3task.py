"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number
"""


class Solution(object):
    def letterCombinations(self, digits: str):

        digit_2 = ["a", "b", "c"]
        digit_3 = ["d", "e", "f"]
        digit_4 = ["g", "h", "i"]
        digit_5 = ["j", "k", "l"]
        digit_6 = ["m", "n", "o"]
        digit_7 = ["p", "q", "r", "s"]
        digit_8 = ["t", "u", "v"]
        digit_9 = ["w", "x", "y", "z"]

        number_of_answers = 1;

        for i in range(len(digits)):
            if (digits[i] == "7" or digits[i] == "9"):
                number_of_answers *=4
            else:
                number_of_answers *= 3
        print(number_of_answers)

        all_answers = [''] * number_of_answers

        for i in range(len(digits)):
            for i in range(number_of_answers):
                if (digits[i] == "7" or digits[i] == "9"):
                    for i  in range(4):
                else:
                    for i in range(3):

        print(len(digit_2))



solution = Solution()

print(solution.letterCombinations("72"))
