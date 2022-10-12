# 给定一个包含大写字母和小写字母的字符串 s ，返回 通过这些字母构造成的 最长的回文串 。 
# 
#  在构造过程中，请注意 区分大小写 。比如 "Aa" 不能当做一个回文字符串。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入:s = "abccccdd"
# 输出:7
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
#  
# 
#  示例 2: 
# 
#  
# 输入:s = "a"
# 输入:1
#  
# 
#  示例 3: 
# 
#  
# 输入:s = "bb"
# 输入: 2
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length <= 2000 
#  s 只能由小写和/或大写英文字母组成 
#  
#  Related Topics 贪心 哈希表 字符串 👍 387 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        count = collections.Counter(s)
        for i in count.values():
            ans += i // 2 * 2
            if ans % 2 == 0 and i % 2 == 1:
                ans += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
