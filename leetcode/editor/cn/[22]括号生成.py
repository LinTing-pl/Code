# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：["()"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
#  Related Topics 字符串 动态规划 回溯 👍 2385 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def g(a, l, r):
            if len(a) == 2 * n:
                ans.append("".join(a))
                return
            if l < n:
                a.append("(")
                g(a, l + 1, r)
                a.pop()
            if r < l:
                a.append(")")
                g(a, l, r + 1)
                a.pop()

        ans = []
        g([], 0, 0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
a = Solution()
a.generateParenthesis(2)
