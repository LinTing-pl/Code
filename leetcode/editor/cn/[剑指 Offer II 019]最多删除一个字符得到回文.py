# 给定一个非空字符串 s，请判断如果 最多 从字符串中删除一个字符能否得到一个回文字符串。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "aba"
# 输出: true
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "abca"
# 输出: true
# 解释: 可以删除 "c" 字符 或者 "b" 字符
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "abc"
# 输出: false 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s 由小写英文字母组成 
#  
# 
#  
# 
#  注意：本题与主站 680 题相同： https://leetcode-cn.com/problems/valid-palindrome-ii/ 
#  Related Topics 贪心 双指针 字符串 👍 30 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]: return True
        cnt = 0
        n = len(s)
        p, q = 0, n - 1
        while p <= q:
            if s[p] == s[q]:
                p += 1
                q -= 1
                continue
            elif s[p:q] == s[p:q][::-1] or s[p + 1:q + 1] == s[p + 1:q + 1][::-1]:
                return True
            else:
                return False

# leetcode submit region end(Prohibit modification and deletion)
