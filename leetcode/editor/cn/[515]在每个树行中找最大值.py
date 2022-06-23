# 给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。 
# 
#  
# 
#  示例1： 
# 
#  
# 
#  
# 输入: root = [1,3,2,5,3,null,9]
# 输出: [1,3,9]
#  
# 
#  示例2： 
# 
#  
# 输入: root = [1,2,3]
# 输出: [1,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  二叉树的节点个数的范围是 [0,10⁴] 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 189 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        q = collections.deque([root])
        while q:
            level = []
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if not node: continue
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if level:
                res.append(level)
        return [max(i) for i in res]

# leetcode submit region end(Prohibit modification and deletion)
