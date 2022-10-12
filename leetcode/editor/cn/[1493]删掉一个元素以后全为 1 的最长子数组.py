# 给你一个二进制数组 nums ，你需要从中删掉一个元素。 
# 
#  请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。 
# 
#  如果不存在这样的子数组，请返回 0 。 
# 
#  
# 
#  提示 1： 
# 
#  
# 输入：nums = [1,1,0,1]
# 输出：3
# 解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1,1,1,0,1,1,0,1]
# 输出：5
# 解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。 
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,1,1]
# 输出：2
# 解释：你必须要删除一个元素。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  nums[i] 要么是 0 要么是 1 。 
#  
#  Related Topics 数学 动态规划 滑动窗口 👍 60 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {1: 0, 0: 0}

        max_one = 0

        left, right = 0, 0

        # 如果nums列表里的0小于等于1个那么直接返回长度减一即可
        if nums.count(0) <= 1:
            return len(nums) - 1

        while right < len(nums):

            key = nums[right]
            nums_dict[key] += 1

            while nums_dict[0] > 1:
                max_one = max(max_one, (right - left - 1))
                nums_dict[nums[left]] -= 1
                left += 1
            right += 1

        max_one = max(max_one, (right - left - 1))

        return max_one
# leetcode submit region end(Prohibit modification and deletion)
