# 给你一个整数数组 nums ，你可以对它进行一些操作。 
# 
#  每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i]
#  + 1 的元素。 
# 
#  开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [3,4,2]
# 输出：6
# 解释：
# 删除 4 获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 获得 2 个点数。总共获得 6 个点数。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2,3,3,3,4]
# 输出：9
# 解释：
# 删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
# 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
# 总共获得 9 个点数。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  1 <= nums[i] <= 10⁴ 
#  
#  Related Topics 数组 哈希表 动态规划 👍 628 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnts = [0] * 10010
        n = len(nums)
        m = 0
        for x in nums:
            cnts[x] += 1
            m = max(m, x)
        # f[i][0] 代表「不选」数值 i；f[i][1] 代表「选择」数值 i
        f = [[0] * 2 for _ in range(m + 1)]
        for i in range(1, m + 1):
            f[i][1] = f[i - 1][0] + i * cnts[i]
            f[i][0] = max(f[i - 1][1], f[i - 1][0])
        return max(f[m][0], f[m][1])
# leetcode submit region end(Prohibit modification and deletion)
