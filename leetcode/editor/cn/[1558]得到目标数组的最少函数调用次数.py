# 
# 
#  给你一个与 nums 大小相同且初始值全为 0 的数组 arr ，请你调用以上函数得到整数数组 nums 。 
# 
#  请你返回将 arr 变成 nums 的最少函数调用次数。 
# 
#  答案保证在 32 位有符号整数以内。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,5]
# 输出：5
# 解释：给第二个数加 1 ：[0, 0] 变成 [0, 1] （1 次操作）。
# 将所有数字乘以 2 ：[0, 1] -> [0, 2] -> [0, 4] （2 次操作）。
# 给两个数字都加 1 ：[0, 4] -> [1, 4] -> [1, 5] （2 次操作）。
# 总操作次数为：1 + 2 + 2 = 5 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2]
# 输出：3
# 解释：给两个数字都加 1 ：[0, 0] -> [0, 1] -> [1, 1] （2 次操作）。
# 将所有数字乘以 2 ： [1, 1] -> [2, 2] （1 次操作）。
# 总操作次数为： 2 + 1 = 3 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [4,2,5]
# 输出：6
# 解释：（初始）[0,0,0] -> [1,0,0] -> [1,0,1] -> [2,0,2] -> [2,1,2] -> [4,2,4] -> [4,2,
# 5] （nums 数组）。
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [3,2,2,4]
# 输出：7
#  
# 
#  示例 5： 
# 
#  
# 输入：nums = [2,4,8,16]
# 输出：8
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  0 <= nums[i] <= 10^9 
#  
#  Related Topics 贪心 数组 👍 35 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxn = max(nums)
        ret = 0
        for num in nums:
            while num > 0:
                if num & 1:
                    ret += 1
                num >>= 1
        if maxn > 0:
            while maxn > 0:
                ret += 1
                maxn >>= 1
            ret -= 1

        return ret
# leetcode submit region end(Prohibit modification and deletion)
