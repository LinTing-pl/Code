# 给你一个整数 n 。按下述规则生成一个长度为 n + 1 的数组 nums ： 
# 
#  
#  nums[0] = 0 
#  nums[1] = 1 
#  当 2 <= 2 * i <= n 时，nums[2 * i] = nums[i] 
#  当 2 <= 2 * i + 1 <= n 时，nums[2 * i + 1] = nums[i] + nums[i + 1] 
#  
# 
#  返回生成数组 nums 中的 最大 值。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 7
# 输出：3
# 解释：根据规则：
#   nums[0] = 0
#   nums[1] = 1
#   nums[(1 * 2) = 2] = nums[1] = 1
#   nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
#   nums[(2 * 2) = 4] = nums[2] = 1
#   nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
#   nums[(3 * 2) = 6] = nums[3] = 2
#   nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
# 因此，nums = [0,1,1,2,1,3,2,3]，最大值 3
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 2
# 输出：1
# 解释：根据规则，nums[0]、nums[1] 和 nums[2] 之中的最大值是 1
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 3
# 输出：2
# 解释：根据规则，nums[0]、nums[1]、nums[2] 和 nums[3] 之中的最大值是 2
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 100 
#  
#  Related Topics 数组 动态规划 模拟 👍 66 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1):
            nums[i] = nums[i // 2] + i % 2 * nums[i // 2 + 1]
        return max(nums)
# leetcode submit region end(Prohibit modification and deletion)
