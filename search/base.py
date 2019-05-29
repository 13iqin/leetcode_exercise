"""
常见查找方法：二分查找及其变形算法
"""


def bsearch(array, n, value):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1


"""
查找第一个值等于给定值的元素
"""

"""
查找最后一个等于给定值的元素
"""

"""
查找第一个大于等于给定值的元素
"""

"""
查找最后一个小于等于给定值的元素
"""
if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6]
    n = len(test_list)
    print(bsearch(test_list, n, 5))
    test_list2 = [1, 2, 2, 3, 3, 4, 5, 6]
