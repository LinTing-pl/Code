# 给你一个整数数组 nums 和一个整数 k ，请你返回数对 (i, j) 的数目，满足 i < j 且 |nums[i] - nums[j]| == k 。
#  
# 
#  |x| 的值定义为： 
# 
#  
#  如果 x >= 0 ，那么值为 x 。 
#  如果 x < 0 ，那么值为 -x 。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,2,2,1], k = 1
# 输出：4
# 解释：差的绝对值为 1 的数对为：
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
#  
# 
#  示例 2： 
# 
#  输入：nums = [1,3], k = 3
# 输出：0
# 解释：没有任何数对差的绝对值为 3 。
#  
# 
#  示例 3： 
# 
#  输入：nums = [3,2,1,5,4], k = 2
# 输出：3
# 解释：差的绝对值为 2 的数对为：
# - [3,2,1,5,4]
# - [3,2,1,5,4]
# - [3,2,1,5,4]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 100 
#  1 <= k <= 99 
#  
#  Related Topics 数组 哈希表 计数 👍 70 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import itertools


class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sum(abs(x - y) == k for x, y in itertools.combinations(nums, 2))
# leetcode submit region end(Prohibit modification and deletion)
