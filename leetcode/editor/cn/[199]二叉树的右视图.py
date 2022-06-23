# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
#  
# 
#  示例 2: 
# 
#  
# 输入: [1,null,3]
# 输出: [1,3]
#  
# 
#  示例 3: 
# 
#  
# 输入: []
# 输出: []
#  
# 
#  
# 
#  提示: 
# 
#  
#  二叉树的节点个数的范围是 [0,100] 
#  -100 <= Node.val <= 100 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 669 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def rightSideView(self, root):
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
                res.append(level[-1])
        return res

# leetcode submit region end(Prohibit modification and deletion)
