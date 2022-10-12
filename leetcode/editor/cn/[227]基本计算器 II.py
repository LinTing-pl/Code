# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。 
# 
#  整数除法仅保留整数部分。 
# 
#  你可以假设给定的表达式总是有效的。所有中间结果将在 [-2³¹, 2³¹ - 1] 的范围内。 
# 
#  注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "3+2*2"
# 输出：7
#  
# 
#  示例 2： 
# 
#  
# 输入：s = " 3/2 "
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：s = " 3+5 / 2 "
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 3 * 10⁵ 
#  s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开 
#  s 表示一个 有效表达式 
#  表达式中的所有整数都是非负整数，且在范围 [0, 2³¹ - 1] 内 
#  题目数据保证答案是一个 32-bit 整数 
#  
#  Related Topics 栈 数学 字符串 👍 558 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        stack = []
        preSign = "+"
        num = 0
        for i in range(n):
            if s[i] != " " and s[i].isdigit():
                num = num * 10 + int(s[i])
            if i == n - 1 or s[i] in "+-*/":
                if preSign == "+":
                    stack.append(num)
                elif preSign == "-":
                    stack.append(-num)
                elif preSign == "*":
                    stack.append(stack.pop() * num)
                elif preSign == "/":
                    a = stack.pop()
                    if a >= 0:
                        stack.append(a // num)
                    else:
                        stack.append(-int(-a / num))
                preSign = s[i]
                num = 0
        return sum(stack)
# leetcode submit region end(Prohibit modification and deletion)
