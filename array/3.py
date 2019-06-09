class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                left, right = i + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == -nums[i]:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] < -nums[i]:
                        while left < right:
                            left += 1
                            if nums[left] > nums[left - 1]:
                                break
                    else:
                        while left < right:
                            right -= 1
                            if nums[right] < nums[right + 1]:
                                break
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(nums))
