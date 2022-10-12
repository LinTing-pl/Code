# 给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。. 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root1 = [2,1,4], root2 = [1,0,3]
# 输出：[0,1,1,2,3,4]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root1 = [1,null,8], root2 = [8,1]
# 输出：[1,1,8,8]
#  
# 
#  
# 
#  提示： 
# 
#  
#  每棵树的节点数在 [0, 5000] 范围内 
#  -10⁵ <= Node.val <= 10⁵ 
#  
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 排序 👍 159 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """

        def inorder(node, res):
            if node:
                inorder(node.left, res)
                res.append(node.val)
                inorder(node.right, res)

        nums1, nums2 = [], []
        inorder(root1, nums1)
        inorder(root2, nums2)

        merged = []
        p1, n1 = 0, len(nums1)
        p2, n2 = 0, len(nums2)
        while True:
            if p1 == n1:
                merged.extend(nums2[p2:])
                break
            if p2 == n2:
                merged.extend(nums1[p1:])
                break
            if nums1[p1] < nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1
        return merged
# leetcode submit region end(Prohibit modification and deletion)
