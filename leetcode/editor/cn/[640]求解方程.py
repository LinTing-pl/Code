# 求解一个给定的方程，将x以字符串 "x=#value" 的形式返回。该方程仅包含 '+' ， '-' 操作，变量 x 和其对应系数。 
# 
#  如果方程没有解，请返回 "No solution" 。如果方程有无限解，则返回 “Infinite solutions” 。 
# 
#  如果方程中只有一个解，要保证返回值 'x' 是一个整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: equation = "x+5-3+x=6+x-2"
# 输出: "x=2"
#  
# 
#  示例 2: 
# 
#  
# 输入: equation = "x=x"
# 输出: "Infinite solutions"
#  
# 
#  示例 3: 
# 
#  
# 输入: equation = "2x=x"
# 输出: "x=0"
#  
# 
#  
# 
#  
# 
#  提示: 
# 
#  
#  3 <= equation.length <= 1000 
#  equation 只有一个 '='. 
#  equation 方程由整数组成，其绝对值在 [0, 100] 范围内，不含前导零和变量 'x' 。 
#  
#  Related Topics 数学 字符串 模拟 👍 87 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        l, r = equation.split('=')

        def parse(expression):
            w = 0
            b = 0
            expression = expression.replace('-', '+-')
            if expression.startswith('+'):
                expression = expression[1:]
            items = expression.split('+')
            for i in items:
                if i.endswith('x'):
                    s = i[:-1]
                    if s == '':
                        w += 1
                    elif s == '-':
                        w -= 1
                    else:
                        w += int(s)
                else:
                    b += int(i)
            return w, b

        lw, lb = parse(l)
        rw, rb = parse(r)
        fw = lw - rw
        fb = rb - lb
        if fw == 0:
            if fb == 0:
                return 'Infinite solutions'
            else:
                return 'No solution'
        return 'x={}'.format(fb // fw)
# leetcode submit region end(Prohibit modification and deletion)
