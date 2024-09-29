"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/compare-version-numbers
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = version1.split(".")
        v2 = version2.split(".")

        max_len = max(len(v1), len(v2))
        for i in range(max_len):
            if i < len(v1):
                rev1 = int(v1[i])
            else:
                rev1 = 0
            if i < len(v2):
                rev2 = int(v2[i])
            else:
                rev2 = 0
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1

        return 0
