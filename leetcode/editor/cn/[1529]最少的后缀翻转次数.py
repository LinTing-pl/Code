# 给你一个长度为 n 、下标从 0 开始的二进制字符串 target 。你自己有另一个长度为 n 的二进制字符串 s ，最初每一位上都是 0 。你想要让 s 
# 和 target 相等。 
# 
#  在一步操作，你可以选择下标 i（0 <= i < n）并翻转在 闭区间 [i, n - 1] 内的所有位。翻转意味着 '0' 变为 '1' ，而 '1' 
# 变为 '0' 。 
# 
#  
#  
#  返回使 s 与 target 相等需要的最少翻转次数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：target = "10111"
# 输出：3
# 解释：最初，s = "00000" 。
# 选择下标 i = 2: "00000" -> "00111"
# 选择下标 i = 0: "00111" -> "11000"
# 选择下标 i = 1: "11000" -> "10111"
# 要达成目标，需要至少 3 次翻转。
#  
# 
#  示例 2： 
# 
#  
# 输入：target = "101"
# 输出：3
# 解释：最初，s = "000" 。
# 选择下标 i = 0: "000" -> "111"
# 选择下标 i = 1: "111" -> "100"
# 选择下标 i = 2: "100" -> "101"
# 要达成目标，需要至少 3 次翻转。
#  
# 
#  示例 3： 
# 
#  
# 输入：target = "00000"
# 输出：0
# 解释：由于 s 已经等于目标，所以不需要任何操作
#  
#  
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == target.length 
#  1 <= n <= 10⁵ 
#  target[i] 为 '0' 或 '1' 
#  
#  Related Topics 贪心 字符串 👍 43 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        flips, prev = 0, "0"
        for curr in target:
            if curr != prev:
                flips += 1
                prev = curr
        return flips
# leetcode submit region end(Prohibit modification and deletion)
