# 给定两个字符串 s 和 t ，它们只包含小写字母。 
# 
#  字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。 
# 
#  请找出在 t 中被添加的字母。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abcd", t = "abcde"
# 输出："e"
# 解释：'e' 是那个被添加的字母。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "", t = "y"
# 输出："y"
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 1000 
#  t.length == s.length + 1 
#  s 和 t 只包含小写字母 
#  
#  Related Topics 位运算 哈希表 字符串 排序 👍 304 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hsr = collections.Counter(t) - collections.Counter(s)
        return hsr.keys()[0]
# leetcode submit region end(Prohibit modification and deletion)
