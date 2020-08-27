# 数据结构与算法之美 https://time.geekbang.org/column/article/41913
# 快排、归并排序

from typing import List

'''
伪码
快速排序，A是数组，n表示数组的大小
quick_sort(A, n) {
  quick_sort_c(A, 0, n-1)
}
// 快速排序递归函数，p,r为下标
quick_sort_c(A, p, r) {
  if p >= r then return
  
  q = partition(A, p, r) // 获取分区点
  quick_sort_c(A, p, q-1)
  quick_sort_c(A, q+1, r)
}
'''
# 快排 单边扫描法
def qsort(arr: List[int]):
    if not arr or len(arr) <= 1:
        return
    _qsort_c(arr, 0, len(arr) - 1)

def _qsort_c(arr, start, end):
    if start >= end:
        return
    k = _qpartition(arr, start, end)
    _qsort_c(arr, start, k-1)
    _qsort_c(arr, k+1, end)

def _swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def _qpartition(arr, start, end):
    pivot = arr[end]
    i = start
    for j in range(start, end):
        if arr[j] < pivot:
            # swap arr[i] with arr[j]
            _swap(arr, i, j)
            i += 1
    _swap(arr, i, end)
    return i

# 利用快排原理 查找数组中第k大元素
def findK(arr: List[int], k):
    return _kvalue(arr, 0, len(arr) - 1, k)

def _kvalue(arr, start, end, k):
    if start >= end:
        return None
    pivot = _qpartition(arr, start, end)
    p = pivot + 1
    if p == k:
        return arr[pivot]
    elif p > k:
        return _kvalue(arr, start, pivot - 1, k)
    else:
        return _kvalue(arr, pivot + 1, end, k)

'''
// 归并排序算法, A是数组，n表示数组大小
merge_sort(A, n) {
  merge_sort_c(A, 0, n-1)
}

// 递归调用函数
merge_sort_c(A, p, r) {
  // 递归终止条件
  if p >= r  then return

  // 取p到r之间的中间位置q
  q = (p+r) / 2
  // 分治递归
  merge_sort_c(A, p, q)
  merge_sort_c(A, q+1, r)
  // 将A[p...q]和A[q+1...r]合并为A[p...r]
  merge(A[p...r], A[p...q], A[q+1...r])
}
'''

# 归并排序
def merge_sort(arr: List[int]):
    merger_sort_c(arr, 0, len(arr) - 1)

def merger_sort_c(arr: List[int], low: int, high: int):
    if low >= high:
        return

    mid = (low + high) // 2
    # mid = low + (high - low) // 2
    merger_sort_c(arr, low, mid)
    merger_sort_c(arr, mid + 1, high)
    merger(arr, low, mid, high)

def merger(arr, low, mid, high):
    # arr[low:mid], arr[mid+1, high] are sorted.
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(arr[start: end+1])
    arr[low: high+1] = tmp



'''
我们现在需要对 D，a，F，B，c，A，z 这个字符串进行排序，
要求将其中所有小写字母都排在大写字母的前面，但小写字母内部和大写字母内部不要求有序。
比如经过排序之后为 a，c，z，D，F，B，A，这个如何来实现呢？如果字符串中存储的不仅有大小写字母，还有数字。
要将小写字母的放到前面，大写字母放在最后，数字放在中间，不用排序算法，又该怎么解决呢？
'''
def sortLetter(s:str):
    arr = list(s)
    left = 0
    right = len(arr) - 1

    # 先把小写字母数字和大写字母分开(右侧大写字母，左侧小写字母和数字)
    while left < right:
        if not arr[left].isupper():
            left += 1
        else:
            if arr[right].isupper():
                right -= 1
            else:
                _swap(arr, left, right)
    print(left)
    # 再把小写字母和数字分开
    seq = left - 1
    left = 0
    right = seq
    while left < right:
        if arr[left].islower():
            left +=1
        else:
            if arr[right].isdigit():
                right -= 1
            else:
                _swap(arr, left, right)

    return ''.join(arr)
    

if __name__ == "__main__":
    arr = [1,3,2,4,7,5,2,8,8,7,6,9,0,43,3,3,5,5,99]
    print(arr)
    merge_sort(arr)
    print(arr)

    print(findK(arr, 10))

    s = '215abI15dIIDf515dsfDF555s9dfKKj'
    print(sortLetter(s))

