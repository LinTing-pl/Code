# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。 
# 
#  示例 2: 
# 
#  
# 输入: nums = [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  nums[i] 不是 0 就是 1 
#  
#  Related Topics 数组 哈希表 前缀和 👍 555 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, prev, ans = {}, 0, 0
        for i in range(len(nums)):
            prev += 1 if nums[i] else -1
            if prev == 0:
                ans = max(ans, i + 1)
            elif prev not in cnt:
                cnt[prev] = i
            else:
                ans = max(ans, i - cnt[prev])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
