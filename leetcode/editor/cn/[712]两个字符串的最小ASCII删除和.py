# 给定两个字符串s1 和 s2，返回 使两个字符串相等所需删除字符的 ASCII 值的最小和 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s1 = "sea", s2 = "eat"
# 输出: 231
# 解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
# 在 "eat" 中删除 "t" 并将 116 加入总和。
# 结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
#  
# 
#  示例 2: 
# 
#  
# 输入: s1 = "delete", s2 = "leet"
# 输出: 403
# 解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
# 将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
# 结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
# 如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
#  
# 
#  
# 
#  提示: 
# 
#  
#  0 <= s1.length, s2.length <= 1000 
#  s1 和 s2 由小写英文字母组成 
#  
#  Related Topics 字符串 动态规划 👍 273 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        # 转化为最长公共子序列(lcs)问题，用总的ascii值减去相同的值即可
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 分为两种情况，s1的第i个元素和s2的第j个元素相等和不相等
        for i, ch1 in enumerate(s1):
            for j, ch2 in enumerate(s2):
                if ch1 == ch2:
                    dp[i + 1][j + 1] = dp[i][j] + ord(ch1)
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        # 分别得到两个的ascii值
        ord1, ord2 = 0, 0
        for ch in s1:
            ord1 += ord(ch)
        for ch in s2:
            ord2 += ord(ch)
        return ord1 + ord2 - 2 * dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
