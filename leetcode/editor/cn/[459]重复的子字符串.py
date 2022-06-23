# 给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abab"
# 输出: true
# 解释: 可由子串 "ab" 重复两次构成。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "aba"
# 输出: false
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "abcabcabcabc"
# 输出: true
# 解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)
#  
# 
#  
# 
#  提示： 
# 
#  
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 由小写英文字母组成 
#  
#  Related Topics 字符串 字符串匹配 👍 630 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        zilen = 1
        while zilen < len(s) // 2 + 1:
            if len(s) % zilen != 0:
                zilen += 1
                continue
            if s[0:zilen] * (len(s) // zilen) == s:
                return True
            zilen += 1
        return False
# leetcode submit region end(Prohibit modification and deletion)
