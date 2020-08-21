# 队列
from itertools import chain

class Queue(object):
    def __init__(self, capacities):
        self.capacities = capacities
        self.items = []
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        pass

    def dequeue(self):
        pass

    def __repr__(self):
        return '->'.join(str(item) for item in self.items[self.head:self.tail])

class ArrayQueue(Queue):
    def enqueue(self, item):
        if self.tail == self.capacities:
            if self.head == 0:
                # 队列满了
                return False
            # 搬迁数据到队首
            # i = self.head
            # while i < self.tail:
            #     self.items[i-self.head] = self.items[i]
            #     i += 1
            self.items[0 : self.tail - self.head] = self.items[self.head : self.tail]
            self.tail -= self.head
            self.head = 0

        self.items.insert(self.tail, item)
        self.tail += 1
        return True

    def dequeue(self):
        if self.head == self.tail:
            return None
        ret = self.items[self.head]
        self.head += 1
        return ret
    

# 环形队列 
class CircularQueue(Queue):
    def __init__(self, capacities):
        # 为了区分队列满要多浪费一个空间
        super(CircularQueue, self).__init__(capacities + 1)

    def enqueue(self, item):
        if (self.tail + 1) % self.capacities == self.head:
            # 队列满了
            return False
        self.items.insert(self.tail, item)
        self.tail = (self.tail + 1) % self.capacities 
        return True

    def dequeue(self):
        if self.head == self.tail:
            return None
        ret = self.items[self.head]
        self.head = (self.head + 1) % self.capacities
        return ret

    def __repr__(self):
        if self.head <= self.tail:
            return '->'.join(str(item) for item in self.items[self.head : self.tail])
        else:
            return '->'.join(str(item) for item in chain(self.items[self.head + 1:], self.items[:self.tail]))

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
    
    def dequeue(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return data
    
    def __repr__(self):
        items = []
        cur = self.head
        while cur:
            items.append(cur.data)
            cur = cur.next
        return "->".join(str(data) for data in items)

# que = ArrayQueue(3)
que = LinkedQueue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
print(que)
print(que.enqueue(4))
print(que.dequeue())
print(que)
print(que.dequeue())
print(que)
print(que.dequeue())
print(que)
print(que.enqueue(5))
print(que.enqueue(6))
print(que)