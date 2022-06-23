# 给你一个大小为 rows x cols 的矩阵 grid 。最初，你位于左上角 (0, 0) ，每一步，你可以在矩阵中 向右 或 向下 移动。 
# 
#  在从左上角 (0, 0) 开始到右下角 (rows - 1, cols - 1) 结束的所有路径中，找出具有 最大非负积 的路径。路径的积是沿路径访问的单
# 元格中所有整数的乘积。 
# 
#  返回 最大非负积 对 10⁹ + 7 取余 的结果。如果最大积为负数，则返回 -1 。 
# 
#  注意，取余是在得到最大积之后执行的。 
# 
#  
# 
#  示例 1： 
# 
#  输入：grid = [[-1,-2,-3],
#              [-2,-3,-3],
#              [-3,-3,-2]]
# 输出：-1
# 解释：从 (0, 0) 到 (2, 2) 的路径中无法得到非负积，所以返回 -1
#  
# 
#  示例 2： 
# 
#  输入：grid = [[1,-2,1],
#              [1,-2,1],
#              [3,-4,1]]
# 输出：8
# 解释：最大非负积对应的路径已经用粗体标出 (1 * 1 * -2 * -4 * 1 = 8)
#  
# 
#  示例 3： 
# 
#  输入：grid = [[1, 3],
#              [0,-4]]
# 输出：0
# 解释：最大非负积对应的路径已经用粗体标出 (1 * 0 * -4 = 0)
#  
# 
#  示例 4： 
# 
#  输入：grid = [[ 1, 4,4,0],
#              [-2, 0,0,1],
#              [ 1,-1,1,1]]
# 输出：2
# 解释：最大非负积对应的路径已经用粗体标出 (1 * -2 * 1 * -1 * 1 * 1 = 2)
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= rows, cols <= 15 
#  -4 <= grid[i][j] <= 4 
#  
#  Related Topics 数组 动态规划 矩阵 👍 37 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        mod = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        maxgt = [[0] * n for _ in range(m)]
        minlt = [[0] * n for _ in range(m)]

        maxgt[0][0] = minlt[0][0] = grid[0][0]
        for i in range(1, n):
            maxgt[0][i] = minlt[0][i] = maxgt[0][i - 1] * grid[0][i]
        for i in range(1, m):
            maxgt[i][0] = minlt[i][0] = maxgt[i - 1][0] * grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] >= 0:
                    maxgt[i][j] = max(maxgt[i][j - 1], maxgt[i - 1][j]) * grid[i][j]
                    minlt[i][j] = min(minlt[i][j - 1], minlt[i - 1][j]) * grid[i][j]
                else:
                    maxgt[i][j] = min(minlt[i][j - 1], minlt[i - 1][j]) * grid[i][j]
                    minlt[i][j] = max(maxgt[i][j - 1], maxgt[i - 1][j]) * grid[i][j]

        if maxgt[m - 1][n - 1] < 0:
            return -1
        return maxgt[m - 1][n - 1] % mod
# leetcode submit region end(Prohibit modification and deletion)
