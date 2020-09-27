# -*- coding: utf-8 -*-
'''
7种常见排序算法
快排(双向扫描)、冒泡、插入、希尔、选择、归并、堆排序
'''

# 快速排序 双向扫描法
def sortQuick(nums, start, end):
    if start >= end:
        return

    left = start
    right = end
    key = nums[left]

    while left < right:
        while left < right and nums[right] >= key:
            right -= 1
        nums[left] = nums[right]

        while left < right and nums[left] <= key:
            left += 1
        nums[right] = nums[left]
    nums[left] = key

    sortQuick(nums, start, left - 1)
    sortQuick(nums, left + 1, end)

# 冒泡排序
def sortBubble(nums):
    length = len(nums)
    i = length -1
    while i > 0:
        j = 0
        flag = False
        while j < i:
            if nums[j] > nums[j+1]:
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
                flag = True
            j += 1
        i -= 1
        if not flag:
            # 已经有序，提前结束
            break

# 插入排序
def sortInsert(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1   
        nums[j+1] = key

# 希尔排序（缩小增量的插入排序)
def sortShell(nums):
    gap = len(nums) // 2
    while gap > 0:
        for i in range(gap, len(nums)):
            key = nums[i]
            j = i - gap
            while j >= 0 and nums[j] > key:
                nums[j+gap] = nums[j]
                j -= gap
            nums[j+gap] = key
        gap = gap // 2

# 直接选择排序
def sortSelect(nums):
    for i in range(len(nums)):
        index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[index]:
                index = j
        if index != i:
            tmp = nums[i]
            nums[i] = nums[index]
            nums[index] = tmp

# 归并排序
def sortMerge(nums):
    def _merge(arr1, arr2):
        ret = []
        while len(arr1) > 0 and len(arr2) > 0:
            if arr1[0] < arr2[0]:
                ret.append(arr1.pop(0))
            else:
                ret.append(arr2.pop(0))
        ret.extend(arr1)
        ret.extend(arr2)
        return ret

    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[0:mid]
    right = nums[mid:]
    return _merge(sortMerge(left), sortMerge(right))

# 堆排序
def sortHeap(nums):
    def swap(indexA, indexB):
        tmp = nums[indexA]
        nums[indexA] = nums[indexB]
        nums[indexB]  = tmp
    
    # 堆化，自上而下处理
    def maxHeap(start, end):
        dad = start
        son = dad * 2 + 1
        while son <= end:
            if son+1 < end and nums[son+1] > nums[son]:
                son = son + 1
            if nums[son] > nums[dad]:
                swap(dad, son)
                dad = son
                son = dad * 2 + 1
            else:
                return

    # 建堆(最大堆积) 自下而上
    length = len(nums)
    for i in range(length // 2 - 1, -1, -1):
        maxHeap(i, length - 1)

    # 根节点和最后一个节点交换（根节点始终最大），然后剔除最后一个节点重新建堆
    for i in range(length-1, 0, -1):
        swap(0, i)
        maxHeap(0, i - 1)
    
# 二分查找
def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# 测试用例   
from datetime import datetime
arr = [5,1,2,3,6,8,4,4]
start = datetime.timestamp(datetime.now())
# sortQuick(arr, 0, len(arr)-1)
sortHeap(arr)
print('time used: ', (datetime.timestamp(datetime.now()) - start) * 1000, 'ms')
print(arr)
