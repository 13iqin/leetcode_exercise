def intersect(nums1, nums2):
    res = []
    for i in range(len(nums1)):
        number = nums1[i]
        if number in nums2:
            nums2[nums2.index(number)] = None
            res.append(number)
    return res