class Solution:
    def climbStairs(self, n):
        count = [1,2]
        for i in range(2,n):
            count.append(count[i-1]+count[i-2])
        return count[n-1]


if __name__ == "__main__":
    s = Solution()
    k = 35
    print(s.climbStairs(k))
