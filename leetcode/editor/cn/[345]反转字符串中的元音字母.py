# 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。 
# 
#  元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "hello"
# 输出："holle"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "leetcode"
# 输出："leotcede" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 3 * 10⁵ 
#  s 由 可打印的 ASCII 字符组成 
#  
#  Related Topics 双指针 字符串 👍 240 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        def isYuan(ch):
            return ch in "aeiouAEIOU"

        n = len(s)
        s = list(s)
        i, j = 0, n - 1
        while i < j:
            while i < j and not isYuan(s[i]):
                i += 1
            while j > i and not isYuan(s[j]):
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)
# leetcode submit region end(Prohibit modification and deletion)
