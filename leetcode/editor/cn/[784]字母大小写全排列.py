# 给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。 
# 
#  返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "3z4"
# 输出: ["3z4","3Z4"]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length <= 12 
#  s 由小写英文字母、大写英文字母和数字组成 
#  
#  Related Topics 位运算 字符串 回溯 👍 384 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = [[]]

        for char in s:
            n = len(ans)
            if char.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n + i].append(char.upper())
            else:
                for i in range(n):
                    ans[i].append(char)

        return map("".join, ans)
# leetcode submit region end(Prohibit modification and deletion)
