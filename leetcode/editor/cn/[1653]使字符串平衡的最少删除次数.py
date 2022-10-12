# 给你一个字符串 s ，它仅包含字符 'a' 和 'b' 。 
# 
#  你可以删除 s 中任意数目的字符，使得 s 平衡 。我们称 s 平衡的 当不存在下标对 (i,j) 满足 i < j 且 s[i] = 'b' 同时 s[
# j]= 'a' 。 
# 
#  请你返回使 s 平衡 的 最少 删除次数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aababbab"
# 输出：2
# 解释：你可以选择以下任意一种方案：
# 下标从 0 开始，删除第 2 和第 6 个字符（"aababbab" -> "aaabbb"），
# 下标从 0 开始，删除第 3 和第 6 个字符（"aababbab" -> "aabbbb"）。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "bbaaaaabb"
# 输出：2
# 解释：唯一的最优解是删除最前面两个字符。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] 要么是 'a' 要么是 'b' 。 
#  
#  Related Topics 栈 字符串 动态规划 👍 30 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = [0] * (n + 1)
        for i, c in enumerate(s):
            if c == 'a':
                count[i + 1] = count[i] + 1
            else:
                count[i + 1] = count[i]
        ans = float("inf")
        for i in range(n):
            # 到i有多少个'b'，后面有多少个'a'
            b = i - count[i]
            a = count[-1] - count[i + 1]
            if not a and not b:
                return 0
            ans = min(ans, b + a)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
