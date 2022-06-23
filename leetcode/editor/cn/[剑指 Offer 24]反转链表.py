# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。 
# 
#  
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL 
# 
#  
# 
#  限制： 
# 
#  0 <= 节点个数 <= 5000 
# 
#  
# 
#  注意：本题与主站 206 题相同：https://leetcode-cn.com/problems/reverse-linked-list/ 
#  Related Topics 递归 链表 👍 421 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, pre = head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre
# leetcode submit region end(Prohibit modification and deletion)
