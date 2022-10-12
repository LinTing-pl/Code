# 给你一维空间的 n 个点，其中第 i 个点（编号从 0 到 n-1）位于 x = i 处，请你找到 恰好 k 个不重叠 线段且每个线段至少覆盖两个点的方案数
# 。线段的两个端点必须都是 整数坐标 。这 k 个线段不需要全部覆盖全部 n 个点，且它们的端点 可以 重合。 
# 
#  请你返回 k 个不重叠线段的方案数。由于答案可能很大，请将结果对 10⁹ + 7 取余 后返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4, k = 2
# 输出：5
# 解释：
# 如图所示，两个线段分别用红色和蓝色标出。
# 上图展示了 5 种不同的方案 {(0,2),(2,3)}，{(0,1),(1,3)}，{(0,1),(2,3)}，{(1,2),(2,3)}，{(0,1),
# (1,2)} 。 
# 
#  示例 2： 
# 
#  
# 输入：n = 3, k = 1
# 输出：3
# 解释：总共有 3 种不同的方案 {(0,1)}, {(0,2)}, {(1,2)} 。
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 30, k = 7
# 输出：796297179
# 解释：画 7 条线段的总方案数为 3796297200 种。将这个数对 10⁹ + 7 取余得到 796297179 。
#  
# 
#  示例 4： 
# 
#  
# 输入：n = 5, k = 3
# 输出：7
#  
# 
#  示例 5： 
# 
#  
# 输入：n = 3, k = 2
# 输出：1 
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 1000 
#  1 <= k <= n-1 
#  
#  Related Topics 数学 动态规划 👍 47 👎 0


# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # k个不重叠线段至少需要k+1个点
        # 将相邻点之间的距离看做1，则n个点，可以看成n-1条长度为1的初始线段，需要挑出来部分初始线段，组成k个线段，组成的线段长度至少为1
        # dp[i][j]表示1———i个初始线段（i<=n-1），组成 j个线段的方案数 j从1开始 最终返回dp[n-1][k]即可
        # i==j时，dp[i][j]=1 i<j时 dp[i][j]=0
        # dp[i][j]=dp[i-1][j]+dp[i-1][j-1]+dp[i-2][j-1]+...+dp[j-1][j-1]
        # 例如 dp[2][1]=dp[1][1]+dp[1][0]+dp[0][0]
        # 意为：1 2这两个初始线段，组成1个线段的方案数，dp[1][1]对应的是只使用1这个线段，dp[1][0]对应的是，只使用2这个线段，dp[0][0]对应的是将1和2拼成一个线段的情况
        '''
        dp=[[1 for col in range(k+1)] for row in range(n)]
        for i in range(1,n):
            for j in range(1,min(i,k+1)):
                dp[i][j]=dp[i-1][j]
                for l in range(i-1,j-2,-1):
                    dp[i][j]+=dp[l][j-1]
        return dp[n-1][k]%(10**9+7)
        '''
        # 上述时间复杂度为O(n^3),导致部分测试用例超时
        # 优化 可用sumdp[i][j]记录dp[i][j]+dp[i-1][j]+...+dp[j][j] 转移方程 sumdp[i][j]=sumdp[i-1][j]+dp[i][j]
        dp = [[1 for col in range(k + 1)] for row in range(n)]
        sumdp = [[1 for col in range(k + 1)] for row in range(n)]
        for i in range(1, n):
            sumdp[i][0] = sumdp[i - 1][0] + 1
            for j in range(1, min(i, k + 1)):
                dp[i][j] = dp[i - 1][j] + sumdp[i - 1][j - 1]
                sumdp[i][j] = sumdp[i - 1][j] + dp[i][j]
        return dp[n - 1][k] % (10 ** 9 + 7)
# leetcode submit region end(Prohibit modification and deletion)
