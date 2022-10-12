# 你将得到一个整数数组 matchsticks ，其中 matchsticks[i] 是第 i 个火柴棒的长度。你要用 所有的火柴棍 拼成一个正方形。你 不能
# 折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。 
# 
#  如果你能使这个正方形，则返回 true ，否则返回 false 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: matchsticks = [1,1,2,2,2]
# 输出: true
# 解释: 能拼成一个边长为2的正方形，每边两根火柴。
#  
# 
#  示例 2: 
# 
#  
# 输入: matchsticks = [3,3,3,3,4]
# 输出: false
# 解释: 不能用所有火柴拼成一个正方形。
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= matchsticks.length <= 15 
#  1 <= matchsticks[i] <= 10⁸ 
#  
#  Related Topics 位运算 数组 动态规划 回溯 状态压缩 👍 264 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        # ------------------------排除特殊情况------------------------------
        # 长度小于4
        if len(matchsticks) < 4:
            return False
        # 除4有余数
        if sum(matchsticks) % 4:
            return False
        # 正方形边长
        s = sum(matchsticks) / 4
        matchsticks.sort()
        # 最大值大于边长
        if matchsticks[-1] > s:
            return False

        # -----------------------回溯--------------------------------
        def dfs(path, l):
            if not l:
                return path[0] == path[1] == path[2] == path[3]
            # 从大到小插入可以快速排除失败情况，减少计算量
            # 当前元素加入任何一条边能成功，则返回True
            if path[0] + l[-1] <= s and dfs([path[0] + l[-1]] + path[1:], l[:-1]):
                return True
            if path[1] + l[-1] <= s and dfs(path[:1] + [path[1] + l[-1]] + path[2:], l[:-1]):
                return True
            if path[2] + l[-1] <= s and dfs(path[:2] + [path[2] + l[-1]] + path[3:], l[:-1]):
                return True
            if path[3] + l[-1] <= s and dfs(path[:3] + [path[3] + l[-1]], l[:-1]):
                return True
            return False

        # 正方形四条边
        path = [0, 0, 0, 0]
        return dfs(path, matchsticks)

# leetcode submit region end(Prohibit modification and deletion)
