# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。 
# 
#  注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [10,2]
# 输出："210" 
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 10⁹ 
#  
#  Related Topics 贪心 字符串 排序 👍 922 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import functools


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums[:] = [str(i) for i in nums]
        nums.sort(key=functools.cmp_to_key(lambda x, y: int(str(y) + str(x)) - int(str(x) + str(y))))
        res = "".join(nums)
        return "0" if res[0] == "0" else res
# leetcode submit region end(Prohibit modification and deletion)
