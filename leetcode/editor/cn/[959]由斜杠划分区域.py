# 在由 1 x 1 方格组成的 n x n 网格 grid 中，每个 1 x 1 方块由 '/'、'\' 或空格构成。这些字符会将方块划分为一些共边的区域。 
# 
# 
#  给定网格 grid 表示为一个字符串数组，返回 区域的数量 。 
# 
#  请注意，反斜杠字符是转义的，因此 '\' 用 '\\' 表示。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：grid = [" /","/ "]
# 输出：2 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：grid = [" /","  "]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：grid = ["/\\","\\/"]
# 输出：5
# 解释：回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == grid.length == grid[i].length 
#  1 <= n <= 30 
#  grid[i][j] 是 '/'、'\'、或 ' ' 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 图 👍 306 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class UF:
    def __init__(self, M):
        self.parent = {}
        self.cnt = 0
        # 初始化 parent，size 和 cnt
        for i in range(M):
            self.parent[i] = i
            self.cnt += 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return x

    def union(self, p, q):
        if self.connected(p, q): return
        leader_p = self.find(p)
        leader_q = self.find(q)
        self.parent[leader_p] = leader_q
        self.cnt -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        N = n * n * 4
        uf = UF(N)

        def get_pos(row, col, i):
            return (row * n + col) * 4 + i

        for row in range(n):
            for col in range(n):
                v = grid[row][col]
                if row > 0:
                    uf.union(get_pos(row - 1, col, 2), get_pos(row, col, 1))
                if col > 0:
                    uf.union(get_pos(row, col - 1, 3), get_pos(row, col, 0))
                if v == '/':
                    uf.union(get_pos(row, col, 0), get_pos(row, col, 1))
                    uf.union(get_pos(row, col, 2), get_pos(row, col, 3))
                if v == '\\':
                    uf.union(get_pos(row, col, 1), get_pos(row, col, 3))
                    uf.union(get_pos(row, col, 0), get_pos(row, col, 2))
                if v == ' ':
                    uf.union(get_pos(row, col, 0), get_pos(row, col, 1))
                    uf.union(get_pos(row, col, 1), get_pos(row, col, 2))
                    uf.union(get_pos(row, col, 2), get_pos(row, col, 3))

        return uf.cnt
# leetcode submit region end(Prohibit modification and deletion)
