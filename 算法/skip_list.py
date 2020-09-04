# 跳表的一种实现
# https://juejin.im/post/6844903446475177998 图表讲述很清楚
# https://time.geekbang.org/column/article/42896
# https://github.com/wangzheng0822/algo/blob/master/java/17_skiplist/SkipList.java

import random

MAX_LEVEL = 16
SKIPLIST_P = 0.5

class Node(object):
    def __init__(self, val):
        self.val = val
        self.maxLevel = 0
        self.forwards = [None] * MAX_LEVEL # forward pointers

class SkipList(object):
    # private
    levelCount = 1 # 当前跳表的层级数
    head = Node(0) # 带头链表

    def __init__(self):
        pass

    def find(self, val):
        p = self.head
        for i in range(self.levelCount-1, -1, -1):
            while p.forwards[i] and p.forwards[i].val < val:
                p = p.forwards[i]
        
        if p.forwards[0] and p.forwards[0].val == val:
            return p.forwards[0]
        else:
            return None

    def insert(self, val):
        level = self.randomLevel()
        newNode = Node(val)
        newNode.maxLevel = level
        update = [None] * level
        for i in range(level):
            update[i] = self.head
        
        # 在update[]中记录小于插入值的每个级别的最大值
        # 此时update里存的是每层要插入的值的前一个节点
        p = self.head
        for i in range(level - 1, -1, -1):
            while p.forwards[i] and p.forwards[i].val < val:
                p = p.forwards[i]
            update[i] = p

        # 搜索路径中的节点下一个节点成为新节点forwards(next)
        # 这里才是插入
        for i in range(level):
            newNode.forwards[i] = update[i].forwards[i]
            update[i].forwards[i] = newNode
        
        # 更新当前跳表的层数
        if self.levelCount < level:
            self.levelCount = level

    def delete(self, val):
        update = [None] * self.levelCount
        p = self.head
        # 找出要删除节点每层的前一个节点
        for i in range(self.levelCount - 1, -1, -1):
            while p.forwards[i] and p.forwards[i].val < val:
                p = p.forwards[i]
            update[i] = p
        
        if p.forwards[0] and p.forwards[0].val == val:
            for i in range(self.levelCount - 1, -1, -1):
                if update[i].forwards[i] and update[i].forwards[i].val == val:
                    update[i].forwards[i] = update[i].forwards[i].forwards[i]
        # 更新层级数
        while self.levelCount > 1 and not self.head.forwards[self.levelCount]:
            self.levelCount -= 1

    '''
    理论来讲，一级索引中元素个数应该占原始数据的50%，二级索引中元素个数占25%，三级索引12.5% ，一直到最顶层。
    因为这里每一层的晋升概率是50%。对于每一个新插入的节点，都需要调用randomLevel生成一个合理的层数。
    该randomLevel方法会随机生成1~MAX_LEVEL之间的数，且：
             50%的概率返回1
             25%的概率返回2
           12.5%的概率返回3 ...
    '''
    def randomLevel(self):
        level = 1
        while random.random() < SKIPLIST_P and level < MAX_LEVEL:
            level += 1
        
        return level

    def __repr__(self):
        ret = []
        p = self.head
        while p.forwards[0]:
            ret.append(p.forwards[0].val)
            p = p.forwards[0]
        return '->'.join(str(num) for num in ret)

if __name__ == "__main__":
    list = SkipList()
    for i in range(10, -1, -1):
        list.insert(i)

    print(f"list:{list}, levelCount:{list.levelCount} \n")
    list.delete(3)
    print(f"list:{list}, levelCount:{list.levelCount} \n")
    node = list.find(9)
    print(node and node.val)
    