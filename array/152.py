def maxProduct2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    min_num = nums[0]
    max_num = nums[0]
    res = nums[0]
    for i in range(1,len(nums)):
        tmp = min_num
        min_num = min(nums[i], min(max_num * nums[i], min_num * nums[i]))
        max_num = max(nums[i], max(max_num * nums[i], tmp * nums[i]))
        res = max(max_num, res)
        print(min_num,max_num)
    return res