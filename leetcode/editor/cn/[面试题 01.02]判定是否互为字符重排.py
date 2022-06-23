# 给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。 
# 
#  示例 1： 
# 
#  输入: s1 = "abc", s2 = "bca"
# 输出: true 
#  
# 
#  示例 2： 
# 
#  输入: s1 = "abc", s2 = "bad"
# 输出: false
#  
# 
#  说明： 
# 
#  
#  0 <= len(s1) <= 100 
#  0 <= len(s2) <= 100 
#  
#  Related Topics 哈希表 字符串 排序 👍 67 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def CheckPermutation(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return sorted(s1) == sorted(s2)
# leetcode submit region end(Prohibit modification and deletion)
