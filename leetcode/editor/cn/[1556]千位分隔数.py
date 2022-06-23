# 给你一个整数 n，请你每隔三位添加点（即 "." 符号）作为千位分隔符，并将结果以字符串格式返回。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 987
# 输出："987"
#  
# 
#  示例 2： 
# 
#  输入：n = 1234
# 输出："1.234"
#  
# 
#  示例 3： 
# 
#  输入：n = 123456789
# 输出："123.456.789"
#  
# 
#  示例 4： 
# 
#  输入：n = 0
# 输出："0"
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n < 2^31 
#  
#  Related Topics 字符串 👍 19 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        count = 0
        for i in str(n)[::-1]:
            if count == 3:
                ans += "."
                count = 0
            ans += i
            count += 1
        return ans[::-1]
    # leetcode submit region end(Prohibit modification and deletion)
