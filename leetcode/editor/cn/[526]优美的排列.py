# 假设有从 1 到 n 的 n 个整数。用这些整数构造一个数组 perm（下标从 1 开始），只要满足下述条件 之一 ，该数组就是一个 优美的排列 ： 
# 
#  
#  perm[i] 能够被 i 整除 
#  i 能够被 perm[i] 整除 
#  
# 
#  给你一个整数 n ，返回可以构造的 优美排列 的 数量 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 2
# 输出：2
# 解释：
# 第 1 个优美的排列是 [1,2]：
#     - perm[1] = 1 能被 i = 1 整除
#     - perm[2] = 2 能被 i = 2 整除
# 第 2 个优美的排列是 [2,1]:
#     - perm[1] = 2 能被 i = 1 整除
#     - i = 2 能被 perm[2] = 1 整除
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 15 
#  
#  Related Topics 位运算 数组 动态规划 回溯 状态压缩 👍 293 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution(object):
    res = 0

    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dfs(n, [], 1)
        return self.res

    def dfs(self, n, path, index):
        if len(path) == n:
            self.res += 1
        for i in range(1, n + 1):
            if i in path:
                continue
            if i % index == 0 or index % i == 0:
                path.append(i)
                self.dfs(n, path, index + 1)
                path.pop()
# leetcode submit region end(Prohibit modification and deletion)
