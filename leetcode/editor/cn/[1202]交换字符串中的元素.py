# 给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。 
# 
# 
#  你可以 任意多次交换 在 pairs 中任意一对索引处的字符。 
# 
#  返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。 
# 
#  
# 
#  示例 1: 
# 
#  输入：s = "dcab", pairs = [[0,3],[1,2]]
# 输出："bacd"
# 解释： 
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[1] 和 s[2], s = "bacd"
#  
# 
#  示例 2： 
# 
#  输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# 输出："abcd"
# 解释：
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[0] 和 s[2], s = "acbd"
# 交换 s[1] 和 s[2], s = "abcd" 
# 
#  示例 3： 
# 
#  输入：s = "cba", pairs = [[0,1],[1,2]]
# 输出："abc"
# 解释：
# 交换 s[0] 和 s[1], s = "bca"
# 交换 s[1] 和 s[2], s = "bac"
# 交换 s[0] 和 s[1], s = "abc"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10^5 
#  0 <= pairs.length <= 10^5 
#  0 <= pairs[i][0], pairs[i][1] < s.length 
#  s 中只含有小写英文字母 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 哈希表 字符串 👍 276 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def dfs(self, res, graph, visited, x):
        for neighbor in graph[x]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                res.append(neighbor)
                self.dfs(res, graph, visited, neighbor)

    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        # 建图
        graph = [[] for _ in range(len(s))]
        visited = [0] * len(s)
        for x, y in pairs:
            graph[x].append(y)
            graph[y].append(x)

        res = list(s)
        for i in range(len(s)):
            if not visited[i]:
                # 获取连通节点
                connected_nodes = []
                self.dfs(connected_nodes, graph, visited, i)
                # 重新赋值
                indices = sorted(connected_nodes)
                string = sorted(res[node] for node in connected_nodes)
                for j, ch in zip(indices, string):
                    res[j] = ch

        return "".join(res)
# leetcode submit region end(Prohibit modification and deletion)
