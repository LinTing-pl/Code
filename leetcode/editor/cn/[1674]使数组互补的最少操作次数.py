# 给你一个长度为 偶数 n 的整数数组 nums 和一个整数 limit 。每一次操作，你可以将 nums 中的任何整数替换为 1 到 limit 之间的另一
# 个整数。 
# 
#  如果对于所有下标 i（下标从 0 开始），nums[i] + nums[n - 1 - i] 都等于同一个数，则数组 nums 是 互补的 。例如，数组 
# [1,2,3,4] 是互补的，因为对于所有下标 i ，nums[i] + nums[n - 1 - i] = 5 。 
# 
#  返回使数组 互补 的 最少 操作次数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,4,3], limit = 4
# 输出：1
# 解释：经过 1 次操作，你可以将数组 nums 变成 [1,2,2,3]（加粗元素是变更的数字）：
# nums[0] + nums[3] = 1 + 3 = 4.
# nums[1] + nums[2] = 2 + 2 = 4.
# nums[2] + nums[1] = 2 + 2 = 4.
# nums[3] + nums[0] = 3 + 1 = 4.
# 对于每个 i ，nums[i] + nums[n-1-i] = 4 ，所以 nums 是互补的。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,2,1], limit = 2
# 输出：2
# 解释：经过 2 次操作，你可以将数组 nums 变成 [2,2,2,2] 。你不能将任何数字变更为 3 ，因为 3 > limit 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,2,1,2], limit = 2
# 输出：0
# 解释：nums 已经是互补的。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  2 <= n <= 10⁵ 
#  1 <= nums[i] <= limit <= 10⁵ 
#  n 是偶数。 
#  
#  Related Topics 数组 哈希表 前缀和 👍 83 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        # 差分统计 以目标和为主线
        n = len(nums)
        sum_diff = [0 for _ in range(2 * limit + 2)]  # targetSum_operation
        for i in range(n // 2):
            A, B = nums[i], nums[n - 1 - i]

            L = 2
            R = 2 * limit
            sum_diff[L] += 2
            sum_diff[R + 1] -= 2
            ####操作多了的情况，这个情况1步就ok
            L = min(A, B) + 1
            R = max(A, B) + limit
            sum_diff[L] -= 1
            sum_diff[R + 1] += 1
            ####操作多了的情况，这个情况0步就ok
            L = A + B
            R = A + B
            sum_diff[L] -= 1
            sum_diff[R + 1] += 1

        res = n  # 最多的情况，是每个数字都要操作
        cur_op = 0
        for ab_sum in range(2, 2 * limit + 1):
            cur_op += sum_diff[ab_sum]
            res = min(res, cur_op)
        return res
# leetcode submit region end(Prohibit modification and deletion)
