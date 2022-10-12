# 给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改
#  数组以供接下来的操作使用。 
# 
#  如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,4,2,3], x = 5
# 输出：2
# 解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,6,7,8,9], x = 4
# 输出：-1
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,2,20,1,1,3], x = 10
# 输出：5
# 解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁴ 
#  1 <= x <= 10⁹ 
#  
#  Related Topics 数组 哈希表 二分查找 前缀和 滑动窗口 👍 106 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        a = sum(nums)
        b = a - x
        cl = len(nums)
        if b < 0:
            return -1
        elif b == 0:
            return cl
        l = r = 0
        ans = cl
        t = nums[0]
        while l < cl:
            # t=nums[l]
            # t=sum(nums[l,r+1])#还可以?
            while t < b:
                r += 1
                if r < cl:
                    t += nums[r]
                else:
                    r -= 1
                    break
            if t == b:
                ans = min(ans, cl - r + l - 1)

            # t的右减吗？到更小先
            t -= nums[l]
            l += 1
            while t > b:
                t -= nums[r]
                if r >= l:
                    r -= 1
                else:
                    break
        if ans == cl:
            return -1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
