# 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aaabb", k = 3
# 输出：3
# 解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "ababbc", k = 2
# 输出：5
# 解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 仅由小写英文字母组成 
#  1 <= k <= 10⁵ 
#  
#  Related Topics 哈希表 字符串 分治 滑动窗口 👍 682 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
import re


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k: return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c) if t)
        return len(s)

# leetcode submit region end(Prohibit modification and deletion)
