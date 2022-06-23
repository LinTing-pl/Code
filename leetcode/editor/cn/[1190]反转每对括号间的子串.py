# 给出一个字符串 s（仅含有小写英文字母和括号）。 
# 
#  请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。 
# 
#  注意，您的结果中 不应 包含任何括号。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "(abcd)"
# 输出："dcba"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "(u(love)i)"
# 输出："iloveu"
# 解释：先反转子字符串 "love" ，然后反转整个字符串。 
# 
#  示例 3： 
# 
#  
# 输入：s = "(ed(et(oc))el)"
# 输出："leetcode"
# 解释：先反转子字符串 "oc" ，接着反转 "etco" ，然后反转整个字符串。 
# 
#  示例 4： 
# 
#  
# 输入：s = "a(bcdefghijkl(mno)p)q"
# 输出："apmnolkjihgfedcbq"
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 2000 
#  s 中只有小写英文字母和括号 
#  题目测试用例确保所有括号都是成对出现的 
#  
#  Related Topics 栈 字符串 👍 230 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []
        word = ""
        for c in s:
            if c == '(':  # 遇到新的一段了
                stk.append(word)  # 这段进stk
                word = ""  # 新的一段开始统计
            elif c == ')':
                word = stk.pop(-1) + word[::-1]  # 这一段要翻转了，与前面的一段可以接起来
            else:
                word += c  # 统计入当前的这一段
        return word
# leetcode submit region end(Prohibit modification and deletion)
