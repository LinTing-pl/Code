# 给定一个整数数组，它表示BST(即 二叉搜索树 )的 先序遍历 ，构造树并返回其根。 
# 
#  保证 对于给定的测试用例，总是有可能找到具有给定需求的二叉搜索树。 
# 
#  二叉搜索树 是一棵二叉树，其中每个节点， Node.left 的任何后代的值 严格小于 Node.val , Node.right 的任何后代的值 严格大
# 于 Node.val。 
# 
#  二叉树的 前序遍历 首先显示节点的值，然后遍历Node.left，最后遍历Node.right。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：preorder = [8,5,1,7,10,12]
# 输出：[8,5,10,1,7,null,12]
#  
# 
#  示例 2: 
# 
#  
# 输入: preorder = [1,3]
# 输出: [1,null,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= preorder.length <= 100 
#  1 <= preorder[i] <= 10^8 
#  preorder 中的值 互不相同 
#  
# 
#  
#  Related Topics 栈 树 二叉搜索树 数组 二叉树 单调栈 👍 219 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if preorder:
            p, root = [[], []], TreeNode(preorder.pop(0))
            [p[val > root.val].append(val) for val in preorder]
            root.left = self.bstFromPreorder(p[0])
            root.right = self.bstFromPreorder(p[1])
            return root
# leetcode submit region end(Prohibit modification and deletion)
