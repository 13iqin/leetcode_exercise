def largestNumber(nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    from functools import cmp_to_key
    key = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
    nums = [str(num) for num in nums]
    nums.sort(key=key)
    return ''.join(nums).lstrip("0") or "0"