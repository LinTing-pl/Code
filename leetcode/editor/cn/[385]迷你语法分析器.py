# 给定一个字符串 s 表示一个整数嵌套列表，实现一个解析它的语法分析器并返回解析的结果 NestedInteger 。 
# 
#  列表中的每个元素只可能是整数或整数嵌套列表 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "324",
# 输出：324
# 解释：你应该返回一个 NestedInteger 对象，其中只包含整数值 324。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "[123,[456,[789]]]",
# 输出：[123,[456,[789]]]
# 解释：返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：
# 1. 一个 integer 包含值 123
# 2. 一个包含两个元素的嵌套列表：
#     i.  一个 integer 包含值 456
#     ii. 一个包含一个元素的嵌套列表
#          a. 一个 integer 包含值 789
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 5 * 10⁴ 
#  s 由数字、方括号 "[]"、负号 '-' 、逗号 ','组成 
#  用例保证 s 是可解析的 NestedInteger 
#  输入中的所有值的范围是 [-10⁶, 10⁶] 
#  
#  Related Topics 栈 深度优先搜索 字符串 👍 178 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if s[0] != "[": return NestedInteger(int(s))
        stack, num, negative = [], 0, False
        for i, c in enumerate(s):
            if c == "-":
                negative = True
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append(NestedInteger())
            elif c in ",]":
                if s[i - 1].isdigit():
                    if negative:
                        num = -num
                    stack[-1].add(NestedInteger(num))
                num, negative = 0, False
                if c == "]" and len(stack) > 1:
                    stack[-2].add(stack.pop())
        return stack.pop()
# leetcode submit region end(Prohibit modification and deletion)
