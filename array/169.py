class Solution:
    def majorityElement(self,nums):
        count = 1
        maj = nums[0]
        for i in range(1, len(nums)):
            if count == 0:
                maj = nums[i]
            if nums[i] == maj:
                count += 1
            else:
                count -= 1
        return maj

if __name__ == "__main__":
    s = Solution()
    nums = [2,2,1,1,1,2,2]
    print(s.majorityElement(nums))
