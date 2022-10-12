# 给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: num = 100
# 输出: "202"
#  
# 
#  示例 2: 
# 
#  
# 输入: num = -7
# 输出: "-10"
#  
# 
#  
# 
#  提示： 
# 
#  
#  -10⁷ <= num <= 10⁷ 
#  
#  Related Topics 数学 👍 171 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        flag = num < 0
        digits = []
        num = abs(num)
        while num:
            digits.append(str(num % 7))
            num //= 7
        if flag:
            digits.append("-")
        digits.reverse()
        return "".join(digits)
# leetcode submit region end(Prohibit modification and deletion)
print(",".join(["1","2","a"]))