# 有一只跳蚤的家在数轴上的位置 x 处。请你帮助它从位置 0 出发，到达它的家。 
# 
#  跳蚤跳跃的规则如下： 
# 
#  
#  它可以 往前 跳恰好 a 个位置（即往右跳）。 
#  它可以 往后 跳恰好 b 个位置（即往左跳）。 
#  它不能 连续 往后跳 2 次。 
#  它不能跳到任何 forbidden 数组中的位置。 
#  
# 
#  跳蚤可以往前跳 超过 它的家的位置，但是它 不能跳到负整数 的位置。 
# 
#  给你一个整数数组 forbidden ，其中 forbidden[i] 是跳蚤不能跳到的位置，同时给你整数 a， b 和 x ，请你返回跳蚤到家的最少跳跃
# 次数。如果没有恰好到达 x 的可行方案，请你返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
# 输出：3
# 解释：往前跳 3 次（0 -> 3 -> 6 -> 9），跳蚤就到家了。
#  
# 
#  示例 2： 
# 
#  
# 输入：forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
# 输出：-1
#  
# 
#  示例 3： 
# 
#  
# 输入：forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
# 输出：2
# 解释：往前跳一次（0 -> 16），然后往回跳一次（16 -> 7），跳蚤就到家了。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= forbidden.length <= 1000 
#  1 <= a, b, forbidden[i] <= 2000 
#  0 <= x <= 2000 
#  forbidden 中所有位置互不相同。 
#  位置 x 不在 forbidden 中。 
#  
#  Related Topics 广度优先搜索 数组 动态规划 👍 54 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        """
        :type forbidden: List[int]
        :type a: int
        :type b: int
        :type x: int
        :rtype: int
        """
        forbidden = set(forbidden)
        self.key = -1

        def dfs(num, cnt, back):
            if self.key < 0 and 0 <= num <= 6000:  # # 6000是往右探索的最大值，x最大为2000
                if num == x:  # 第一次遍历到 x时的次数即为结果，暂存结果，不再递归
                    self.key = cnt
                    return
                if num + a not in forbidden:
                    forbidden.add(num + a)  # 防止无限递归，比如 a = b 时，不加限制，就会出现无限递归
                    dfs(num + a, cnt + 1, 0)
                if num - b not in forbidden and back != 1:  # 若back为1说明上次就是往后跳的
                    dfs(num - b, cnt + 1, 1)

        dfs(0, 0, 0)
        return self.key
# leetcode submit region end(Prohibit modification and deletion)
