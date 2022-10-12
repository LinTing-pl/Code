# 给你两个 非负 整数 num1 和 num2 。 
# 
#  每一步 操作 中，如果 num1 >= num2 ，你必须用 num1 减 num2 ；否则，你必须用 num2 减 num1 。 
# 
#  
#  例如，num1 = 5 且 num2 = 4 ，应该用 num1 减 num2 ，因此，得到 num1 = 1 和 num2 = 4 。然而，如果 
# num1 = 4且 num2 = 5 ，一步操作后，得到 num1 = 4 和 num2 = 1 。 
#  
# 
#  返回使 num1 = 0 或 num2 = 0 的 操作数 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：num1 = 2, num2 = 3
# 输出：3
# 解释：
# - 操作 1 ：num1 = 2 ，num2 = 3 。由于 num1 < num2 ，num2 减 num1 得到 num1 = 2 ，num2 = 3 
# - 2 = 1 。
# - 操作 2 ：num1 = 2 ，num2 = 1 。由于 num1 > num2 ，num1 减 num2 。
# - 操作 3 ：num1 = 1 ，num2 = 1 。由于 num1 == num2 ，num1 减 num2 。
# 此时 num1 = 0 ，num2 = 1 。由于 num1 == 0 ，不需要再执行任何操作。
# 所以总操作数是 3 。
#  
# 
#  示例 2： 
# 
#  
# 输入：num1 = 10, num2 = 10
# 输出：1
# 解释：
# - 操作 1 ：num1 = 10 ，num2 = 10 。由于 num1 == num2 ，num1 减 num2 得到 num1 = 10 - 10 =
#  0 。
# 此时 num1 = 0 ，num2 = 10 。由于 num1 == 0 ，不需要再执行任何操作。
# 所以总操作数是 1 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= num1, num2 <= 10⁵ 
#  
#  Related Topics 数学 模拟 👍 5 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        res = 0
        while num1 and num2:
            res += num1 // num2
            num1 %= num2
            num1, num2 = num2, num1
        return res
# leetcode submit region end(Prohibit modification and deletion)
