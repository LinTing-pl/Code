# 给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。 
# 
#  环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i] 的前一个
# 元素是 nums[(i - 1 + n) % n] 。 
# 
#  子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j] ，不
# 存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,-2,3,-2]
# 输出：3
# 解释：从子数组 [3] 得到最大和 3
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,-3,5]
# 输出：10
# 解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,-2,2,-3]
# 输出：3
# 解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= n <= 3 * 10⁴ 
#  -3 * 10⁴ <= nums[i] <= 3 * 10⁴ 
#  
#  Related Topics 队列 数组 分治 动态规划 单调队列 👍 368 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)

        # Compute P[j] = sum(B[:j]) for the fixed array B = A+A
        P = [0]
        for _ in range(2):
            for x in nums:
                P.append(P[-1] + x)

        # Want largest P[j] - P[i] with 1 <= j-i <= N
        # For each j, want smallest P[i] with i >= j-N
        ans = nums[0]
        deque = collections.deque([0])  # i's, increasing by P[i]
        for j in range(1, len(P)):
            # If the smallest i is too small, remove it.
            if deque[0] < j - N:
                deque.popleft()

            # The optimal i is deque[0], for cand. answer P[j] - P[i].
            ans = max(ans, P[j] - P[deque[0]])

            # Remove any i1's with P[i2] <= P[i1].
            while deque and P[j] <= P[deque[-1]]:
                deque.pop()

            deque.append(j)

        return ans
# leetcode submit region end(Prohibit modification and deletion)
