class Solution:
    def firstMissingPositive(self, nums):
        if len(nums) == 0:
            return 1;
        nums.sort()
        max_int = nums[-1]
        if max_int <= 0:
            return 1
        for i in range(1, max_int):
            if i not in nums:
                return i
        return max_int + 1


if __name__ == "__main__":
    s = Solution()
    nums = [3, 4, -1, 1]
    print(s.firstMissingPositive(nums))
