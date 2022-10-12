# 给你一个字符串 s ，根据下述规则反转字符串： 
# 
#  
#  所有非英文字母保留在原有位置。 
#  所有英文字母（小写或大写）位置反转。 
#  
# 
#  返回反转后的 s 。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ab-cd"
# 输出："dc-ba"
#  
# 
#  
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
#  
# 
#  
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
#  
# 
#  
# 
#  提示 
# 
#  
#  1 <= s.length <= 100 
#  s 仅由 ASCII 值在范围 [33, 122] 的字符组成 
#  s 不含 '\"' 或 '\\' 
#  
#  Related Topics 双指针 字符串 👍 167 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = list(s)
        left, right = 0, len(s) - 1
        while True:
            while left < right and not ans[left].isalpha():
                left += 1
            while right > left and not ans[right].isalpha():
                right -= 1
            if left >= right: break
            ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1
        return "".join(ans)
# leetcode submit region end(Prohibit modification and deletion)
