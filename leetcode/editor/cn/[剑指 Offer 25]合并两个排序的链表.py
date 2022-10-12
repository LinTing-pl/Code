# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。 
# 
#  示例1： 
# 
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4 
# 
#  限制： 
# 
#  0 <= 链表长度 <= 1000 
# 
#  注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/ 
#  Related Topics 递归 链表 👍 234 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        res = ans
        while l1 and l2:
            if l1.val <= l2.val:
                ans.next = l1
                l1 = l1.next
            else:
                ans.next = l2
                l2 = l2.next
            ans = ans.next
        ans.next = l1 if l1 else l2
        return res.next

        # leetcode submit region end(Prohibit modification and deletion)
