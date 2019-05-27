def containsDuplicate(nums):
    count_num = {}
    for i in range(len(nums)):
        if count_num.get(nums[i]) is None:
            count_num[nums[i]] = 1
        else:
            count_num[nums[i]] = count_num.get(nums[i]) + 1
            return True
    return False