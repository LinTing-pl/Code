# 给你一个 m x n 的网格 grid。网格里的每个单元都代表一条街道。grid[i][j] 的街道可以是： 
# 
#  
#  1 表示连接左单元格和右单元格的街道。 
#  2 表示连接上单元格和下单元格的街道。 
#  3 表示连接左单元格和下单元格的街道。 
#  4 表示连接右单元格和下单元格的街道。 
#  5 表示连接左单元格和上单元格的街道。 
#  6 表示连接右单元格和上单元格的街道。 
#  
# 
#  
# 
#  你最开始从左上角的单元格 (0,0) 开始出发，网格中的「有效路径」是指从左上方的单元格 (0,0) 开始、一直到右下方的 (m-1,n-1) 结束的路径
# 。该路径必须只沿着街道走。 
# 
#  注意：你 不能 变更街道。 
# 
#  如果网格中存在有效的路径，则返回 true，否则返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：grid = [[2,4,3],[6,5,2]]
# 输出：true
# 解释：如图所示，你可以从 (0, 0) 开始，访问网格中的所有单元格并到达 (m - 1, n - 1) 。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：grid = [[1,2,1],[1,2,1]]
# 输出：false
# 解释：如图所示，单元格 (0, 0) 上的街道没有与任何其他单元格上的街道相连，你只会停在 (0, 0) 处。
#  
# 
#  示例 3： 
# 
#  输入：grid = [[1,1,2]]
# 输出：false
# 解释：你会停在 (0, 1)，而且无法到达 (0, 2) 。
#  
# 
#  示例 4： 
# 
#  输入：grid = [[1,1,1,1,1,1,3]]
# 输出：true
#  
# 
#  示例 5： 
# 
#  输入：grid = [[2],[2],[2],[2],[2],[2],[6]]
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  1 <= grid[i][j] <= 6 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 57 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """

        def sub2ind(i, j):
            return i * n + j

        m, n = len(grid), len(grid[0])
        uf = FindUnion(m * n)
        for i in range(m):
            for j in range(n):
                e = grid[i][j]
                if e in [1, 3, 5]:
                    # left
                    if j - 1 >= 0 and grid[i][j - 1] in [1, 4, 6]:
                        uf.unite(sub2ind(i, j), sub2ind(i, j - 1))
                if e in [2, 5, 6]:
                    # up
                    if i - 1 >= 0 and grid[i - 1][j] in [2, 3, 4]:
                        uf.unite(sub2ind(i, j), sub2ind(i - 1, j))
        return uf.find(sub2ind(m - 1, n - 1)) == 0


class FindUnion:
    def __init__(self, n):
        self.fa = list(range(n))

    def find(self, i):
        if self.fa[i] == i:
            return i
        self.fa[i] = self.find(self.fa[i])
        return self.fa[i]

    def unite(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if i == j:
            return
        if i < j:
            self.fa[j] = i
        else:
            self.fa[i] = j

# leetcode submit region end(Prohibit modification and deletion)
