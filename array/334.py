def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) < 3:
        return False
    n1 = max(nums)
    n2 = max(nums)
    for i in nums:
        if i <= n1:
            n1 = i
        elif i <= n2:
            n2 = i
        else:
            return True
    return False