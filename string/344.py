import math


class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)
        n = right - 1
        mid = math.ceil(left + (right - left) / 2)
        for i in range(mid):
            s[i], s[n - i] = s[n - i], s[i]


if __name__ == "__main__":
    s = Solution()
    k = ["H","a","n","n","a","h"]
    res = s.reverseString(k)
    print(k)
