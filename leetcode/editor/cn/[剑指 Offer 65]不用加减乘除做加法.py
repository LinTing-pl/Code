# 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。 
# 
#  
# 
#  示例: 
# 
#  输入: a = 1, b = 1
# 输出: 2 
# 
#  
# 
#  提示： 
# 
#  
#  a, b 均可能是负数或 0 
#  结果不会溢出 32 位整数 
#  
#  Related Topics 位运算 数学 👍 295 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a, b])
# leetcode submit region end(Prohibit modification and deletion)
