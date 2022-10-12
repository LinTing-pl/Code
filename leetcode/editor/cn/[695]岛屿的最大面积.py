# 给你一个大小为 m x n 的二进制矩阵 grid 。 
# 
#  岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都
# 被 0（代表水）包围着。 
# 
#  岛屿的面积是岛上值为 1 的单元格的数目。 
# 
#  计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,
# 0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,
# 0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 输出：6
# 解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[0,0,0,0,0,0,0,0]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 50 
#  grid[i][j] 为 0 或 1 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 780 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dfs(grid, x, y):
            # 遇到边界或者遇到0了，就停止
            if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]) or not grid[x][y]:
                return
            # 统计过这个点了，就把它标记成0，下次就不会重复过来了
            grid[x][y] = 0
            # 用一个变量存当前面积
            self.result += 1
            # 上下左右继续遍历
            dfs(grid, x, y + 1)
            dfs(grid, x - 1, y)
            dfs(grid, x, y - 1)
            dfs(grid, x + 1, y)
            # 全都找完了，输出最大面积
            return self.result

        maximum = 0
        # 找第一个陆地的开始
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # 每个岛单独统计
                    self.result = 0
                    # 保留最大值，此时找过的岛全被标注为0了
                    maximum = max(maximum, dfs(grid, i, j))
        return maximum
# leetcode submit region end(Prohibit modification and deletion)
