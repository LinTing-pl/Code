# 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。 
# 
#  设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序
# 列化为最初的二叉搜索树。 
# 
#  编码的字符串应尽可能紧凑。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [2,1,3]
# 输出：[2,1,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数范围是 [0, 10⁴] 
#  0 <= Node.val <= 10⁴ 
#  题目数据 保证 输入的树是一棵二叉搜索树。 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 设计 二叉搜索树 字符串 二叉树 👍 268 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        arr = []

        def postOrder(root):
            if root is None:
                return
            postOrder(root.left)
            postOrder(root.right)
            arr.append(root.val)

        postOrder(root)
        return ' '.join(map(str, arr))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = list(map(int, data.split()))

        def construct(lower, upper):
            if arr == [] or arr[-1] < lower or arr[-1] > upper:
                return None
            val = arr.pop()
            root = TreeNode(val)
            root.right = construct(val, upper)
            root.left = construct(lower, val)
            return root

        return construct(float("-inf"), float("inf"))
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# leetcode submit region end(Prohibit modification and deletion)
