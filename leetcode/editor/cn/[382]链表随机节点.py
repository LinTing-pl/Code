# 给你一个单链表，随机选择链表的一个节点，并返回相应的节点值。每个节点 被选中的概率一样 。 
# 
#  实现 Solution 类： 
# 
#  
#  Solution(ListNode head) 使用整数数组初始化对象。 
#  int getRandom() 从链表中随机选择一个节点并返回该节点的值。链表中所有节点被选中的概率相等。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
# [[[1, 2, 3]], [], [], [], [], []]
# 输出
# [null, 1, 3, 2, 2, 3]
# 
# 解释
# Solution solution = new Solution([1, 2, 3]);
# solution.getRandom(); // 返回 1
# solution.getRandom(); // 返回 3
# solution.getRandom(); // 返回 2
# solution.getRandom(); // 返回 2
# solution.getRandom(); // 返回 3
# // getRandom() 方法应随机返回 1、2、3中的一个，每个元素被返回的概率相等。 
# 
#  
# 
#  提示： 
# 
#  
#  链表中的节点数在范围 [1, 10⁴] 内 
#  -10⁴ <= Node.val <= 10⁴ 
#  至多调用 getRandom 方法 10⁴ 次 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  如果链表非常大且长度未知，该怎么处理？ 
#  你能否在不使用额外空间的情况下解决此问题？ 
#  
#  Related Topics 水塘抽样 链表 数学 随机化 👍 283 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random


class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.h = []
        while head:
            self.h.append(head)
            head = head.next

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.h).val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# leetcode submit region end(Prohibit modification and deletion)
