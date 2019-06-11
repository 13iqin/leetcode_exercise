import re


class Solution:
    def myAtoi(self, str: str) -> int:
        return max(min(int(*re.findall('(^[\+\-]?\d+)\D*', str.strip())[0:1] or '0'), 2 ** 31 - 1), -2 ** 31)


if __name__ == "__main__":
    s = Solution()
    k = "42"
    k2 = "   -42"
    k3 = "4193 with words"
    k4 = "words and 987"
    k5 = "-91283472332"
    res = s.myAtoi(k4)
    print(res)
