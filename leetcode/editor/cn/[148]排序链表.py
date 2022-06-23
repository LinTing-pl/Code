# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 5 * 10⁴] 内 
#  -10⁵ <= Node.val <= 10⁵ 
#  
# 
#  
# 
#  进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？ 
#  Related Topics 链表 双指针 分治 排序 归并排序 👍 1582 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if not head or not head.next: return head
        # slow, fast = head, head.next
        # while fast and fast.next:
        #     fast, slow = fast.next.next, slow.next
        # mid, slow.next = slow.next, None
        # left, right = self.sortList(head), self.sortList(mid)
        # h = res = ListNode(0)
        # while left and right:
        #     if left.val < right.val:
        #         h.next, left = left, left.next
        #     else:
        #         h.next, right = right, right.next
        #     h = h.next
        # h.next = left if left else right
        # return res.next
        cur = res = ListNode(0)

        def dfs(node):
            if not node:
                return []
            return [node.val] + dfs(node.next)

        ls = dfs(head)
        ls.sort(reverse=True)
        while ls:
            cur.next = ListNode(ls.pop())
            cur = cur.next
        return res.next

# leetcode submit region end(Prohibit modification and deletion)
