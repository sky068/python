# 桶排序 适合处理数据量大但数值范围分布均匀的数据，适合外部排序

from typing import List
class BucketSort(object):
    @staticmethod
    def bucketSort(arr:List[int], bucketSize: int): 
        if len(arr) <= 1:
            return
        
        # 找出最大最小值
        minValue = arr[0]
        maxValue = arr[len(arr) - 1]
        for i in (arr):
            if i < minValue:
                minValue = i
            elif i > maxValue:
                maxValue = i
        
        # 桶数量
        bucketCount = (maxValue - minValue) // bucketSize + 1
        # buckets = [[None for col in range(bucketSize)] for row in range(bucketCount)]
        buckets = [[] for row in range(bucketCount)]

        # 记录每个桶存入的元素数量
        indexArr = [0 for x in range(bucketCount)] 

        # 将数组值均匀的分到各个桶内
        for i in range(len(arr)):
            bucketIndex = (arr[i] - minValue) // bucketSize
            # 数组满了要扩容
            # if indexArr[bucketIndex] == len(buckets[bucketIndex]):
            #     pass
            buckets[bucketIndex].append(arr[i])
            indexArr[bucketIndex] += 1
        
        # 对每个桶进行排序，一般用快速排序
        k = 0
        for subArr in buckets:
            l = len(subArr)
            if l == 0:
                continue
            BucketSort.quickSortC(subArr, 0, l - 1)
            arr[k:(k + l)] = subArr[0:l]
            k = k + l

    # 快排递归函数
    @staticmethod
    def quickSortC(arr, low, high):
        if low >= high:
            return
        
        mid = BucketSort.partition(arr, low, high)
        BucketSort.quickSortC(arr, low, mid-1)
        BucketSort.quickSortC(arr, mid+1, high)
    
    # 快排分区函数
    @staticmethod
    def partition(arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        # swap
        arr[i], arr[high] = arr[high], arr[i]
        return i

       
if __name__ == "__main__":
    arr = [1,2,3,4,2,4,3,6,8,10,2,3,5,7,3,4,6,8,9]
    print(arr)
    BucketSort.bucketSort(arr, 5)
    print(arr)