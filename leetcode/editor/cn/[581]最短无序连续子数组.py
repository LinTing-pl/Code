# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。 
# 
#  请你找出符合题意的 最短 子数组，并输出它的长度。 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：nums = [2,6,4,8,10,9,15]
# 输出：5
# 解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,4]
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
# 
#  
# 
#  进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？ 
#  
#  
#  Related Topics 栈 贪心 数组 双指针 排序 单调栈 👍 853 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        co = sorted(nums)
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == co[i]:
                i += 1
            else:
                break
        else:
            return 0
        if i <= j:
            while True:
                if nums[j] == co[j]:
                    j -= 1
                else:
                    break
        return j - i + 1
# leetcode submit region end(Prohibit modification and deletion)
