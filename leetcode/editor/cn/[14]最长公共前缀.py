# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#  
# 
#  示例 2： 
# 
#  
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] 仅由小写英文字母组成 
#  
#  Related Topics 字符串 👍 2045 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def s(self, str1, str2):
        str = ""
        length = min(len(str1), len(str2))
        for i in range(length):
            if str1[i] == str2[i]:
                str += str1[i]
            else:
                break
        return str

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        s = strs[0]
        for i in range(1, len(strs)):
            s = self.s(s, strs[i])
        return s

# leetcode submit region end(Prohibit modification and deletion)
