# 给定在 xy 平面上的一组点，确定由这些点组成的任何矩形的最小面积，其中矩形的边不一定平行于 x 轴和 y 轴。 
# 
#  如果没有任何矩形，就返回 0。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：[[1,2],[2,1],[1,0],[0,1]]
# 输出：2.00000
# 解释：最小面积的矩形出现在 [1,2],[2,1],[1,0],[0,1] 处，面积为 2。 
# 
#  示例 2： 
# 
#  
# 
#  输入：[[0,1],[2,1],[1,1],[1,0],[2,0]]
# 输出：1.00000
# 解释：最小面积的矩形出现在 [1,0],[1,1],[2,1],[2,0] 处，面积为 1。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：[[0,3],[1,2],[3,1],[1,3],[2,1]]
# 输出：0
# 解释：没法从这些点中组成任何矩形。
#  
# 
#  示例 4： 
# 
#  
# 
#  输入：[[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
# 输出：2.00000
# 解释：最小面积的矩形出现在 [2,1],[2,3],[3,3],[3,1] 处，面积为 2。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= points.length <= 50 
#  0 <= points[i][0] <= 40000 
#  0 <= points[i][1] <= 40000 
#  所有的点都是不同的。 
#  与真实值误差不超过 10^-5 的答案将视为正确结果。 
#  
#  Related Topics 几何 数组 数学 👍 57 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import itertools


class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        EPS = 1e-7
        points = set(map(tuple, points))

        ans = float('inf')
        for p1, p2, p3 in itertools.permutations(points, 3):
            p4 = p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1]
            if p4 in points:
                v21 = complex(p2[0] - p1[0], p2[1] - p1[1])
                v31 = complex(p3[0] - p1[0], p3[1] - p1[1])
                if abs(v21.real * v31.real + v21.imag * v31.imag) < EPS:
                    area = abs(v21) * abs(v31)
                    if area < ans:
                        ans = area

        return ans if ans < float('inf') else 0
# leetcode submit region end(Prohibit modification and deletion)
