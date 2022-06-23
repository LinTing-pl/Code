# 给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# 输出：3
# 解释：长度最长的公共子数组是 [3,2,1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums1.length, nums2.length <= 1000 
#  0 <= nums1[i], nums2[i] <= 100 
#  
#  Related Topics 数组 二分查找 动态规划 滑动窗口 哈希函数 滚动哈希 👍 708 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] + 1 if nums1[i] == nums2[j] else 0
                ans = max(ans, dp[i][j])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
