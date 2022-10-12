# 给定一个整数数组，找出总和最大的连续数列，并返回总和。 
# 
#  示例： 
# 
#  输入： [-2,1,-3,4,-1,2,1,-5,4]
# 输出： 6
# 解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
#  
# 
#  进阶： 
# 
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。 
#  Related Topics 数组 分治 动态规划 👍 112 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, ret = 0, nums[0]
        for num in nums:
            cnt = max(num, cnt + num)
            ret = max(ret, cnt)
        return ret
# leetcode submit region end(Prohibit modification and deletion)
