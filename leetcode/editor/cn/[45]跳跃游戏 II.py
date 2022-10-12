# 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。 
# 
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。 
# 
#  你的目标是使用最少的跳跃次数到达数组的最后一个位置。 
# 
#  假设你总是可以到达数组的最后一个位置。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [2,3,0,1,4]
# 输出: 2
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  0 <= nums[i] <= 1000 
#  
#  Related Topics 贪心 数组 动态规划 👍 1570 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, last_m, m, n = 0, 0, 0, len(nums)
        while m < n - 1:
            cur = m + 1
            for i in range(last_m, cur):
                cur = max(cur, i + nums[i])
            last_m, m = m + 1, cur
            ans += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
