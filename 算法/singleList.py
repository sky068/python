'''
leetcode: 206，141，21，19，876
单链表有关算法
'''

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

# 翻转单链表 leetcode206
def reverse(head):
    reverse_head = None
    while(head):
        next = head.next
        head.next = reverse_head
        reverse_head = head
        head = next
    return reverse_head

# 检查链表是否有环 leetcode141
def isCircle(head):
    if not head or not head.next:
        return False

    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

# 删除链表倒数第n个节点 leetcode19
def deleteNth(head, n):
    # 两次循环 O(N) 共2l - n次计算
    # guardNode = ListNode(-1)
    # guardNode.next = head
    # first = head
    # length = 0
    # while first:
    #     length += 1
    #     first = first.next
    # length -= n
    # first = guardNode
    # while length > 0:
    #     length -= 1
    #     first = first.next
    # first.next = first.next.next
    # return guardNode.next

    # 一次循环，双指针 l次计算 O(N)
    guardNode = ListNode(-1)
    guardNode.next = head
    first = guardNode
    second = guardNode
    i = 0
    while i <= n:
        i += 1
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return guardNode.next


# 返回链表的中间节点 快慢指针 leetcode876
def middleNode(head):
    if not head:
        return None
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# 合并两个有序链表 leetcode21
def mergeList(h1, h2):
    if h1 and h2:
        p1, p2 = h1, h2
        fake_node = ListNode(-1)
        cur = fake_node
        while p1 and p2:
            if p1.val < p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        cur.next = p1 if p1 else p2
        return fake_node.next
    return h1 or h2

def logList(head):
    cur = head
    data = []
    while(cur):
        data.append(cur.val)
        cur = cur.next
    print("->".join(str(num) for num in data))

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(5)
    logList(head)

    # print('-----')
    # logList(reverse(head))

    print('-----')
    head2 = ListNode(2)
    head2.next = ListNode(4)
    head2.next.next = ListNode(6)
    logList(head2)
    print('----')
    # logList(mergeList(head, head2))
    # logList(middleNode(head2))
    logList(deleteNth(head, 1))
