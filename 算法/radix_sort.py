'''
https://time.geekbang.org/column/article/42038
基数排序
基数排序对要排序的数据是有要求的，需要可以分割出独立的“位”来比较，而且位之间有递进的关系，
如果 a 数据的高位比 b 数据大，那剩下的低位就不用比较了。除此之外，每一位的数据范围不能太大，
要可以用线性排序算法来排序，否则，基数排序的时间复杂度就无法做到 O(n) 了
比如排序11位的手机号码，可以对每一位一次进行计数排序，这样进行11次后就是有序的了
'''

from typing import List
import itertools

class RadixSort(object):

    @staticmethod
    def radixSort(arr: List[int]):
        if len(arr) <= 1:
            return

        maxValue = max(arr)
        # 从个位开始，对数组进行按‘位’进行排序
        exp = 1
        while (maxValue // exp) > 0:
            # 开始用计数排序对某一位排序
            RadixSort.countingSort(arr, exp)
            exp *= 10
    
    # 这里arr的元素范围为0-9, 所以10个桶就够了
    @staticmethod
    def countingSort(arr, exp):
        c = [0] * 10
        for i in arr:
            # 获取当前应该比较的一位(比如个位、十位)
            e = (i // exp) % 10
            c[e] += 1

        # 计算排序后的位置
        for i in range(1, len(c)):
            c[i] = c[i] + c[i - 1]
        
        # 临时数组，存储排序后的结果
        r = [None] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            pos = c[(arr[i] // exp) % 10] 
            r[pos-1] = arr[i]
            c[(arr[i] // exp) % 10] -= 1
        
        # 将结果拷贝到原数组
        arr[:] = r[:]

if __name__ == "__main__":
    arr = [135, 542, 5487, 125, 111, 9, 251, 221, 102, 105, 951, 100, 88, 67]
    print(arr)
    RadixSort.radixSort(arr)
    print(arr)