# -*- coding: utf-8 -*-
'''
leetcode 中国 题目
https://leetcode-cn.com/problemset/all/
'''

import math
import sys
import time

# 广度优先搜索二叉树（利用队列先进先出)


def BFS(treeRoot):
    if not treeRoot:
        return
    queue = []
    queue.append(treeRoot)

    while len(queue) != 0:
        node = queue.pop(0)
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# 非递归深度优先(前序)搜索二叉树 （利用盏的后进先出）


def DFS(treeRoot):
    if not treeRoot:
        return
    stack = []
    stack.append(treeRoot)
    while len(stack) != 0:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# 深度优先 中序


def DFS_M(treeRoot):
    if not treeRoot:
        return
    stack = []
    node = treeRoot
    while node or len(stack) != 0:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.val)
            node = node.right

# 深度优先 后序


def DFS_L(treeRoot):
    if not treeRoot:
        return
    stack = []
    node = treeRoot
    last = treeRoot
    while node or len(stack) != 0:
        while(node):
            stack.append(node)
            node = node.left
        node = stack[len(stack)-1]
        if not node.right or node.right == last:
            print(node.val)
            stack.pop()
            last = node
            node = None
        else:
            node = node.right

# 深度优先 递归先序


def dfs_recursive(treeRoot):
    if not treeRoot:
        return
    print(treeRoot.val)
    dfs_recursive(treeRoot.left)
    dfs_recursive(treeRoot.right)

# 树的最大深度


def max_deep(treeRoot):
    if not treeRoot:
        return 0
    return max(max_deep(treeRoot.left), max_deep(treeRoot.right)) + 1

# 树的最小深度


def min_deep(treeRoot):
    if not treeRoot:
        return 0
    children = [treeRoot.left, treeRoot.right]
    if not any(children):
        return 1
    dep = float('inf')
    for c in children:
        if c:
            dep = min(dep, min_deep(c))
    return dep + 1

# 打印先序


def print_tree(treeRoot):
    if not treeRoot:
        return
    print(treeRoot.val)
    if treeRoot.left:
        print_tree(treeRoot.left)
    if treeRoot.right:
        print_tree(treeRoot.right)

# 判断二叉树是否相同


