# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[
# b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）： 
# 
#  
#  0 <= a, b, c, d < n 
#  a、b、c 和 d 互不相同 
#  nums[a] + nums[b] + nums[c] + nums[d] == target 
#  
# 
#  你可以按 任意顺序 返回答案 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  
#  Related Topics 数组 双指针 排序 👍 1130 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        l = len(nums)
        r = []
        for first in range(l - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            if nums[first] + nums[first + 1] + nums[first + 2] + nums[first + 3] > target:
                break
            if nums[first] + nums[l - 3] + nums[l - 2] + nums[l - 1] < target:
                continue
            for second in range(first + 1, l - 2):
                third, forth = second + 1, l - 1
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                if nums[first] + nums[second] + nums[second + 1] + nums[second + 2] > target:
                    break
                if nums[first] + nums[second] + nums[l - 2] + nums[l - 1] < target:
                    continue
                while third < forth:
                    curr = nums[first] + nums[second] + nums[third] + nums[forth]
                    if curr == target:
                        r.append([nums[first], nums[second], nums[third], nums[forth]])
                        while third < forth and nums[third] == nums[third + 1]:
                            third += 1
                        third += 1
                        while third < forth and nums[forth] == nums[forth - 1]:
                            forth -= 1
                        forth -= 1
                    elif curr > target:
                        forth = forth - 1
                    else:
                        third = third + 1
        return r


# leetcode submit region end(Prohibit modification and deletion)
a = Solution()
a.fourSum([1, 0, -1, 0, -2, 2], 0)
