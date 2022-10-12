# Alice 把 n 个气球排列在一根绳子上。给你一个下标从 0 开始的字符串 colors ，其中 colors[i] 是第 i 个气球的颜色。 
# 
#  Alice 想要把绳子装扮成 彩色 ，且她不希望两个连续的气球涂着相同的颜色，所以她喊来 Bob 帮忙。Bob 可以从绳子上移除一些气球使绳子变成 彩色 
# 。给你一个下标从 0 开始的整数数组 neededTime ，其中 neededTime[i] 是 Bob 从绳子上移除第 i 个气球需要的时间（以秒为单位）。
#  
# 
#  返回 Bob 使绳子变成 彩色 需要的 最少时间 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：colors = "abaac", neededTime = [1,2,3,4,5]
# 输出：3
# 解释：在上图中，'a' 是蓝色，'b' 是红色且 'c' 是绿色。
# Bob 可以移除下标 2 的蓝色气球。这将花费 3 秒。
# 移除后，不存在两个连续的气球涂着相同的颜色。总时间 = 3 。 
# 
#  示例 2： 
# 
#  
# 输入：colors = "abc", neededTime = [1,2,3]
# 输出：0
# 解释：绳子已经是彩色的，Bob 不需要从绳子上移除任何气球。
#  
# 
#  示例 3： 
# 
#  
# 输入：colors = "aabaa", neededTime = [1,2,3,4,1]
# 输出：2
# 解释：Bob 会移除下标 0 和下标 4 处的气球。这两个气球各需要 1 秒来移除。
# 移除后，不存在两个连续的气球涂着相同的颜色。总时间 = 1 + 1 = 2 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == colors.length == neededTime.length 
#  1 <= n <= 10⁵ 
#  1 <= neededTime[i] <= 10⁴ 
#  colors 仅由小写英文字母组成 
#  
#  Related Topics 贪心 数组 字符串 动态规划 👍 56 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        i = 0
        length = len(colors)
        ret = 0

        while i < length:
            ch = colors[i]
            maxValue = 0
            total = 0

            while i < length and colors[i] == ch:
                maxValue = max(maxValue, neededTime[i])
                total += neededTime[i]
                i += 1

            ret += total - maxValue

        return ret
# leetcode submit region end(Prohibit modification and deletion)
