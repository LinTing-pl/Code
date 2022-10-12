# 给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。 
# 
#  删除完毕后，请你返回最终结果链表的头节点。 
# 
#  
# 
#  你可以返回任何满足题目要求的答案。 
# 
#  （注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。） 
# 
#  示例 1： 
# 
#  输入：head = [1,2,-3,3,1]
# 输出：[3,1]
# 提示：答案 [1,2,1] 也是正确的。
#  
# 
#  示例 2： 
# 
#  输入：head = [1,2,3,-3,4]
# 输出：[1,2,4]
#  
# 
#  示例 3： 
# 
#  输入：head = [1,2,3,-3,-2]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  给你的链表中可能有 1 到 1000 个节点。 
#  对于链表中的每个节点，节点的值：-1000 <= node.val <= 1000. 
#  
#  Related Topics 哈希表 链表 👍 163 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict


class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        presum_lastNode_dic = defaultdict(ListNode)

        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        cur_presum = 0
        while p:
            cur_presum += p.val
            presum_lastNode_dic[cur_presum] = p  # 等于这去个前缀和的最右的一个结点
            p = p.next

        cur_presum = 0
        p = dummy
        while p:
            cur_presum += p.val
            p.next = presum_lastNode_dic[cur_presum].next  # 2个结点中间，都直接删除了 要么就只有自己1个结点
            p = p.next

        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
