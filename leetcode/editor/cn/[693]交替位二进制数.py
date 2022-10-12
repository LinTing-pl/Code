# 给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 5
# 输出：true
# 解释：5 的二进制表示是：101
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 7
# 输出：false
# 解释：7 的二进制表示是：111. 
# 
#  示例 3： 
# 
#  
# 输入：n = 11
# 输出：false
# 解释：11 的二进制表示是：1011. 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2³¹ - 1 
#  
#  Related Topics 位运算 👍 113 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        e=bin(n)[2:]
        return "00" not in e and "11" not in e
# leetcode submit region end(Prohibit modification and deletion)
