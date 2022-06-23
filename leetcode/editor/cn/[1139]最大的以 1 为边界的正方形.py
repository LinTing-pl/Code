# 给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0
# 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：9
#  
# 
#  示例 2： 
# 
#  输入：grid = [[1,1,0,0]]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length <= 100 
#  1 <= grid[0].length <= 100 
#  grid[i][j] 为 0 或 1 
#  
#  Related Topics 数组 动态规划 矩阵 👍 92 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        # l表示点i,j左侧连续0的个数，u表示i,j上方连续0的个数
        l = [[0 for _ in range(n)] for _ in range(m)]
        u = [[0 for _ in range(n)] for _ in range(m)]
        maxLen = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                l[i][j], u[i][j] = 1, 1
                if i > 0:
                    u[i][j] += u[i - 1][j]
                if j > 0:
                    l[i][j] += l[i][j - 1]
                k = min(u[i][j], l[i][j])
                while (k > maxLen):
                    if u[i][j - k + 1] >= k and l[i - k + 1][j] >= k:
                        maxLen = k
                    else:
                        k -= 1
        return maxLen ** 2
# leetcode submit region end(Prohibit modification and deletion)
