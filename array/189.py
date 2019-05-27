def rotate(nums, k):
    k = k % len(nums)
    nums.reverse()
    nums[0:k] = reversed(nums[0:k])
    nums[k:] = reversed(nums[k:])