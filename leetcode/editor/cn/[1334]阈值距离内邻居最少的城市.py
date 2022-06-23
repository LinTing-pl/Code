# 有 n 个城市，按从 0 到 n-1 编号。给你一个边数组 edges，其中 edges[i] = [fromi, toi, weighti] 代表 
# fromi 和 toi 两个城市之间的双向加权边，距离阈值是一个整数 distanceThreshold。 
# 
#  返回能通过某些路径到达其他城市数目最少、且路径距离 最大 为 distanceThreshold 的城市。如果有多个这样的城市，则返回编号最大的城市。 
# 
#  注意，连接城市 i 和 j 的路径的距离等于沿该路径的所有边的权重之和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
# 输出：3
# 解释：城市分布图如上。
# 每个城市阈值距离 distanceThreshold = 4 内的邻居城市分别是：
# 城市 0 -> [城市 1, 城市 2] 
# 城市 1 -> [城市 0, 城市 2, 城市 3] 
# 城市 2 -> [城市 0, 城市 1, 城市 3] 
# 城市 3 -> [城市 1, 城市 2] 
# 城市 0 和 3 在阈值距离 4 以内都有 2 个邻居城市，但是我们必须返回城市 3，因为它的编号最大。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 
# distanceThreshold = 2
# 输出：0
# 解释：城市分布图如上。 
# 每个城市阈值距离 distanceThreshold = 2 内的邻居城市分别是：
# 城市 0 -> [城市 1] 
# 城市 1 -> [城市 0, 城市 4] 
# 城市 2 -> [城市 3, 城市 4] 
# 城市 3 -> [城市 2, 城市 4]
# 城市 4 -> [城市 1, 城市 2, 城市 3] 
# 城市 0 在阈值距离 2 以内只有 1 个邻居城市。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 100 
#  1 <= edges.length <= n * (n - 1) / 2 
#  edges[i].length == 3 
#  0 <= fromi < toi < n 
#  1 <= weighti, distanceThreshold <= 10^4 
#  所有 (fromi, toi) 都是不同的。 
#  
#  Related Topics 图 动态规划 最短路 👍 78 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        dis = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n): dis[i][i] = 0
        for i, j, w in edges:
            dis[i][j] = w
            dis[j][i] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        res, count = 0, n + 1
        for i in range(n):
            cur = 0
            for j in range(n):
                if dis[i][j] <= distanceThreshold:
                    cur += 1
            if cur <= count:
                res, count = i, cur
        return res
# leetcode submit region end(Prohibit modification and deletion)
