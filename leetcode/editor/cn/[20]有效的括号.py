# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。 
# 
#  有效字符串需满足： 
# 
#  
#  左括号必须用相同类型的右括号闭合。 
#  左括号必须以正确的顺序闭合。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "()"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "()[]{}"
# 输出：true
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "(]"
# 输出：false
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "([)]"
# 输出：false
#  
# 
#  示例 5： 
# 
#  
# 输入：s = "{[]}"
# 输出：true 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 仅由括号 '()[]{}' 组成 
#  
#  Related Topics 栈 字符串 👍 3006 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        obj = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for ch in s:
            if ch in obj:
                if not stack or stack[-1] != obj[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack
    # leetcode submit region end(Prohibit modification and deletion)
