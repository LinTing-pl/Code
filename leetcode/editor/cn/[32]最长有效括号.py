# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = ""
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 3 * 10⁴ 
#  s[i] 为 '(' 或 ')' 
#  
#  
#  
#  Related Topics 栈 字符串 动态规划 👍 1670 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        stack = []
        ans = 0
        for i in range(len(s)):
            if not stack or s[i] == "(" or s[stack[-1]] == ")":
                stack.append(i)
            else:
                stack.pop()
                ans = max(ans, i - (stack[-1] if stack else -1))
        return ans


# leetcode submit region end(Prohibit modification and deletion)
a = Solution()
a.longestValidParentheses("()()(())")
