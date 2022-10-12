# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一
# 个。 
# 
#  更正式地说，即 root.val = min(root.left.val, root.right.val) 总成立。 
# 
#  给出这样的一个二叉树，你需要输出所有节点中的 第二小的值 。 
# 
#  如果第二小的值不存在的话，输出 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [2,2,5,null,null,5,7]
# 输出：5
# 解释：最小的值是 2 ，第二小的值是 5 。
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [2,2,2]
# 输出：-1
# 解释：最小的值是 2, 但是不存在第二小的值。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [1, 25] 内 
#  1 <= Node.val <= 2³¹ - 1 
#  对于树中每个节点 root.val == min(root.left.val, root.right.val) 
#  
#  Related Topics 树 深度优先搜索 二叉树 👍 250 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or not root.left:
            return -1
        left = root.left.val if root.left.val != root.val else self.findSecondMinimumValue(root.left)
        right = root.right.val if root.right.val != root.val else self.findSecondMinimumValue(root.right)
        return min(left, right) if left != -1 and right != -1 else max(left, right)
# leetcode submit region end(Prohibit modification and deletion)
