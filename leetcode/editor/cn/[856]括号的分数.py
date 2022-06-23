# 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数： 
# 
#  
#  () 得 1 分。 
#  AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。 
#  (A) 得 2 * A 分，其中 A 是平衡括号字符串。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入： "()"
# 输出： 1
#  
# 
#  示例 2： 
# 
#  输入： "(())"
# 输出： 2
#  
# 
#  示例 3： 
# 
#  输入： "()()"
# 输出： 2
#  
# 
#  示例 4： 
# 
#  输入： "(()(()))"
# 输出： 6
#  
# 
#  
# 
#  提示： 
# 
#  
#  S 是平衡括号字符串，且只含有 ( 和 ) 。 
#  2 <= S.length <= 50 
#  
#  Related Topics 栈 字符串 👍 286 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        def F(i, j):
            # Score of balanced string S[i:j]
            ans = bal = 0

            # Split string into primitives
            for k in range(i, j):
                bal += 1 if s[k] == '(' else -1
                if bal == 0:
                    if k - i == 1:
                        ans += 1
                    else:
                        ans += 2 * F(i + 1, k)
                    i = k + 1

            return ans

        return F(0, len(s))
# leetcode submit region end(Prohibit modification and deletion)
