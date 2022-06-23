# 有两个水壶，容量分别为 jug1Capacity 和 jug2Capacity 升。水的供应是无限的。确定是否有可能使用这两个壶准确得到 
# targetCapacity 升。 
# 
#  如果可以得到 targetCapacity 升水，最后请用以上水壶中的一或两个来盛放取得的 targetCapacity 升水。 
# 
#  你可以： 
# 
#  
#  装满任意一个水壶 
#  清空任意一个水壶 
#  从一个水壶向另外一个水壶倒水，直到装满或者倒空 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
# 输出: true
# 解释：来自著名的 "Die Hard" 
# 
#  示例 2: 
# 
#  
# 输入: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
# 输出: false
#  
# 
#  示例 3: 
# 
#  
# 输入: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
# 输出: true
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= jug1Capacity, jug2Capacity, targetCapacity <= 10⁶ 
#  
#  Related Topics 深度优先搜索 广度优先搜索 数学 👍 365 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution(object):
    def __init__(self):
        self.seen = set()

    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        """
        :type jug1Capacity: int
        :type jug2Capacity: int
        :type targetCapacity: int
        :rtype: bool
        """
        stack = [(0, 0)]
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == targetCapacity or remain_y == targetCapacity or remain_x + remain_y == targetCapacity:
                return True
            if (remain_x, remain_y) in self.seen: continue
            self.seen.add((remain_x, remain_y))
            stack.append((jug1Capacity, remain_y))
            stack.append((remain_x, jug2Capacity))
            stack.append((0, remain_y))
            stack.append((remain_x, 0))
            stack.append(
                (remain_x - min(remain_x, jug2Capacity - remain_y), remain_y + min(remain_x, jug2Capacity - remain_y)))
            stack.append(
                (remain_x + min(remain_y, jug1Capacity - remain_x), remain_y - min(remain_y, jug1Capacity - remain_x)))
        return False
# leetcode submit region end(Prohibit modification and deletion)
