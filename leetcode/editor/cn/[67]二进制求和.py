# 给你两个二进制字符串，返回它们的和（用二进制表示）。 
# 
#  输入为 非空 字符串且只包含数字 1 和 0。 
# 
#  
# 
#  示例 1: 
# 
#  输入: a = "11", b = "1"
# 输出: "100" 
# 
#  示例 2: 
# 
#  输入: a = "1010", b = "1011"
# 输出: "10101" 
# 
#  
# 
#  提示： 
# 
#  
#  每个字符串仅由字符 '0' 或 '1' 组成。 
#  1 <= a.length, b.length <= 10^4 
#  字符串如果不是 "0" ，就都不含前导零。 
#  
#  Related Topics 位运算 数学 字符串 模拟 👍 751 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = int(a, 2) + int(b, 2)
        d = bin(c).replace("0b", "")
        return d

    # leetcode submit region end(Prohibit modification and deletion)


print(int("11", 2))
