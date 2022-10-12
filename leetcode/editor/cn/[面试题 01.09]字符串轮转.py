# 字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。 
# 
#  示例1: 
# 
#   输入：s1 = "waterbottle", s2 = "erbottlewat"
#  输出：True
#  
# 
#  示例2: 
# 
#   输入：s1 = "aa", s2 = "aba"
#  输出：False
#  
# 
#  
#  
# 
#  提示： 
# 
#  
#  字符串长度在[0, 100000]范围内。 
#  
# 
#  说明: 
# 
#  
#  你能只调用一次检查子串的方法吗？ 
#  
#  Related Topics 字符串 字符串匹配 👍 113 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isFlipedString(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2: return True
        for i in range(len(s1)):
            if s1[i:] + s1[:i] == s2:
                return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
