# 给你二叉树的根节点 root 和一个整数 distance 。 
# 
#  如果二叉树中两个 叶 节点之间的 最短路径长度 小于或者等于 distance ，那它们就可以构成一组 好叶子节点对 。 
# 
#  返回树中 好叶子节点对的数量 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 
#  输入：root = [1,2,3,null,4], distance = 3
# 输出：1
# 解释：树的叶节点是 3 和 4 ，它们之间的最短路径的长度是 3 。这是唯一的好叶子节点对。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：root = [1,2,3,4,5,6,7], distance = 3
# 输出：2
# 解释：好叶子节点对为 [4,5] 和 [6,7] ，最短路径长度都是 2 。但是叶子节点对 [4,6] 不满足要求，因为它们之间的最短路径长度为 4 。
#  
# 
#  示例 3： 
# 
#  输入：root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
# 输出：1
# 解释：唯一的好叶子节点对是 [2,5] 。
#  
# 
#  示例 4： 
# 
#  输入：root = [100], distance = 1
# 输出：0
#  
# 
#  示例 5： 
# 
#  输入：root = [1,1,1], distance = 2
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  tree 的节点数在 [1, 2^10] 范围内。 
#  每个节点的值都在 [1, 100] 之间。 
#  1 <= distance <= 10 
#  
#  Related Topics 树 深度优先搜索 二叉树 👍 109 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """

        # 对于 dfs(root,distance)，同时返回：
        # 每个叶子节点与 root 之间的距离
        # 以 root 为根节点的子树中好叶子节点对的数量
        def dfs(root, distance):
            depths = [0] * (distance + 1)
            isLeaf = not root.left and not root.right
            if isLeaf:
                depths[0] = 1
                return (depths, 0)

            leftDepths, rightDepths = [0] * (distance + 1), [0] * (distance + 1)
            leftCount = rightCount = 0

            if root.left:
                leftDepths, leftCount = dfs(root.left, distance)
            if root.right:
                rightDepths, rightCount = dfs(root.right, distance)

            for i in range(distance):
                depths[i + 1] += leftDepths[i]
                depths[i + 1] += rightDepths[i]

            cnt = 0
            for i in range(distance + 1):
                for j in range(distance - i - 1):
                    cnt += leftDepths[i] * rightDepths[j]

            return (depths, cnt + leftCount + rightCount)

        _, ret = dfs(root, distance)
        return ret
# leetcode submit region end(Prohibit modification and deletion)
