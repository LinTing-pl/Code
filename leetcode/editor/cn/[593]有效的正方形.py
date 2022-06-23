# 给定2D空间中四个点的坐标 p1, p2, p3 和 p4，如果这四个点构成一个正方形，则返回 true 。 
# 
#  点的坐标 pi 表示为 [xi, yi] 。输入 不是 按任何顺序给出的。 
# 
#  一个 有效的正方形 有四条等边和四个等角(90度角)。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# 输出: True
#  
# 
#  示例 2: 
# 
#  
# 输入：p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
# 输出：false
#  
# 
#  示例 3: 
# 
#  
# 输入：p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
# 输出：true
#  
# 
#  
# 
#  提示: 
# 
#  
#  p1.length == p2.length == p3.length == p4.length == 2 
#  -10⁴ <= xi, yi <= 10⁴ 
#  
#  Related Topics 几何 数学 👍 90 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from itertools import combinations


class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        s = set((x1 - x2) ** 2 + (y1 - y2) ** 2 for (x1, y1), (x2, y2) in combinations([p1, p2, p3, p4], 2))
        return 0 not in s and len(s) == 2
# leetcode submit region end(Prohibit modification and deletion)
