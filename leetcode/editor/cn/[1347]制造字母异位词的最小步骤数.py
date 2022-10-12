# 给你两个长度相等的字符串 s 和 t。每一个步骤中，你可以选择将 t 中的 任一字符 替换为 另一个字符。 
# 
#  返回使 t 成为 s 的字母异位词的最小步骤数。 
# 
#  字母异位词 指字母相同，但排列不同（也可能相同）的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  输出：s = "bab", t = "aba"
# 输出：1
# 提示：用 'b' 替换 t 中的第一个 'a'，t = "bba" 是 s 的一个字母异位词。
#  
# 
#  示例 2： 
# 
#  输出：s = "leetcode", t = "practice"
# 输出：5
# 提示：用合适的字符替换 t 中的 'p', 'r', 'a', 'i' 和 'c'，使 t 变成 s 的字母异位词。
#  
# 
#  示例 3： 
# 
#  输出：s = "anagram", t = "mangaar"
# 输出：0
# 提示："anagram" 和 "mangaar" 本身就是一组字母异位词。 
#  
# 
#  示例 4： 
# 
#  输出：s = "xxyyzz", t = "xxyyzz"
# 输出：0
#  
# 
#  示例 5： 
# 
#  输出：s = "friend", t = "family"
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 50000 
#  s.length == t.length 
#  s 和 t 只包含小写英文字母 
#  
#  Related Topics 哈希表 字符串 计数 👍 36 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_cnt = collections.Counter(s)
        t_cnt = collections.Counter(t)
        ans = 0
        for c in set(s_cnt.keys()).union(set(t_cnt.keys())):
            if s_cnt[c] < t_cnt[c]:
                ans += t_cnt[c] - s_cnt[c]
        return ans
# leetcode submit region end(Prohibit modification and deletion)
