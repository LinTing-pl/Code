# 给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得
# 从 1 到 n 的 min(ai, bi) 总和最大。 
# 
#  返回该 最大总和 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,4,3,2]
# 输出：4
# 解释：所有可能的分法（忽略元素顺序）为：
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# 所以最大总和为 4 
# 
#  示例 2： 
# 
#  
# 输入：nums = [6,2,6,5,1,2]
# 输出：9
# 解释：最优的分法为 (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 
# 6 = 9
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10⁴ 
#  nums.length == 2 * n 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
#  Related Topics 贪心 数组 计数排序 排序 👍 286 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])
# leetcode submit region end(Prohibit modification and deletion)
