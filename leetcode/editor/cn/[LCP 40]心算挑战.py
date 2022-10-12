# 「力扣挑战赛」心算项目的挑战比赛中，要求选手从 `N` 张卡牌中选出 `cnt` 张卡牌，若这 `cnt` 张卡牌数字总和为偶数，则选手成绩「有效」且得分为
#  `cnt` 张卡牌数字总和。
# 给定数组 `cards` 和 `cnt`，其中 `cards[i]` 表示第 `i` 张卡牌上的数字。 请帮参赛选手计算最大的有效得分。若不存在获取有效得分
# 的卡牌方案，则返回 0。
# 
# **示例 1：**
# >输入：`cards = [1,2,8,9], cnt = 3`
# >
# >输出：`18`
# >
# >解释：选择数字为 1、8、9 的这三张卡牌，此时可获得最大的有效得分 1+8+9=18。
# 
# **示例 2：**
# >输入：`cards = [3,3,1], cnt = 1`
# >
# >输出：`0`
# >
# >解释：不存在获取有效得分的卡牌方案。
# 
# **提示：**
# - `1 <= cnt <= cards.length <= 10^5`
# - `1 <= cards[i] <= 1000`
# 
# 
#  Related Topics 贪心 数组 排序 👍 30 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import itertools


class Solution(object):
    def maxmiumScore(self, cards, cnt):
        """
        :type cards: List[int]
        :type cnt: int
        :rtype: int
        """
        c = sorted(cards, reverse=True)
        t = c[:cnt]
        s = sum(t)
        if s % 2 == 0:
            return s
        for i in range(cnt, len(c)):
            for j in range(cnt - 1, -1, -1):
                if c[i] % 2 != t[j] % 2:
                    return s - t[j] + c[i]
        return 0
# leetcode submit region end(Prohibit modification and deletion)
