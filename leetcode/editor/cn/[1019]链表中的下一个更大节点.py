# 给定一个长度为 n 的链表 head 
# 
#  对于列表中的每个节点，查找下一个 更大节点 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值 严格大于 它的值。 
# 
#  返回一个整数数组 answer ，其中 answer[i] 是第 i 个节点( 从1开始 )的下一个更大的节点的值。如果第 i 个节点没有下一个更大的节点
# ，设置 answer[i] = 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：head = [2,1,5]
# 输出：[5,5,0]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [2,7,4,3,5]
# 输出：[7,0,5,5,0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数为 n 
#  1 <= n <= 10⁴ 
#  1 <= Node.val <= 10⁹ 
#  
#  Related Topics 栈 数组 链表 单调栈 👍 199 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = []
        stack_loc = []
        loc = -1
        res = []
        while head:
            loc += 1
            res.append(0)
            while stack and stack[-1] < head.val:
                res[stack_loc[-1]] = head.val
                stack.pop()
                stack_loc.pop()
            stack.append(head.val)
            stack_loc.append(loc)

            head = head.next

        return res
# leetcode submit region end(Prohibit modification and deletion)
