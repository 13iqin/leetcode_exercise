def wiggleSort(nums):
    """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
    """
    if not nums or len(nums) == 1:
        return nums
    tmp = sorted(nums)
    print(tmp)
    for i in range(1, len(nums), 2):
        nums[i] = tmp.pop()
    for i in range(0, len(nums), 2):
        nums[i] = tmp.pop()
    return nums