# 在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个"LX"替换一个"XL"，或
# 者用一个"XR"替换一个"RX"。现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时， 返回
# True。 
# 
#  
# 
#  示例 : 
# 
#  输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
# 输出: True
# 解释:
# 我们可以通过以下几步将start转换成end:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= len(start) = len(end) <= 10000。 
#  start和end中的字符串仅限于'L', 'R'和'X'。 
#  
#  Related Topics 双指针 字符串 👍 118 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import operator


class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if start.replace('X', '') != end.replace('X', ''):
            return False

        for (symbol, op) in (('L', operator.ge), ('R', operator.le)):
            B = (i for i, c in enumerate(end) if c == symbol)
            for i, c in enumerate(start):
                if c == symbol and not op(i, next(B)):
                    return False

        return True
# leetcode submit region end(Prohibit modification and deletion)
