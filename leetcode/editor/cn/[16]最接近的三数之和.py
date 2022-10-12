# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。 
# 
#  返回这三个数的和。 
# 
#  假定每组输入只存在恰好一个解。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,0,0], target = 1
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 1000 
#  -1000 <= nums[i] <= 1000 
#  -10⁴ <= target <= 10⁴ 
#  
#  Related Topics 数组 双指针 排序 👍 1050 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        l = len(nums)
        r = 100000000
        for first in range(l - 2):
            if first > 0 and nums[first] == nums[first - 1]: continue
            second, third = first + 1, l - 1
            while third > second:
                curr = nums[first] + nums[second] + nums[third]
                if curr == target:
                    return curr
                if abs(r - target) > abs(curr - target):
                    r = curr
                if curr > target:
                    third = third - 1
                    while second < third and nums[third + 1] == nums[third]:
                        third -= 1

                else:
                    second += 1
                    while second < third and nums[second] == nums[second - 1]:
                        second += 1

        return r


# leetcode submit region end(Prohibit modification and deletion)
a = Solution()
print(a.threeSumClosest([1, 2, 1, -4], 1))
a = 0
for i in [0, 2, 1, -3]:
    a += i
print(a)
