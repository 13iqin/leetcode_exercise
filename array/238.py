def productExceptSelf(nums):
    tmp = 1
    res = []
    for i in range(len(nums)):
        res.append(tmp)
        tmp *= nums[i]
    tmp2 = 1
    for j in reversed(range(len(nums))):
        res[j] = res[j] * tmp2
        tmp2 *= nums[j]
    return res