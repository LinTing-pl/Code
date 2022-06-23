# 实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。 
# 
#  注意：本题相对原题稍作改动 
# 
#  示例： 
# 
#  输入： 1->2->3->4->5 和 k = 2
# 输出： 4 
# 
#  说明： 
# 
#  给定的 k 保证是有效的。 
#  Related Topics 链表 双指针 👍 104 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """

        def dfs(root):
            if not root: return []
            return [root.val] + dfs(root.next)

        return dfs(head)[-k]
# leetcode submit region end(Prohibit modification and deletion)
