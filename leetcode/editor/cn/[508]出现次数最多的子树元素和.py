# 给你一个二叉树的根结点 root ，请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。 
# 
#  一个结点的 「子树元素和」 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入: root = [5,2,-3]
# 输出: [2,-3,4]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入: root = [5,2,-5]
# 输出: [2]
#  
# 
#  
# 
#  提示: 
# 
#  
#  节点数在 [1, 10⁴] 范围内 
#  -10⁵ <= Node.val <= 10⁵ 
#  
#  Related Topics 树 深度优先搜索 哈希表 二叉树 👍 145 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 思路，dfs计算所有子树元素和，并用hash表存储各子树元素和出现次数
        def dfs(root):
            """自底向上地（后序遍历），记录所有子树元素和及其出现次数"""
            # 以root为根节点的树的元素和，等于，root.val+左子树元素和+右子树元素和
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            total = root.val + left + right
            hashmap[total] = hashmap.get(total, 0) + 1
            return total

        hashmap = {}
        dfs(root)
        # 对各子树元素和，按出现次数从大到小排序
        sorted_hash = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        # 取前面所有次数最多且相同的子树元素和
        res = [sorted_hash[i][0] for i in range(len(sorted_hash)) if sorted_hash[i][1] == sorted_hash[0][1]]
        return res
# leetcode submit region end(Prohibit modification and deletion)
