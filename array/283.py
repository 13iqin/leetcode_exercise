def moveZeroes(nums):
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    for j in range(index,len(nums)):
        nums[j] = 0
    return nums