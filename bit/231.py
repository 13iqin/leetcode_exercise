class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n != 0) & (n & (n - 1) == 0)


if __name__ == "__main__":
    s = Solution()
    num = 16
    print(s.isPowerOfTwo(num))