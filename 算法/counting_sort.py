'''
计数排序（特殊的桶排序）适合处理元素数值范围不大的数据，每个桶内的数值都相同所以节省了对每个桶排序
计数排序只能用在数据范围不大的场景中，如果数据范围 k 比要排序的数据 n 大很多，就不适合用计数排序了。
而且，计数排序只能给非负整数排序，如果要排序的数据是其他类型的，要将其在不改变相对大小的情况下，转化为非负整数。
'''

from typing import List
import itertools

class CountingSort(object):
    # 数组元素都是正整数
    @staticmethod
    def countingSort(arr: List[int]):
        if len(arr) <= 1:
            return
        
        minValue, maxValue = arr[0], arr[len(arr) - 1]
        for i in arr:
            if i < minValue:
                minValue = i
            elif i > maxValue:
                maxValue = i
        # 每个数值对应一个桶，桶内存该数值的个数
        bucketCount = maxValue - minValue + 1
        # c的下标是数值，值是该数值的数量(默认都是0个)
        c = [0] * (bucketCount + 1)
        # 计算每个元素的数量，放入c中
        for i in range(len(arr)):
            c[arr[i]] += 1

        # 依次累加(可以快速获得数值排序后对应的位置)
        # c = list(itertools.accumulate(c))
        for i in range(1, len(c)):
            c[i] = c[i-1] + c[i]
        
        # 临时数组存储排序后的结果
        r = [None for x in range(len(arr))]
        # 这里倒序遍历，原因是为了稳定，保证相同元素的相对位置不变
        for i in range(len(arr)-1, -1, -1):
            index = c[arr[i]] - 1
            r[index] = arr[i]
            c[arr[i]] -= 1
        
        # 将结果拷贝给数组
        arr[:] = r[:]

if __name__ == "__main__":
    arr = [3,2,1,4,5,6,7,8,9,4,3,5,6,7,8,10]
    print(arr)
    CountingSort.countingSort(arr)
    print(arr)