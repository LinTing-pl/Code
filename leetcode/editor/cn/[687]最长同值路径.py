# 给定一个二叉树的 root ，返回 最长的路径的长度 ，这个路径中的 每个节点具有相同值 。 这条路径可以经过也可以不经过根节点。 
# 
#  两个节点之间的路径长度 由它们之间的边数表示。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入：root = [5,4,5,1,1,5]
# 输出：2
#  
# 
#  示例 2: 
# 
#  
# 
#  
# 输入：root = [1,4,5,4,4,5]
# 输出：2
#  
# 
#  
# 
#  提示: 
# 
#  
#  树的节点数的范围是 [0, 10⁴] 
#  -1000 <= Node.val <= 1000 
#  树的深度将不超过 1000 
#  
#  Related Topics 树 深度优先搜索 二叉树 👍 564 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        def dfs(node):
            left = (node.val == node.left.val) * dfs(node.left) if node.left else 0
            # 接收左边节点返回的以左边节点为端点的最长路径，并且只有当存在左节点且左节点和当前节点值一样时才有效 否则为0
            right = (node.val == node.right.val) * dfs(node.right) if node.right else 0
            # 接收右边节点返回的以右边节点为端点的最长路径，与左节点同理
            ans[0] = max(ans[0], left + right + 1)
            # 讨论子-父-子结构的路径长度
            return max(left, right) + 1
            # 向父节点返回以当前节点为端点的路径长度

        ans = [0]
        dfs(root)
        return ans[0] - 1
        # 我们统计的是端点数 题目要求边数故减一
# leetcode submit region end(Prohibit modification and deletion)
