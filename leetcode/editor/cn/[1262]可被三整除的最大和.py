# 给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [3,6,5,1,8]
# 输出：18
# 解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。 
# 
#  示例 2： 
# 
#  输入：nums = [4]
# 输出：0
# 解释：4 不能被 3 整除，所以无法选出数字，返回 0。
#  
# 
#  示例 3： 
# 
#  输入：nums = [1,2,3,4,4]
# 输出：12
# 解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 4 * 10^4 
#  1 <= nums[i] <= 10^4 
#  
#  Related Topics 贪心 数组 动态规划 👍 182 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[0] * 3 for _ in range(n + 1)]
        dp[0][0] = 0
        dp[0][1] = float("-inf")
        dp[0][2] = float("-inf")
        for k in range(n):
            if nums[k] % 3 == 0:  # k = 0 dp = 1
                dp[k + 1][0] = max(dp[k][0], dp[k][0] + nums[k])
                dp[k + 1][1] = max(dp[k][1], dp[k][1] + nums[k])
                dp[k + 1][2] = max(dp[k][2], dp[k][2] + nums[k])
            elif nums[k] % 3 == 1:
                dp[k + 1][0] = max(dp[k][0], dp[k][2] + nums[k])
                dp[k + 1][1] = max(dp[k][1], dp[k][0] + nums[k])
                dp[k + 1][2] = max(dp[k][2], dp[k][1] + nums[k])
            elif nums[k] % 3 == 2:
                dp[k + 1][0] = max(dp[k][0], dp[k][1] + nums[k])
                dp[k + 1][1] = max(dp[k][1], dp[k][2] + nums[k])
                dp[k + 1][2] = max(dp[k][2], dp[k][0] + nums[k])
        return dp[-1][0]
# leetcode submit region end(Prohibit modification and deletion)
