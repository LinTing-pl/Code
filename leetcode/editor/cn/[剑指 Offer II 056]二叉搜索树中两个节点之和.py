# 给定一个二叉搜索树的 根节点 root 和一个整数 k , 请判断该二叉搜索树中是否存在两个节点它们的值之和等于 k 。假设二叉搜索树中节点的值均唯一。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: root = [8,6,10,5,7,9,11], k = 12
# 输出: true
# 解释: 节点 5 和节点 7 之和等于 12
#  
# 
#  示例 2： 
# 
#  
# 输入: root = [8,6,10,5,7,9,11], k = 22
# 输出: false
# 解释: 不存在两个节点值之和为 22 的节点
#  
# 
#  
# 
#  提示： 
# 
#  
#  二叉树的节点个数的范围是 [1, 10⁴]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  root 为二叉搜索树 
#  -10⁵ <= k <= 10⁵ 
#  
# 
#  
# 
#  注意：本题与主站 653 题相同： https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉搜索树 哈希表 双指针 二叉树 👍 25 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        def dfs(root):
            if not root:
                return []
            return dfs(root.left) + [root.val] + dfs(root.right)

        ls = dfs(root)
        i, j = 0, len(ls) - 1
        while i < j:
            if ls[i] + ls[j] < k:
                i += 1
            elif ls[i] + ls[j] > k:
                j -= 1
            else:
                return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
