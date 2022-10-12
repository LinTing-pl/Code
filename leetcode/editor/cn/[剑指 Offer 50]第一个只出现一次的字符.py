# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。 
# 
#  示例 1: 
# 
#  
# 输入：s = "abaccdeff"
# 输出：'b'
#  
# 
#  示例 2: 
# 
#  
# 输入：s = "" 
# 输出：' '
#  
# 
#  
# 
#  限制： 
# 
#  0 <= s 的长度 <= 50000 
#  Related Topics 队列 哈希表 字符串 计数 👍 208 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in s:
            if s.count(i) == 1:
                return i
        return " "
# leetcode submit region end(Prohibit modification and deletion)
