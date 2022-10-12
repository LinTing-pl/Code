# 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。矩形的上下边平行于 x 
# 轴，左右边平行于 y 轴。 
# 
#  如果相交的面积为 正 ，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。 
# 
#  给出两个矩形 rec1 和 rec2 。如果它们重叠，返回 true；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：rec1 = [0,0,1,1], rec2 = [2,2,3,3]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  rect1.length == 4 
#  rect2.length == 4 
#  -10⁹ <= rec1[i], rec2[i] <= 10⁹ 
#  rec1 和 rec2 表示一个面积不为零的有效矩形 
#  
#  Related Topics 几何 数学 👍 243 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return not (rec1[2] <= rec2[0] or rec2[2] <= rec1[0]) and not (rec1[3] <= rec2[1] or rec2[3] <= rec1[1])
# leetcode submit region end(Prohibit modification and deletion)
