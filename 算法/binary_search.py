# 二分查找

from typing import List

# 查找等于v的值
def bsearch(arr: List[int], v):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] == v:
            return mid
        elif arr[mid] < v:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 查找第一个等于v的值
def bsearch_first(arr: List[int], v):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + ((high - low)>>1)
        if arr[mid] >= v:
            high = mid - 1
        else:
            low = mid + 1

    if low < len(arr) and arr[low] == v:
        return low
    return -1

# 和上面一样，但是好理解
# def bsearch_first(arr: List[int], v):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = low + ((high - low)>>1)
#         if arr[mid] > v:
#             high = mid - 1
#         elif (arr[mid] < v):
#             low = mid + 1
#         else:
#             if mid == 0 or (arr[mid - 1]) != v:
#                 return mid
#             else:
#                 high = mid - 1

#     return -1
    

# 查找最后一个等于v的值
def bsearch_last(arr: List[int], v):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] <= v:
            low = mid + 1
        else:
            high = mid - 1
    
    if high >= 0 and arr[high] == v:
        return high
    return -1

# 和上面一样但是好理解
# def bsearch_last(arr: List[int], v):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = low + ((high - low) >> 1)
#         if arr[mid] < v:
#             low = mid + 1
#         elif arr[mid] > v:
#             high = mid - 1
#         else:
#             if mid == len(arr) - 1 or arr[mid + 1] != v:
#                 return mid
#             else:
#                 low = mid + 1

#     return -1
    
# 查找第一个大于等于v的值
def bsearch_first_ge(arr:List[int], v):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] >= v:
            if mid == 0 or arr[mid - 1] < v:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    
    return -1

# 查找最后一个小于等于v的值
def bsearch_last_le(arr:List[int], v):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] > v:
            high = mid - 1
        else:
            if mid == len(arr) - 1 or arr[mid + 1] > v:
                    return mid
            else:
                low = mid + 1

    return -1


# 搜索升序排序旋转数组，比如[4,5,6,1,2,3] 力扣 id: 33
def bsearch_rotate_arr(arr:List[int], v):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] == v:
            return mid
        elif arr[mid] < arr[low]:
            # mid及之后是有序的
            if v >= arr[mid] and v <= arr[high]:
                low = mid
            else:
                high = mid - 1
        else:
            # mid之前是有序的
            if v >= arr[low] and v <= arr[mid]:
                high = mid
            else:
                low = mid + 1
    return -1
        
arr = [1,2,3,4,4,4,4,5,6]
print(bsearch(arr, 4))
print(bsearch_first(arr, 4))
print(bsearch_last(arr, 4))
print(bsearch_first_ge(arr, -10))
print(bsearch_last_le(arr, 100))
print('------------')
print(bsearch_rotate_arr([4,5,6,1,2,3,4], 3))
