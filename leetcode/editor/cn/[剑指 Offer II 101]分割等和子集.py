# 给定一个非空的正整数数组 nums ，请判断能否将这些数字分成元素和相等的两部分。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：nums 可以分割成 [1, 5, 5] 和 [11] 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：nums 不可以分为和相等的两部分
#  
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 100 
#  
# 
#  
# 
#  注意：本题与主站 416 题相同： https://leetcode-cn.com/problems/partition-equal-subset-
# sum/ 
#  Related Topics 数学 字符串 模拟 👍 36 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        nums.sort()
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] | dp[i - num]
        return dp[target]
# leetcode submit region end(Prohibit modification and deletion)
