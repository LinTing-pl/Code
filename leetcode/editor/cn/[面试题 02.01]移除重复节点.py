# 编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。 
# 
#  示例1: 
# 
#  
#  输入：[1, 2, 3, 3, 2, 1]
#  输出：[1, 2, 3]
#  
# 
#  示例2: 
# 
#  
#  输入：[1, 1, 1, 1, 2]
#  输出：[1, 2]
#  
# 
#  提示： 
# 
#  
#  链表长度在[0, 20000]范围内。 
#  链表元素在[0, 20000]范围内。 
#  
# 
#  进阶： 
# 
#  如果不得使用临时缓冲区，该怎么解决？ 
#  Related Topics 哈希表 链表 双指针 👍 152 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        a = [head.val]
        res = head
        while head.next:
            if head.next.val not in a:
                a.append(head.next.val)
                head = head.next
            else:
                head.next = head.next.next
        return res
# leetcode submit region end(Prohibit modification and deletion)
