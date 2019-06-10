import math
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = math.floor(left + (right - left) / 2)
            sqt =  mid * mid
            if sqt > x:
                right = mid - 1
            elif sqt < x:
                left = mid + 1
            else:
                return int(mid)
        return int(right)


if __name__ == "__main__":
    s = Solution()
    k = 8
    res = s.mySqrt(k)
    print(res)
