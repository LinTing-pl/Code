# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [], val = 1
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [7,7,7,7], val = 7
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  列表中的节点数目在范围 [0, 10⁴] 内 
#  1 <= Node.val <= 50 
#  0 <= val <= 50 
#  
#  Related Topics 递归 链表 👍 820 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
import math


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return head
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head

# leetcode submit region end(Prohibit modification and deletion)
print(math.log10(6)*3.33)