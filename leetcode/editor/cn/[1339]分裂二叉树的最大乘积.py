# 给你一棵二叉树，它的根为 root 。请你删除 1 条边，使二叉树分裂成两棵子树，且它们子树和的乘积尽可能大。 
# 
#  由于答案可能会很大，请你将结果对 10^9 + 7 取模后再返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：root = [1,2,3,4,5,6]
# 输出：110
# 解释：删除红色的边，得到 2 棵子树，和分别为 11 和 10 。它们的乘积是 110 （11*10）
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：root = [1,null,2,3,4,null,null,5,6]
# 输出：90
# 解释：移除红色的边，得到 2 棵子树，和分别是 15 和 6 。它们的乘积为 90 （15*6）
#  
# 
#  示例 3： 
# 
#  输入：root = [2,3,9,10,7,8,6,5,4,11,1]
# 输出：1025
#  
# 
#  示例 4： 
# 
#  输入：root = [1,1]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  每棵树最多有 50000 个节点，且至少有 2 个节点。 
#  每个节点的值在 [1, 10000] 之间。 
#  
#  Related Topics 树 深度优先搜索 二叉树 👍 74 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.cur_t = 0

        def get_sum(r):
            if r:
                self.sum += r.val
                if not r.left and not r.right:
                    self.cur_t = r.val
                else:
                    get_sum(r.left)
                    get_sum(r.right)

        get_sum(root)
        self.target = self.sum / 2
        self.cur_x = abs(self.target - self.cur_t)

        def find_tar(r):
            if r:
                s = r.val
                s += find_tar(r.left)
                s += find_tar(r.right)
                cur_x = abs(s - self.target)
                if cur_x < self.cur_x:
                    self.cur_t = s
                    self.cur_x = cur_x
                return s
            else:
                return 0

        find_tar(root)
        return ((self.sum - self.cur_t) * self.cur_t) % 1000000007
# leetcode submit region end(Prohibit modification and deletion)
