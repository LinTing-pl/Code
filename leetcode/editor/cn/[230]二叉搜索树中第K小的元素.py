# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3
#  
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数为 n 。 
#  1 <= k <= n <= 10⁴ 
#  0 <= Node.val <= 10⁴ 
#  
# 
#  
# 
#  进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？ 
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 608 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def dfs(root):
            if not root: return []
            return dfs(root.left) + [root.val] + dfs(root.right)

        return dfs(root)[k - 1]

# leetcode submit region end(Prohibit modification and deletion)
