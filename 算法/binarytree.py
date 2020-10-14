#-*- coding: utf-8 -*-
'''
二叉树相关
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# DFS（深度遍历） 分为前序、中序、后序
# 先序 递归
def preorderRecursion(root: TreeNode):
    if root:
        print(root.val, end='  ')
        preorderRecursion(root.left)
        preorderRecursion(root.right)

# 先序非递归 利用栈的后进先出
def preorderNotRecursion(root: TreeNode):
    if not root:
        return
    stack = []
    stack.append(root)
    while len(stack) > 0:
        node = stack.pop()
        print(node.val, end='  ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# 中序 递归
def middleorderRecursion(root: TreeNode):
    if root:
        middleorderRecursion(root.left)
        print(root.val, end='  ')
        middleorderRecursion(root.right)

# 中序列 非递归
def middleorderNotRecursion(root: TreeNode):
    if not root:
        return
    stack = []
    node = root
    while node or len(stack) > 0:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.val, end='  ')
            node = node.right

# 后序递归
def afterorderRecursion(root: TreeNode):
    if root:
        afterorderRecursion(root.left)
        afterorderRecursion(root.right)
        print(root.val, end='  ')

# 后续非递归 着重理解 需要标志位，右侧节点打印后才可以打印当前节点
def afterorderNotRecursion(root: TreeNode):
    if not root:
        return
    stack = []
    node = root
    last = node
    while node or len(stack) > 0:
        while node:
            stack.append(node)
            node = node.left
        node = stack[len(stack)-1] # 栈顶元素
        if not node.right or node.right == last:
            print(node.val, end='  ')
            stack.pop()
            last = node
            node = None
        else:
            node = node.right

# BFS（广度优先）利用队列的先进先出特性
def bfs(root: TreeNode):
    heap = []
    if not root:
        return
    heap.append(root)
    while len(heap) > 0:
        node = heap.pop(0)
        print(node.val, end='  ')
        if node.left:
            heap.append(node.left)
        if node.right:
            heap.append(node.right)

# 广度优先搜索，按层输出结果
def bfs_layer(root: TreeNode):
    ret = []
    if not root:
            return ret

    queue = []
    queue.append([root])
    while len(queue) != 0:
        layerNodes = queue.pop(0)

        layerRet = []
        nextLayerNodes = []
        while len(layerNodes) != 0:
            node = layerNodes.pop(0)
            layerRet.append(node.val)
            if node.left:
                nextLayerNodes.append(node.left)
            if node.right:
                nextLayerNodes.append(node.right)

        ret.append(layerRet)

        if len(nextLayerNodes) > 0:
            queue.append(nextLayerNodes)

    return ret


# 树的最大深度
def maxDepth(root: TreeNode):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

# 树的最小深度
def minDepth(treeRoot):
    if not treeRoot:
        return 0
    left = minDepth(treeRoot.left)
    right = minDepth(treeRoot.right)
    if left == 0 or right == 0:
        return left + right + 1
    return  min(left,right) + 1

# def minDepth(root: TreeNode):
#     if not root:
#         return 0
#     children = [root.left, root.right]
#     if not any(children):
#         return 1
#     depth = float('inf')  #无限大
#     for child in children:
#         if child:
#             depth = min(depth, minDepth(child))
#     return depth + 1

# 测试用例
# DFS:
# 先序: 12467835
# 中序: 47682135
# 后序: 78642531
# BFS: 12345678
#        1
#       / \
#      2    3
#     /      \
#    4        5 
#    \
#     6
#    / \
#   7   8   

if __name__ == "__main__":
    btree = TreeNode(1)
    btree.left = TreeNode(2)
    btree.left.left = TreeNode(4)
    btree.left.left.right = TreeNode(6)
    btree.left.left.right.left = TreeNode(7)
    btree.left.left.right.right = TreeNode(8)
    btree.right = TreeNode(3)
    btree.right.right = TreeNode(5)

    print('------DFS（深度优先）------')
    print('先序递归: ', end='')
    preorderRecursion(btree)
    print('')
    print('先序非递归: ', end='')
    preorderNotRecursion(btree)
    print('\n--------------------------------')
    print('中序递归: ', end='')
    middleorderRecursion(btree)
    print('')
    print('中序非递归: ', end='')
    middleorderNotRecursion(btree)
    print('\n--------------------------------')
    print('后序递归: ', end='')
    afterorderRecursion(btree)
    print('')
    print('后序非递归: ', end='')
    afterorderNotRecursion(btree)
    print('')
    print('------BFS（广度优先）------')
    bfs(btree)
    print('')
    print('树的最大深度:', maxDepth(btree))
    print('树的最小深度:', minDepth(btree))

    print(bfs_layer(btree))