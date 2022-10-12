# 给定在 xy 平面上的一组点，确定由这些点组成的矩形的最小面积，其中矩形的边平行于 x 轴和 y 轴。 
# 
#  如果没有任何矩形，就返回 0。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[[1,1],[1,3],[3,1],[3,3],[2,2]]
# 输出：4
#  
# 
#  示例 2： 
# 
#  输入：[[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= points.length <= 500 
#  0 <= points[i][0] <= 40000 
#  0 <= points[i][1] <= 40000 
#  所有的点都是不同的。 
#  
#  Related Topics 几何 数组 哈希表 数学 排序 👍 115 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx = {}
        ans = float('inf')

        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1, y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0
# leetcode submit region end(Prohibit modification and deletion)
