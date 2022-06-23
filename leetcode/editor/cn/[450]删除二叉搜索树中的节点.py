# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的
# 根节点的引用。 
# 
#  一般来说，删除节点可分为两个步骤： 
# 
#  
#  首先找到需要删除的节点； 
#  如果找到了，删除它。 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入：root = [5,3,6,2,4,null,7], key = 3
# 输出：[5,4,6,2,null,null,7]
# 解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
# 另一个正确答案是 [5,2,6,null,4,null,7]。
# 
# 
#  
# 
#  示例 2: 
# 
#  
# 输入: root = [5,3,6,2,4,null,7], key = 0
# 输出: [5,3,6,2,4,null,7]
# 解释: 二叉树不包含值为 0 的节点
#  
# 
#  示例 3: 
# 
#  
# 输入: root = [], key = 0
# 输出: [] 
# 
#  
# 
#  提示: 
# 
#  
#  节点数的范围 [0, 10⁴]. 
#  -10⁵ <= Node.val <= 10⁵ 
#  节点值唯一 
#  root 是合法的二叉搜索树 
#  -10⁵ <= key <= 10⁵ 
#  
# 
#  
# 
#  进阶： 要求算法时间复杂度为 O(h)，h 为树的高度。 
#  Related Topics 树 二叉搜索树 二叉树 👍 742 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

    def getSuccessor(self, root):
        """获取root的后继节点"""
        root = root.right  # 定位到root右子树
        while root.left:  # 寻找右子树中最靠左的节点
            root = root.left
        return root

    def getPrecursor(self, root):
        """获取root的前驱节点"""
        root = root.left  # 定位到root左子树
        while root.right:  # 寻找左子树中最靠右的节点
            root = root.right
        return root

    def deleteNode(self, root, key):
        """删除具有key值的节点，并返回删除后的根节点"""
        if not root:
            return None
        # 最外层的if...elif...else用于搜索待删除结点
        if root.val > key:  # 待删除结点值小于根节点，位于根节点左子树
            root.left = self.deleteNode(root.left, key)  # 递归删除左子树，并返回删除后的左子树
        elif root.val < key:  # 待删除结点值大于根节点，位于根节点右子树
            root.right = self.deleteNode(root.right, key)  # 递归删除右子树，并返回删除后的右子树
        else:  # 待删除节点为根节点
            if not root.left and not root.right:  # 对应情况1，待删除结点没有子节点
                root = None  # 将该节点置空
            elif not root.left and root.right:  # 对应情况2，待删除节点只有右节点
                root = root.right  # 用右节点代替该节点
            elif not root.right and root.left:  # 对应情况2，待删除节点只有左节点
                root = root.left  # 用左节点代替该节点
            else:  # 对应情况3，待删除节点有左右两个节点
                succ = self.getSuccessor(root)  # 找到后继节点
                root.val = succ.val  # 将值替换为后继节点的值
                root.right = self.deleteNode(root.right, succ.val)  # 删除没用的后继节点
        return root
# leetcode submit region end(Prohibit modification and deletion)
