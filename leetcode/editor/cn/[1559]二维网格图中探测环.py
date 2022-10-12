# 给你一个二维字符网格数组 grid ，大小为 m x n ，你需要检查 grid 中是否存在 相同值 形成的环。 
# 
#  一个环是一条开始和结束于同一个格子的长度 大于等于 4 的路径。对于一个给定的格子，你可以移动到它上、下、左、右四个方向相邻的格子之一，可以移动的前提是这
# 两个格子有 相同的值 。 
# 
#  同时，你也不能回到上一次移动时所在的格子。比方说，环 (1, 1) -> (1, 2) -> (1, 1) 是不合法的，因为从 (1, 2) 移动到 (1
# , 1) 回到了上一次移动时的格子。 
# 
#  如果 grid 中有相同值形成的环，请你返回 true ，否则返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a",
# "a","a"]]
# 输出：true
# 解释：如下图所示，有 2 个用不同颜色标出来的环：
# 
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c",
# "c","c"]]
# 输出：true
# 解释：如下图所示，只有高亮所示的一个合法环：
# 
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m <= 500 
#  1 <= n <= 500 
#  grid 只包含小写英文字母。 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 41 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.setCount = n
        self.parent = list(range(n))
        self.size = [1] * n

    def findset(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1

    def findAndUnite(self, x, y):
        parentX, parentY = self.findset(x), self.findset(y)
        if parentX != parentY:
            self.unite(parentX, parentY)
            return True
        return False


class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    if not uf.findAndUnite(i * n + j, (i - 1) * n + j):
                        return True
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    if not uf.findAndUnite(i * n + j, i * n + j - 1):
                        return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
