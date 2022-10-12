# 给定一棵二叉搜索树，请找出其中第 k 大的节点的值。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 4 
# 
#  示例 2: 
# 
#  
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 4 
# 
#  
# 
#  限制： 
# 
#  
#  1 ≤ k ≤ 二叉搜索树元素个数 
#  
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 281 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def dfs(root):
            if not root: return []
            return dfs(root.left) + [root.val] + dfs(root.right)

        ans = dfs(root)
        ans.sort()
        return ans[-k]
# leetcode submit region end(Prohibit modification and deletion)
