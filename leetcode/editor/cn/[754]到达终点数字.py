# 在一根无限长的数轴上，你站在0的位置。终点在target的位置。 
# 
#  你可以做一些数量的移动 numMoves : 
# 
#  
#  每次你可以选择向左或向右移动。 
#  第 i 次移动（从 i == 1 开始，到 i == numMoves ），在选择的方向上走 i 步。 
#  
# 
#  给定整数 target ，返回 到达目标所需的 最小 移动次数(即最小 numMoves ) 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: target = 2
# 输出: 3
# 解释:
# 第一次移动，从 0 到 1 。
# 第二次移动，从 1 到 -1 。
# 第三次移动，从 -1 到 2 。
#  
# 
#  示例 2: 
# 
#  
# 输入: target = 3
# 输出: 2
# 解释:
# 第一次移动，从 0 到 1 。
# 第二次移动，从 1 到 3 。
#  
# 
#  
# 
#  提示: 
# 
#  
#  -10⁹ <= target <= 10⁹ 
#  target != 0 
#  
#  Related Topics 数学 二分查找 👍 174 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target < 0:
            target = -target
        lst = [0, 1, 3, 2, 3, 5, 3, 5, 4, 5, 4]
        if target <= 10:
            return lst[target]
        cmin = int((target * 2 + 1 / 4) ** 0.5 - 0.5)
        if target % 2 == 0:
            for i in range(cmin, cmin + 5):
                t = i * (i + 1) // 2
                if t >= target and t % 2 == 0:
                    return i
        else:
            for i in range(cmin, cmin + 5):
                t = i * (i + 1) // 2
                if t >= target and t % 2 == 1:
                    return i
# leetcode submit region end(Prohibit modification and deletion)
