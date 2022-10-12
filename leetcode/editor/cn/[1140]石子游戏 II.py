# 爱丽丝和鲍勃继续他们的石子游戏。许多堆石子 排成一行，每堆都有正整数颗石子 piles[i]。游戏以谁手中的石子最多来决出胜负。 
# 
#  爱丽丝和鲍勃轮流进行，爱丽丝先开始。最初，M = 1。 
# 
#  在每个玩家的回合中，该玩家可以拿走剩下的 前 X 堆的所有石子，其中 1 <= X <= 2M。然后，令 M = max(M, X)。 
# 
#  游戏一直持续到所有石子都被拿走。 
# 
#  假设爱丽丝和鲍勃都发挥出最佳水平，返回爱丽丝可以得到的最大数量的石头。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：piles = [2,7,9,4,4]
# 输出：10
# 解释：如果一开始Alice取了一堆，Bob取了两堆，然后Alice再取两堆。爱丽丝可以得到2 + 4 + 4 = 10堆。如果Alice一开始拿走了两堆，那
# 么Bob可以拿走剩下的三堆。在这种情况下，Alice得到2 + 7 = 9堆。返回10，因为它更大。
#  
# 
#  示例 2: 
# 
#  
# 输入：piles = [1,2,3,4,5,100]
# 输出：104
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= piles.length <= 100 
#  1 <= piles[i] <= 10⁴ 
#  
#  Related Topics 数组 数学 动态规划 博弈 👍 131 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n, memo = len(piles), dict()

        # s[i] 表示第 i 堆石子到最后一堆石子的总石子数
        s = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            s[i] = s[i + 1] + piles[i]

        # dfs(i, M) 表示从第 i 堆石子开始取，最多能取 M 堆石子所能得到的最优值
        def dfs(i, M):
            # 如果已经搜索过，直接返回
            if (i, M) in memo:
                return memo[(i, M)]
            # 溢出拿不到任何石子
            if i >= n:
                return 0
            # 如果剩余堆数小于等于 2M， 那么可以全拿走
            if i + M * 2 >= n:
                return s[i]
            # 枚举拿 x 堆的最优值
            best = 0
            for x in range(1, M * 2 + 1):
                # 剩余石子减去对方最优策略
                best = max(best, s[i] - dfs(i + x, max(x, M)))
            # 记忆化
            memo[(i, M)] = best
            return best

        return dfs(0, 1)
# leetcode submit region end(Prohibit modification and deletion)
