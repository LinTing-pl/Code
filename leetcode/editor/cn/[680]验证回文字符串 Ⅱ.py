# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。 
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
# 解释: 你可以删除c字符。
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
#  Related Topics 贪心 双指针 字符串 👍 460 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def check(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return check(low + 1, high) or check(low, high - 1)
        return True
# leetcode submit region end(Prohibit modification and deletion)
