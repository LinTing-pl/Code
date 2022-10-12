# 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。 
# 
#  
# 示例:
# 输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# 输出: 2
# 解释: 
# 这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
#  
# 
#  
# 
#  注意: 
# 
#  
#  3 <= points.length <= 50. 
#  不存在重复的点。 
#  -50 <= points[i][j] <= 50. 
#  结果误差值在 10^-6 以内都认为是正确答案。 
#  
#  Related Topics 几何 数组 数学 👍 96 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from itertools import combinations


class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """

        def area(p, q, r):
            return 0.5 * abs(p[0] * q[1] + q[0] * r[1] + r[0] * p[1] - p[1] * q[0] - q[1] * r[0] - r[1] * p[0])

        return max(area(*triangle) for triangle in
                   combinations(points, 3))
# leetcode submit region end(Prohibit modification and deletion)
