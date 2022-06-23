# 编写一个程序，通过填充空格来解决数独问题。 
# 
#  数独的解法需 遵循如下规则： 
# 
#  
#  数字 1-9 在每一行只能出现一次。 
#  数字 1-9 在每一列只能出现一次。 
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图） 
#  
# 
#  数独部分空格内已填入了数字，空白格用 '.' 表示。 
# 
#  
# 
#  
#  
#  
#  示例： 
# 
#  
# 输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".
# ",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".
# ","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6
# "],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[
# ".",".",".",".","8",".",".","7","9"]]
# 输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8
# "],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],[
# "4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9",
# "6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4",
# "5","2","8","6","1","7","9"]]
# 解释：输入的数独如上图所示，唯一有效的解决方案如下所示：
# 
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  board.length == 9 
#  board[i].length == 9 
#  board[i][j] 是一位数字或者 '.' 
#  题目数据 保证 输入数独仅有一个解 
#  
#  
#  
#  
#  Related Topics 数组 回溯 矩阵 👍 1135 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def dfs(pos):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            i, j = spaces[pos]
            for digit in range(9):
                if row[i][digit] == col[j][digit] == sqrt[i // 3][j // 3][digit] == False:
                    row[i][digit] = col[j][digit] = sqrt[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    row[i][digit] = col[j][digit] = sqrt[i // 3][j // 3][digit] = False
                if valid:
                    return

        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        sqrt = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        valid = False
        spaces = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    row[i][digit] = col[j][digit] = sqrt[i // 3][j // 3][digit] = True
        dfs(0)
# leetcode submit region end(Prohibit modification and deletion)
