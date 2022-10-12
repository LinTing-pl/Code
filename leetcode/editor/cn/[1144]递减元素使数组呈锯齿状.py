# 给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。 
# 
#  如果符合下列情况之一，则数组 A 就是 锯齿数组： 
# 
#  
#  每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ... 
#  或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ... 
#  
# 
#  返回将数组 nums 转换为锯齿数组所需的最小操作次数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,2,3]
# 输出：2
# 解释：我们可以把 2 递减到 0，或把 3 递减到 1。
#  
# 
#  示例 2： 
# 
#  输入：nums = [9,6,1,6,2]
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  1 <= nums[i] <= 1000 
#  
#  Related Topics 贪心 数组 👍 40 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans1, ans2 = 0, 0
        for i in range(n):
            # 奇数位置
            if i % 2 == 0:
                d1 = nums[i] - nums[i - 1] + 1 if i > 0 and nums[i] >= nums[i - 1] else 0
                d2 = nums[i] - nums[i + 1] + 1 if i < n - 1 and nums[i] >= nums[i + 1] else 0
                ans1 += max(d1, d2)
            # 偶数位置
            else:
                d1 = nums[i] - nums[i - 1] + 1 if nums[i] >= nums[i - 1] else 0
                d2 = nums[i] - nums[i + 1] + 1 if i < n - 1 and nums[i] >= nums[i + 1] else 0
                ans2 += max(d1, d2)
        return min(ans1, ans2)
# leetcode submit region end(Prohibit modification and deletion)