def same_tree(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    return same_tree(t1.left, t2.left) and same_tree(t1.right, t2.right)


# 两数和，从数组中找出和为指定值的两个数的下标并返回 #1
def twoSum(nums, target):
        dic = {}
        for i in range(len(nums)):
            if dic.get(target - nums[i], None) != None:
                return [dic[target - nums[i]], i]
            else:
                dic[nums[i]] = i
        return []

# 反转整数 #7


def reverse(x: int) -> int:
    ret = 0
    max_int = sys.maxsize
    min_int = -sys.maxsize - 1
    ax = abs(x)
    while x != 0:
        pop = x - 10 * (int(x/10))
        x = int(x/10)
        if ret > (max_int / 10) or (ret == max_int / 10 and pop > 7):
            return 0
        if ret < (min_int / 10) or (ret == min_int / 10 and pop < -8):
            return 0
        ret = ret * 10 + pop

    return int(ret)

# 回文数 #9


def isPalindrome(x: int) -> bool:
    if x < 0 or (x != 0 and x % 10 == 0):
        return false
    ret = 0
    while ret < x:
        p = x % 10
        x = x // 10
        ret = ret * 10 + p
    return ret == y or x == ret // 10

# 罗马数字转整数 #13
# I:1, V:5, X:10, L:50, C:100, D:500, M:1000


def romanToInt(s: str) -> int:
    hashNum = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    ret = 0
    for i in range(len(s)):
        if i < len(s) - 1 and hashNum[s[i]] < hashNum[s[i+1]]:
            ret -= hashNum[s[i]]
        else:
            ret += hashNum[s[i]]
    return ret

# 最长公共前缀 #14


def longestCommonPrefix(strs):
    # if (len(strs) <= 0):
    #     return ''
    # prefix = strs[0]
    # for i in range(1, len(strs)):
    #     while strs[i].find(prefix) != 0:
    #         prefix = prefix[0:len(prefix)-1]
    #         if prefix == '':
    #             return ''
    # return prefix

    # 动态规划？
    if len(strs) == 0:
        return ""
    i = 0
    while i < len(strs[0]):
        c = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                strs[0] = strs[0][0:i]
        i += 1
    return strs[0]

# 有效的括号 #20


def isValid(s):
    if len(s) % 2 != 0:
        return False
    values = {
        '{': 1,
        '[': 2,
        '(': 3,
        '}': 11,
        ']': 12,
        ')': 13
    }
    ret = []
    for c in s:
        if values[c] < 10:
            ret.append(c)
        else:
            if len(ret) == 0 or values[c] - values[ret.pop()] != 10:
                return False
    return len(ret) == 0

# 合并两个有序链表 #21
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    head = ListNode(0)
    if l1.val < l2.val:
        head.val = l1.val
        l1 = l1.next
    else:
        head.val = l2.val
        l2 = l2.next
    tmp = head
    while l1 and l2:
        if l1.val < l2.val:
            tmp.next = l1
            l1 = l1.next
        else:
            tmp.next = l2
            l2 = l2.next
        tmp = tmp.next
    while l1:
        tmp.next = l1
        l1 = l1.next
        tmp = tmp.next
    while l2:
        tmp.next = l2
        l2 = l2.next
        tmp = tmp.next
    return head

# 合并两个有序数组，把nums2合并进nums1, 假设nums1空间足够 #88


def merge(nums1, m, nums2, n) -> None:
    # j = 0
    # t = m
    # for i in range(n):
    #     key = nums2[i]
    #     while j < m + n:
    #         if (j < t and nums1[j] > key) or j >= t:
    #             if j >= t:
    #                 nums1[j] = key
    #             else:
    #                 nums1.pop()
    #                 nums1.insert(j, key)
    #             t += 1
    #             j += 1
    #             break
    #         j += 1

    # 双指针法，从后往前推进
    p = m+n-1
    p1 = m-1
    p2 = n-1
    while p1 >= 0 or p2 >= 0:
        if p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
        elif p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1

# 删除排序数组中的重复项 #26


def removeDuplicates(nums) -> int:
    # if len(nums) == 0:
    #     return 0
    # flag = nums[0]
    # index = 1
    # while index < len(nums) - 1:
    #     if nums[index] == flag:
    #         del nums[index]
    #     else:
    #         flag = nums[index]
    #         index += 1
    # return len(nums)
    # 快慢指针
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] == nums[j]:
            j += 1
        else:
            nums[i+1] = nums[j]
            i += 1
    return i+1

# 移除元素 #27


def removeElement(nums, val: int) -> int:
    # l = len(nums)
    # i = 0
    # while i < l:
    #     if nums[i] == val:
    #         del nums[i]
    #         i -= 1
    #         l -= 1
    #     i += 1
    # return l

    # 双指针(快慢指针)
    i = 0
    j = 0
    while j < len(nums):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
        j += 1
    return i

    # 改变数组元素位置
    # i = 0
    # l = len(nums)
    # while i < l:
    #     if nums[i] == val:
    #         nums[i] = nums[l-1]
    #         l -= 1
    #     else:
    #         i += 1
    # return l

# 实现strStr()函数 #28


def strStr(haystack: str, needle: str) -> int:
    if len(needle) == 0:
        return 0
    if len(haystack) == 0:
        return -1
    l, n = len(haystack), len(needle)
    for start in range(l - n + 1):
        if (haystack[start:start+n] == needle):
            return start
    return -1

# 在有序数组中查找给定值的位置，如果找不到则返回插入位置 #35


