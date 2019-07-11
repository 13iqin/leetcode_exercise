"""
常用的排序算法实现，冒泡排序，插入排序，选择排序，归并排序，快速排序
"""
import sys


def bubbleSort(array, n):
    if n <= 1:
        return array
    for i in range(n):
        stopFlag = False
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                stopFlag = True
        if not stopFlag:
            return array
    return array


def insertSort(array, n):
    if n <= 1:
        return array
    for i in range(1, n):
        value = array[i]
        j = i - 1
        for j in reversed(range(-1, j + 1)):
            print(j)
            if array[j] > value:
                array[j + 1] = array[j]
            else:
                break
        array[j + 1] = value

    return array


def selectSort(array, n):
    if n <= 1:
        return array
    for i in range(n):
        min_value_index = array.index(min(array[i:]))
        array[i],array[min_value_index] = array[min_value_index],array[i]
    return array


"""
递推公式：merge_sort(p..r) = merge(merge_sort(p..q),merge_sort(q+1,r))
终止条件：
p>=r
"""


def merge(A, p, q, r):
    tmp = list(range(r - p + 1))
    i, j, k = p, q + 1, 0
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[k] = A[i]
            k += 1
            i += 1
        else:
            tmp[k] = A[j]
            k += 1
            j += 1
    start, end = i, q
    if j <= r:
        start = j
        end = r
    while start <= end:
        tmp[k] = A[start]
        k += 1
        start += 1

    for i in range(r - p + 1):
        A[p + i] = tmp[i]


def merge_sort_c(A, p, r):
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort_c(A, p, q)
    merge_sort_c(A, q + 1, r)
    merge(A, p, q, r)
    return A


"""
递推公式：merge_sort(p..r) = merge(merge_sort(p..q),merge_sort(q+1,r))
终止条件：
p>=r
"""


def mergeSort(array, n):
    return merge_sort_c(array, 0, n - 1)


"""
递推公式：quick_sort(p..r) = quick_sort(p..q-1),quick_sort(q+1,r)
终止条件：
p>=r
"""


def partition(A, p, r):
    pivot = A[r]
    i = p
    for j in range(p, r + 1):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i


def quick_sort_c(A, p, r):
    if p >= r:
        return
    q = partition(A, p, r)
    quick_sort_c(A, p, q - 1)
    quick_sort_c(A, q + 1, r)
    return A


def quikSort(array, n):
    return quick_sort_c(array, 0, n - 1)


if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    test_list = [4, 5, 6, 3, 2, 1]
    n = len(test_list)
    print(bubbleSort(test_list, n))
    print(insertSort(test_list, n))
    print(selectSort(test_list, n))
    print(mergeSort(test_list, n))
    print(quikSort(test_list, n))
