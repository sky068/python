'''
二叉查找树
二叉查找树要求，在树中的任意一个节点，其左子树中的每个节点的值，都要小于这个节点的值，而右子树节点的值都大于这个节点的值
二叉查找树中还可以支持快速地查找最大节点和最小节点、前驱节点和后继节点
还有一个重要的特性，就是中序遍历二叉查找树，可以输出有序的数据序列，时间复杂度是 O(n)，非常高效
极客时间 王争:
https://time.geekbang.org/column/article/68334

次例子不包含有相同元素的情况
'''

from binarytree import bfs_layer
from binarytree import TreeNode

class BinarySearchTree(object):
    def __init__(self):
        self.tree = None
    
    def find(self, data):
        p = self.tree
        while p != None:
            if data < p.val:
                p = p.left
            elif data > p.val:
                p = p.right
            else:
                return p

        return None
    
    def insert(self, data):
        if not self.tree:
            self.tree = TreeNode(data)
            return
        
        p = self.tree
        while p != None:
            if data > p.val:
                if p.right == None:
                    p.right = TreeNode(data)
                    return
                p = p.right
            else:
                if p.left == None:
                    p.left = TreeNode(data)
                    return
                p = p.left

    # 删除分三种情况，节点是叶子节点，节点只有一个子节点，节点有两个子节点
    def delete(self, data):
        p = self.tree # p指向即将要删除的节点
        pp = None # p的父节点
        while p != None and p.val != data:
            pp = p
            if data < p.val:
                p = p.left
            else:
                p = p.right
        
        # 未找到
        if p == None:
            return 
        
        # p有两个子节点
        # 如果节点有两个子节点，则把节点和右子树的最小节点进行替换，然后删除这个最小节点即可
        if p.left != None and p.right != None:
            minP = p.right # 在p的右子树下找最大节点
            minPP = p # 表示minP的父节点
            while minP.left != None:
                minPP = minP
                minP = minP.left
            
            p.val = minP.val
            p = minP
            pp = minPP
        
        # 删除的节点为叶子节点或者只有一个子节点
        child = None
        if p.left != None:
            child = p.left
        elif p.right != None:
            child = p.right
        
        # 删除的是根节点
        if pp == None:
            self.tree = child
        elif pp.left == p:
            pp.left = child
        else:
            pp.right = child

if  __name__ == "__main__":
    btree = BinarySearchTree()
    # 构建二叉查找树
    for i in [33,16,50,13,18,34,58,15,17,25,51,66,19,27,55]:
        btree.insert(i)
    
    print(bfs_layer(btree.tree))
    btree.delete(13)
    btree.delete(18)
    btree.delete(55)
    print(bfs_layer(btree.tree))