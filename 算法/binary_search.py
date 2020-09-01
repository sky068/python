# 二分查找

from typing import List

def bsearch(arr: List[int], t):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [3,4,5,6,7,8,9,9,11]
print(bsearch(arr, 9))

