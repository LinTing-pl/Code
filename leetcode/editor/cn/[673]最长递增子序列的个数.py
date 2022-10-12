# 给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。 
# 
#  注意 这个数列必须是 严格 递增的。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
#  
# 
#  示例 2: 
# 
#  
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
#  
# 
#  
# 
#  提示: 
# 
#  
# 
#  
#  1 <= nums.length <= 2000 
#  -10⁶ <= nums[i] <= 10⁶ 
#  
#  Related Topics 树状数组 线段树 数组 动态规划 👍 600 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, max_len, ans = len(nums), 0, 0
        dp = [0] * n
        cnt = [0] * n
        for i, x in enumerate(nums):
            dp[i] = 1
            cnt[i] = 1
            for j in range(i):
                if x > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]  # 重置计数
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
            if dp[i] > max_len:
                max_len = dp[i]
                ans = cnt[i]  # 重置计数
            elif dp[i] == max_len:
                ans += cnt[i]
        return ans
# leetcode submit region end(Prohibit modification and deletion)
