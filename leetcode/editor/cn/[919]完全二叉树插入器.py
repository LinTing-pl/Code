# 完全二叉树 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。 
# 
#  设计一种算法，将一个新节点插入到一个完整的二叉树中，并在插入后保持其完整。 
# 
#  实现 CBTInserter 类: 
# 
#  
#  CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构； 
#  CBTInserter.insert(int v) 向树中插入一个值为 Node.val == val的新节点 TreeNode。使树保持完全二叉树的状态
# ，并返回插入节点 TreeNode 的父节点的值； 
#  CBTInserter.get_root() 将返回树的头节点。 
#  
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入
# ["CBTInserter", "insert", "insert", "get_root"]
# [[[1, 2]], [3], [4], []]
# 输出
# [null, 1, 2, [1, 2, 3, 4]]
# 
# 解释
# CBTInserter cBTInserter = new CBTInserter([1, 2]);
# cBTInserter.insert(3);  // 返回 1
# cBTInserter.insert(4);  // 返回 2
# cBTInserter.get_root(); // 返回 [1, 2, 3, 4] 
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数量范围为 [1, 1000] 
#  0 <= Node.val <= 5000 
#  root 是完全二叉树 
#  0 <= val <= 5000 
#  每个测试用例最多调用 insert 和 get_root 操作 10⁴ 次 
#  
#  Related Topics 树 广度优先搜索 设计 二叉树 👍 69 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.deque = collections.deque()
        self.root = root
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val):
        """
        :type val: int
        :rtype: int
        """
        node = self.deque[0]
        self.deque.append(TreeNode(val))
        if not node.left:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.popleft()
        return node.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root




# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
# leetcode submit region end(Prohibit modification and deletion)
