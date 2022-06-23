# 给你一个数组 nums 和一个整数 target 。 
# 
#  请你返回 非空不重叠 子数组的最大数目，且每个子数组中数字和都为 target 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,1,1,1,1], target = 2
# 输出：2
# 解释：总共有 2 个不重叠子数组（加粗数字表示） [1,1,1,1,1] ，它们的和为目标值 2 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [-1,3,5,1,4,2,-9], target = 6
# 输出：2
# 解释：总共有 3 个子数组和为 6 。
# ([5,1], [4,2], [3,5,1,4,2,-9]) 但只有前 2 个是不重叠的。 
# 
#  示例 3： 
# 
#  输入：nums = [-2,6,6,3,5,4,1,2,8], target = 10
# 输出：3
#  
# 
#  示例 4： 
# 
#  输入：nums = [0,0,0], target = 0
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  -10^4 <= nums[i] <= 10^4 
#  0 <= target <= 10^6 
#  
#  Related Topics 贪心 数组 哈希表 前缀和 👍 80 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        ret = 0
        i = 0
        while i < size:
            s = {0}
            total = 0
            while i < size:
                total += nums[i]
                if total - target in s:
                    ret += 1
                    break
                else:
                    s.add(total)
                    i += 1
            i += 1
        return ret
# leetcode submit region end(Prohibit modification and deletion)
