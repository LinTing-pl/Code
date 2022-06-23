# 给定两个整数 a 和 b ，返回 任意 字符串 s ，要求满足： 
# 
#  
#  s 的长度为 a + b，且正好包含a 个 'a' 字母与 b 个 'b' 字母； 
#  子串 'aaa' 没有出现在 s 中； 
#  子串 'bbb' 没有出现在 s 中。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：a = 1, b = 2
# 输出："abb"
# 解释："abb", "bab" 和 "bba" 都是正确答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：a = 4, b = 1
# 输出："aabaa" 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= a, b <= 100 
#  对于给定的 a 和 b，保证存在满足要求的 s 
#  
#  Related Topics 贪心 字符串 👍 73 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        ans = []

        while a or b:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                writeA = ans[-1] == 'b'
            else:
                writeA = a >= b

            if writeA:
                a -= 1
                ans.append('a')
            else:
                b -= 1
                ans.append('b')

        return "".join(ans)
# leetcode submit region end(Prohibit modification and deletion)
