# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
#  Related Topics 数组 双指针 排序 👍 4352 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        r = []
        l = len(nums)
        for first in range(l):
            if first > 0 and nums[first] == nums[first - 1]: continue
            target = -nums[first]
            third = l - 1
            for second in range(first + 1, l-1):
                if second > first + 1 and nums[second] == nums[second - 1]: continue
                while second < third and -target + nums[second] + nums[third] > 0:
                    third -= 1
                if second == third: break
                if -target + nums[second] + nums[third] == 0:
                    r.append([-target, nums[second], nums[third]])
        return r


# leetcode submit region end(Prohibit modification and deletion)
a = Solution()
print(a.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
