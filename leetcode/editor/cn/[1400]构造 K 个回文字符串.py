# 给你一个字符串 s 和一个整数 k 。请你用 s 字符串中 所有字符 构造 k 个非空 回文串 。 
# 
#  如果你可以用 s 中所有字符构造 k 个回文字符串，那么请你返回 True ，否则返回 False 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "annabelle", k = 2
# 输出：true
# 解释：可以用 s 中所有字符构造 2 个回文字符串。
# 一些可行的构造方案包括："anna" + "elble"，"anbna" + "elle"，"anellena" + "b"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "leetcode", k = 3
# 输出：false
# 解释：无法用 s 中所有字符构造 3 个回文串。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "true", k = 4
# 输出：true
# 解释：唯一可行的方案是让 s 中每个字符单独构成一个字符串。
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "yzyzyzyzyzyzyzy", k = 2
# 输出：true
# 解释：你只需要将所有的 z 放在一个字符串中，所有的 y 放在另一个字符串中。那么两个字符串都是回文串。
#  
# 
#  示例 5： 
# 
#  
# 输入：s = "cr", k = 7
# 输出：false
# 解释：我们没有足够的字符去构造 7 个回文串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10^5 
#  s 中所有字符都是小写英文字母。 
#  1 <= k <= 10^5 
#  
#  Related Topics 贪心 哈希表 字符串 计数 👍 41 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # 右边界为字符串的长度
        right = len(s)
        # 统计每个字符出现的次数
        occ = collections.Counter(s)
        # 左边界为出现奇数次字符的个数
        left = sum(1 for _, v in occ.items() if v % 2 == 1)
        # 注意没有出现奇数次的字符的特殊情况
        left = max(left, 1)
        return left <= k <= right
# leetcode submit region end(Prohibit modification and deletion)
