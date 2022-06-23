# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充
# 。
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O",
# "X","X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都
# 会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["X"]]
# 输出：[["X"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 200 
#  board[i][j] 为 'X' 或 'O' 
#  
#  
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 782 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])

        def dfs(x, y):
            if board[x][y] != "O":
                return
            else:
                board[x][y] = "#"
            for c in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= x + c[0] < row and 0 <= y + c[1] < col:
                    dfs(x + c[0], y + c[1])

        for i in range(row):
            dfs(i, 0)
            dfs(i, col - 1)
        for j in range(1, col - 1):
            dfs(0, j)
            dfs(row - 1, j)
        for i in range(row):
            for j in range(col):
                board[i][j] = "O" if board[i][j] == "#" else "X"
# leetcode submit region end(Prohibit modification and deletion)
