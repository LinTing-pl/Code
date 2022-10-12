# 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 
# values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。 
# 
#  另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj =
#  ? 的结果作为答案。 
# 
#  返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替
# 代这个答案。 
# 
#  注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"]
# ,["b","a"],["a","e"],["a","a"],["x","x"]]
# 输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
# 解释：
# 条件：a / b = 2.0, b / c = 3.0
# 问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# 结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
#  
# 
#  示例 2： 
# 
#  
# 输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], 
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# 输出：[3.75000,0.40000,5.00000,0.20000]
#  
# 
#  示例 3： 
# 
#  
# 输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],[
# "a","c"],["x","y"]]
# 输出：[0.50000,2.00000,-1.00000,-1.00000]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= equations.length <= 20 
#  equations[i].length == 2 
#  1 <= Ai.length, Bi.length <= 5 
#  values.length == equations.length 
#  0.0 < values[i] <= 20.0 
#  1 <= queries.length <= 20 
#  queries[i].length == 2 
#  1 <= Cj.length, Dj.length <= 5 
#  Ai, Bi, Cj, Dj 由小写英文字母与数字组成 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 图 数组 最短路 👍 739 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind(object):
    def __init__(self):
        self.father = {}
        self.value = {}

    def find(self, x):
        root = x
        base = 1
        while self.father[root] is not None:
            root = self.father[root]
            base *= self.value[root]
        while x != root:
            original_father = self.father[x]
            self.value[x] *= base
            base /= self.value[original_father]
            self.father[x] = root
            x = original_father
        return root

    def merge(self, x, y, val):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.value[root_x] = self.value[y] * val / self.value[x]

    def is_connected(self, x, y):
        return x in self.value and y in self.value and self.find(x) == self.find(y)

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.value[x] = 1.0


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        uf = UnionFind()
        for (a, b), val in zip(equations, values):
            uf.add(a)
            uf.add(b)
            uf.merge(a, b, val)
        res = [-1.0] * len(queries)
        for i, (a, b) in enumerate(queries):
            if uf.is_connected(a, b):
                res[i] = uf.value[a] / uf.value[b]
        return res

# leetcode submit region end(Prohibit modification and deletion)
