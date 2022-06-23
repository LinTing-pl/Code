# 如果一个二进制字符串，是以一些 0（可能没有 0）后面跟着一些 1（也可能没有 1）的形式组成的，那么该字符串是 单调递增 的。 
# 
#  给你一个二进制字符串 s，你可以将任何 0 翻转为 1 或者将 1 翻转为 0 。 
# 
#  返回使 s 单调递增的最小翻转次数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "00110"
# 输出：1
# 解释：翻转最后一位得到 00111.
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "010110"
# 输出：2
# 解释：翻转得到 011111，或者是 000111。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "00011000"
# 输出：2
# 解释：翻转得到 00000000。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] 为 '0' 或 '1' 
#  
#  Related Topics 字符串 动态规划 👍 158 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        P = [0]
        for x in s:
            P.append(P[-1] + int(x))

        return min(P[j] + len(s) - j - (P[-1] - P[j])
                   for j in range(len(P)))
# leetcode submit region end(Prohibit modification and deletion)
