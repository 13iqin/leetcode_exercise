class Solution:
    def twoSum(self, nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]


if __name__ == "__main__":
    s = Solution()
    nums =  [2, 7, 11, 15]
    target = 9
    print(s.twoSum(nums,target))
