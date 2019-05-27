def majorityElement2(nums):
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