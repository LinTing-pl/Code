# 给你一个字符串 s，找到 s 中最长的回文子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "a"
# 输出："a"
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "ac"
# 输出："a"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母（大写和/或小写）组成 
#  
#  Related Topics 字符串 动态规划 👍 4505 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        s_length = len(s)
        for i in range(s_length):
            for j in range(s_length, i, -1):
                string = self.ishuiwen(s[i:j])
                if string:
                    if len(string) > s_length / 2:
                        return string
                    result.append(string)
        result.sort(reverse=True, key=len)
        return result[0]

    def ishuiwen(self, l):
        r = l[::-1]
        if l == r:
            return l

# leetcode submit region end(Prohibit modification and deletion)
