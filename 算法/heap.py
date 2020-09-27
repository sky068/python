'''
堆是一种特殊的树，满足两个条件：
1、堆是一个完全二叉树
2、堆中每一个节点的值都必须大于或者小于子节点的值（大顶堆、小顶堆）
'''

from typing import List

class Heap(object):
    def __init__(self, capacity):
        super().__init__()
        self.data = [None] * (capacity + 1) #数组，从下标1开始存储数据（方便计算左右子节点）
        self.capacity = capacity # 堆可以存储的最大数据个数
        self.count = 0 # 堆中当前已经存储的数据个数
    
    def insert(self, d):
        if self.count >= self.capacity:
            print("堆满了")
            return
        self.count += 1
        self.data[self.count] = d
        i = self.count
        # 自下而上堆化
        while i//2 > 0 and self.data[i] > self.data[i//2]:
            tmp = self.data[i//2]
            self.data[i//2] = self.data[i]
            self.data[i] = tmp
            i = i//2
    
    # 删除堆顶元素
    def removeTop(self):
        if self.count == 0:
            print('堆中没有数据')
            return
        
        self.data[1] = self.data[self.count]
        self.data[self.count] = None
        self.count -= 1
        # 重新堆化
        self._heapify(self.count, 1)
    
    def _heapify(self, n, i):
        # 自上而下堆化
        while True:
            maxPos = i
            if i * 2 <= n and self.data[i] < self.data[i*2]:
                maxPos = i * 2
            if (i * 2 + 1) <= n and self.data[maxPos] < self.data[i*2+1]:
                maxPos = i * 2 + 1
            
            if maxPos == i:
                break

            tmp = self.data[maxPos]
            self.data[maxPos] = self.data[i]
            self.data[i] = tmp

            i = maxPos
    def __repr__(self):
        return ' '.join(str(i) for i in self.data)

# 堆排序
def heapSort(arr:List[int]):
    n = len(arr)
    if n <= 1:
        return

    buildHeap(arr)
    last = n - 1
    while last > 0:
        tmp = arr[last]
        arr[last] = arr[0]
        arr[0] = tmp
        heapify(arr, 0, last)
        last -= 1
    
def buildHeap(arr:List[int]):
    # 自下而上建堆
    # 从n/2 到 1开始堆化, n/2 + 1到n都是叶子节点不用处理
    for i in range(len(arr)//2, -1, -1):
        heapify(arr, i, len(arr))

def heapify(arr, start, end):
    # 自上而下堆化
    while(True):
        maxPos = start
        if start * 2 + 1 < end and arr[start] < arr[start * 2 + 1]:
            maxPos = start * 2 + 1
        if (start * 2 + 2) < end and arr[maxPos] < arr[start * 2 + 2]:
            maxPos = start * 2 + 2
        if maxPos == start:
            break
        tmp = arr[maxPos]
        arr[maxPos] = arr[start]
        arr[start] = tmp
        start = maxPos


if __name__ == "__main__":
    heap = Heap(10)
    for i in range(11):
        heap.insert(i)

    print(heap)
    heap.removeTop()
    print(heap)

    print('------堆排序-----')
    arr = [3,4,2,5,1,7,8,2,6]
    heapSort(arr)
    print(arr)