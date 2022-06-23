# 给你一个长度为 n 的整数数组 nums ，返回使所有数组元素相等需要的最少移动数。 
# 
#  在一步操作中，你可以使数组中的一个元素加 1 或者减 1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：2
# 解释：
# 只需要两步操作（每步操作指南使一个元素加 1 或减 1）：
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,10,2,9]
# 输出：16
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
#  Related Topics 数组 数学 排序 👍 158 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        nums.sort()
        mid = nums[len(nums) // 2]
        for i in nums:
            ret += abs(i - mid)
        return ret
# leetcode submit region end(Prohibit modification and deletion)
