# 给定两个单词 word1 和 word2 ，返回使得 word1 和 word2 相同所需的最小步数。 
# 
#  每步 可以删除任意一个字符串中的一个字符。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: word1 = "sea", word2 = "eat"
# 输出: 2
# 解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"
#  
# 
#  示例 2: 
# 
#  
# 输入：word1 = "leetcode", word2 = "etco"
# 输出：4
#  
# 
#  
# 
#  提示： 
#  
# 
#  
#  1 <= word1.length, word2.length <= 500 
#  word1 和 word2 只包含小写英文字母 
#  
#  Related Topics 字符串 动态规划 👍 423 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        lcs = dp[m][n]
        return m - lcs + n - lcs
# leetcode submit region end(Prohibit modification and deletion)