def searchInsert(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left

# 盛水最多的容器 #11  双指针法 **


def maxArea(height) -> int:
    volume, left, right = 0, 0, len(height)-1
    while left < right:
        volume = max(volume, min(height[left], height[right]) * (right-left))
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return volume

# 寻找两个正序数组的中位数 #4 ***


def findMedianSortedArrays(nums1, nums2) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    len1, len2 = len(nums1), len(nums2)

    left, right, half_len = 0, len1, (len1 + len2 + 1) // 2
    mid1 = (left + right) // 2
    mid2 = half_len - mid1

    while left < right:
        if mid1 < len1 and nums2[mid1-1] > nums1[mid1]:
            left = left + 1
        else:
            right = mid1
        mid1 = (left + right) // 2
        mid2 = half_len - mid1

    if mid1 == 0:
        max_of_left = nums2[mid2 - 1]
    elif mid2 == 0:
        max_of_left = nums1[mid1 - 1]
    else:
        max_of_left = max(nums1[mid1 - 1], nums2[mid2 - 1])

    if (len1 + len2) % 2 == 1:
        return max_of_left

    if mid1 == len1:
        min_of_right = nums2[mid2]
    elif mid2 == len2:
        min_of_right = nums1[mid2]
    else:
        min_of_right = min(nums1[mid1], nums2[mid2])

    return (max_of_left + min_of_right) / 2


# 外观数列 #38
def countAndSay(n: int) -> str:
    if n <= 1:
        return '1'
    pre = countAndSay(n - 1)
    res = ''
    count = 1
    for idx in range(len(pre)):
        if idx == 0:
            count = 1
        elif pre[idx] != pre[idx-1]:
            tmp = str(count) + pre[idx-1]
            res += tmp
            count = 1
        elif pre[idx] == pre[idx-1]:
            count += 1

        if idx == len(pre) - 1:
            tmp = str(count) + pre[idx]
            res += tmp
    return res


def countAndSay2(n: int) -> str:
    pre_person = '1'
    for i in range(1, n):
        next_person, num, count = '', pre_person[0], 1
        for j in range(1, len(pre_person)):
            if pre_person[j] == num:
                count += 1
            else:
                next_person += str(count) + num
                num = pre_person[j]
                count = 1
        next_person += str(count) + num
        pre_person = next_person
    return pre_person


def heapsort(nums):
    def swap(x, y):
        tmp = nums[x]
        nums[x] = nums[y]
        nums[y] = tmp

    def maxheap(start, end):
        dad = start
        son = dad * 2 + 1
        while son <= end:
            if son+1 <= end and nums[son] < nums[son+1]:
                son += 1
            if nums[dad] > nums[son]:
                return
            else:
                swap(dad, son)
                dad = son
                son = dad * 2 + 1

    l = len(nums)
    i = l // 2 - 1
    while i >= 0:
        maxheap(i, l-1)
        i -= 1

    i = l - 1
    while i > 0:
        swap(0, i)
        maxheap(0, i - 1)
        i -= 1

    return nums

# 查找无序数组中的中位数
# 使用小顶堆


def findMid(nums):
    # 模拟小顶堆
    class Heap:
        def __init__(self, nums):
            if len(nums) == 0:
                nums = []
            nums.sort()
            self.data = nums

        def push(self, n):
            self.data.insert(0, n)
            self.data.sort()

        def pop(self):
            self.data.pop(0)

        def top(self):
            return self.data[0]

    l = len(nums)
    if l == 0:
        return 0
    if l % 2 == 1:
        s = (l+1) / 2
    else:
        s = l / 2
    s = int(s)
    heap = Heap(nums[0:s])
    for i in range(s, l):
        if nums[i] > heap.top():
            heap.pop()
            heap.push(nums[i])
        i += 1
    return heap.top()


def findMid2(nums):
    def partSort(arr, start, end):
        def swap(a, b):
            tmp = arr[a]
            arr[a] = arr[b]
            arr[b] = tmp

        left = start
        right = end
        key = arr[end]
        while left < right:
            while left < right and arr[left] <= key:
                left += 1
            while left < right and arr[right] >= key:
                right -= 1
            if left < right:
                swap(left, right)
        swap(right, end)
        return left

    start = 0
    end = len(nums) - 1
    mid = end // 2
    div = partSort(nums, start, end)
    while div != mid:
        if mid < div:
            div = partSort(nums, start, div-1)
        else:
            div = partSort(nums, div+1, end)
    return nums[mid]

# 最大子序和 #53


def maxSubArray(nums) -> int:
    pre = 0
    maxValue = nums[0]
    for i in nums:
        pre = max(pre+i, i)
        maxValue = max(maxValue, pre)
    return maxValue

# 最后一个单词的长度 #58


def lengthOfLastWord(s: str) -> int:
    s = s.strip()
    l = len(s)
    if l == 0:
        return 0
    last = ""
    i = l - 1
    while i >= 0:
        if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('z'):
            last += s[i]
        else:
            break
        i -= 1
    return len(last)

    # n = 0
    # i = len(s) - 1
    # while i >= 0:
    #     c = s[i]
    #     i -= 1
    #     if c == ' ':
    #         if n == 0:
    #             continue
    #         break
    #     n += 1
    # return n

# 加1 #66


def plusOne(digits):
    # ns = ''.join('%s' % d for d in digits)
    # n = int(ns)
    # n += 1
    # ns = str(n)
    # l = list(ns)
    # l = list(map(lambda x: int(x), l))
    # return l

    l = len(digits)
    i = l - 1
    while i >= 0:
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            break
        i -= 1
    # 9999...这种情况
    if digits[0] == 0:
        digits.insert(0, 1)
    return digits


# 二进制求和 #67
def addBinary(a: str, b: str) -> str:
    # 1转十进制求和后转二进制
    # return "{:b}".format(int(a,2) + int(b,2))
    # 2逐位计算
    ret = ""
    la = len(a) - 1
    lb = len(b) - 1
    carry = 0
    while la >= 0 or lb >= 0:
        if la < 0:
            va = 0
        else:
            va = int(a[la])
        if lb < 0:
            vb = 0
        else:
            vb = int(b[lb])
        sum = (va + vb + carry) % 2
        ret = str(sum) + ret
        carry = (va + vb + carry) // 2
        la -= 1
        lb -= 1
    if carry > 0:
        ret = str(carry) + ret
    return ret

# 求平方根(结果只要整数) #69


def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    l, r, ans = 0, x, -1
    while l <= r:
        mid = (l+r) // 2
        if mid * mid <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans

# 括号生成 #22
# def generateParenthesis(n: int):
#     def merge(*num):

#     ret = []
#     first = []
#     for i in range(n):
#         first.append('()')
#     ret.append(''.join(first))
#     for i in range(2,n):
#         j = 0
#         tmp = []
#         while j < =:

#             j += i
#     return ''.join(first)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 删除排序链表中重复的元素 #83


def deleteDuplicates(head: ListNode) -> ListNode:
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

# 相同的树 #100


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# pow(x, n)  #50


def myPow(x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

# 给定一个无序数组和一个目标值，找出数组中两个数之和等于目标值的所有组合, 并指出时间复杂度
# O(n)


def findSum(nums, target):
    m = {}
    ret = []
    for i in range(len(nums)):
        v = nums[i]
        diffIdex = m.get(target-v, None)
        if diffIdex != None and m.get(v, None) == None:
            ret.append((diffIdex, i))
        m[v] = i
    return ret


start = time.time()

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t1.left.left = TreeNode(4)

t2 = TreeNode(1)
t2.left = TreeNode(2)

print('---------')

print(findMedianSortedArrays([1, 2, 3, 9], [4, 5, 6]))

print('time cost: %f' % (time.time()-start))


import time, threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

t = threading.Thread(target=loop, name = 'loopthread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)