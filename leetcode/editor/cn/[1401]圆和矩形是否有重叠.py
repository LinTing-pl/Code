# 给你一个以 (radius, xCenter, yCenter) 表示的圆和一个与坐标轴平行的矩形 (x1, y1, x2, y2)，其中 (x1,
# y1) 是矩形左下角的坐标，(x2, y2) 是右上角的坐标。 
# 
#  如果圆和矩形有重叠的部分，请你返回 True ，否则返回 False 。 
# 
#  换句话说，请你检测是否 存在 点 (xi, yi) ，它既在圆上也在矩形上（两者都包括点落在边界上的情况）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
# 输出：true
# 解释：圆和矩形有公共点 (1,0) 
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
# 输出：true
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：radius = 1, xCenter = 1, yCenter = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
# 输出：true
#  
# 
#  示例 4： 
# 
#  输入：radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= radius <= 2000 
#  -10^4 <= xCenter, yCenter, x1, y1, x2, y2 <= 10^4
#  x1 < x2 
#  y1 < y2 
#  
#  Related Topics 几何 数学 👍 39 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        # 条件 1：首先判断圆心是否在矩形内
        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
            return True
        # 条件 2：圆心位于矩形的上下左右四个区域
        elif xCenter > x2 and y1 <= yCenter <= y2:  # 右
            return radius >= xCenter - x2
        elif yCenter < y1 and x1 <= xCenter <= x2:  # 下
            return radius >= y1 - yCenter
        elif xCenter < x1 and y1 <= yCenter <= y2:  # 左
            return radius >= x1 - xCenter
        elif yCenter > y2 and x1 <= xCenter <= x2:  # 上
            return radius >= yCenter - y2
        else:
            # 条件 3：判断矩形的四个顶点是否在圆的内部
            return min((x1 - xCenter) ** 2 + (y2 - yCenter) ** 2,
                       (x2 - xCenter) ** 2 + (y2 - yCenter) ** 2,
                       (x2 - xCenter) ** 2 + (y1 - yCenter) ** 2,
                       (x1 - xCenter) ** 2 + (y1 - yCenter) ** 2) <= radius ** 2
# leetcode submit region end(Prohibit modification and deletion)
