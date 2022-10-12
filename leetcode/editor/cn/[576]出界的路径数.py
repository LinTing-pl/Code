# 给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。你可以将球移到在四个方向上相邻的单元格内（可以
# 穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。 
# 
#  给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对 
# 10⁹ + 7 取余 后的结果。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# 输出：6
#  
# 
#  示例 2： 
# 
#  
# 输入：m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# 输出：12
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= m, n <= 50 
#  0 <= maxMove <= 50 
#  0 <= startRow < m 
#  0 <= startColumn < n 
#  
#  Related Topics 动态规划 👍 241 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        outCounts = 0
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        dp[0][startRow][startColumn] = 1
        for i in range(maxMove):
            for j in range(m):
                for k in range(n):
                    if dp[i][j][k] > 0:
                        for j1, k1 in [(j - 1, k), (j + 1, k), (j, k - 1), (j, k + 1)]:
                            if 0 <= j1 < m and 0 <= k1 < n:
                                dp[i + 1][j1][k1] = (dp[i + 1][j1][k1] + dp[i][j][k]) % MOD
                            else:
                                outCounts = (outCounts + dp[i][j][k]) % MOD

        return outCounts
# leetcode submit region end(Prohibit modification and deletion)
