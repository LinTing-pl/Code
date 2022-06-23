# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
#  
# 
#  示例 2： 
# 
#  
# 输入：l1 = [], l2 = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  两个链表的节点数目范围是 [0, 50] 
#  -100 <= Node.val <= 100 
#  l1 和 l2 均按 非递减顺序 排列 
#  
#  Related Topics 递归 链表 👍 2210 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


# leetcode submit region end(Prohibit modification and deletion)
