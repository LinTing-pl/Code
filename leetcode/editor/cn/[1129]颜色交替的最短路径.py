# 在一个有向图中，节点分别标记为 0, 1, ..., n-1。图中每条边为红色或者蓝色，且存在自环或平行边。 
# 
#  red_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的红色有向边。类似地，blue_edges 中的每一个 [i, j] 对表示从
# 节点 i 到节点 j 的蓝色有向边。 
# 
#  返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，
# 那么 answer[x] = -1。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
# 输出：[0,1,-1]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
# 输出：[0,1,-1]
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
# 输出：[0,-1,-1]
#  
# 
#  示例 4： 
# 
#  
# 输入：n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
# 输出：[0,1,2]
#  
# 
#  示例 5： 
# 
#  
# 输入：n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
# 输出：[0,1,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 100 
#  red_edges.length <= 400 
#  blue_edges.length <= 400 
#  red_edges[i].length == blue_edges[i].length == 2 
#  0 <= red_edges[i][j], blue_edges[i][j] < n 
#  
#  Related Topics 广度优先搜索 图 👍 103 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        rg = defaultdict(list)
        for src, dest in redEdges:
            rg[src].append(dest)

        bg = defaultdict(list)
        for src, dest in blueEdges:
            bg[src].append(dest)

        ans = [float('inf')] * n

        def bfs():
            queue = deque([(0, True, 0), (0, False, 0)])
            while queue:
                node, flag, step = queue.popleft()
                ans[node] = min(ans[node], step)
                v = bv if flag else rv
                v[node] = True

                g = rg if flag else bg
                v = rv if flag else bv
                for nei in g[node]:
                    if v[nei]:
                        continue
                    queue.append((nei, not flag, step + 1))

        bv = [False] * n
        rv = [False] * n
        bfs()

        ans = [x if x != float('inf') else -1 for x in ans]
        return ans
# leetcode submit region end(Prohibit modification and deletion)
