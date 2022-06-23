# 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 k 。 
# 
#  返回到目标结点 target 距离为 k 的所有结点的值的列表。 答案可以以 任何顺序 返回。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# 输出：[7,4,1]
# 解释：所求结点为与目标结点（值为 5）距离为 2 的结点，值分别为 7，4，以及 1
#  
# 
#  示例 2: 
# 
#  
# 输入: root = [1], target = 1, k = 3
# 输出: []
#  
# 
#  
# 
#  提示: 
# 
#  
#  节点数在 [1, 500] 范围内 
#  0 <= Node.val <= 500 
#  Node.val 中所有值 不同 
#  目标结点 target 是树上的结点。 
#  0 <= k <= 1000 
#  
# 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 543 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """

        def dfs(root):
            if not root:
                return
            if root.left:
                mp[root.left].append(root)
                mp[root].append(root.left)
                dfs(root.left)

            if root.right:
                mp[root.right].append(root)
                mp[root].append(root.right)
                dfs(root.right)

        vis = {target}
        mp = defaultdict(list)
        dfs(root)  # 建图
        q = [target]
        while q:
            level = []
            for _ in range(len(q)):
                tmp = q.pop(0)
                level.append(tmp.val)  # 记录每层的结点
                for nex in mp[tmp]:
                    if nex not in vis:
                        vis.add(nex)
                        q.append(nex)
            k -= 1
            if k == -1:  # 层数为 k 时
                return level

        return []

        
# leetcode submit region end(Prohibit modification and deletion)
