# 给你一个整数 num，请你找出同时满足下面全部要求的两个整数： 
# 
#  
#  两数乘积等于 num + 1 或 num + 2 
#  以绝对差进行度量，两数大小最接近 
#  
# 
#  你可以按任意顺序返回这两个整数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：num = 8
# 输出：[3,3]
# 解释：对于 num + 1 = 9，最接近的两个因数是 3 & 3；对于 num + 2 = 10, 最接近的两个因数是 2 & 5，因此返回 3 & 3 
# 。
#  
# 
#  示例 2： 
# 
#  输入：num = 123
# 输出：[5,25]
#  
# 
#  示例 3： 
# 
#  输入：num = 999
# 输出：[40,25]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num <= 10^9 
#  
#  Related Topics 数学 👍 27 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0, int(1e9)]
        for i in range(num + 1, num + 3):
            cur = self.divide(i)
            if abs(cur[0] - cur[1]) < abs(ans[0] - ans[1]):
                ans = cur
        return ans

    def divide(self, n):
        for i in range(int(math.sqrt(n)), 0, -1):
            if n % i == 0:
                return [i, n // i]

# leetcode submit region end(Prohibit modification and deletion)
