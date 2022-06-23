# 给你一个整数数组 nums，请你返回该数组中恰有四个因数的这些整数的各因数之和。如果数组中不存在满足题意的整数，则返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [21,4,7]
# 输出：32
# 解释：
# 21 有 4 个因数：1, 3, 7, 21
# 4 有 3 个因数：1, 2, 4
# 7 有 2 个因数：1, 7
# 答案仅为 21 的所有因数的和。
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [21,21]
# 输出: 64
#  
# 
#  示例 3: 
# 
#  
# 输入: nums = [1,2,3,4,5]
# 输出: 0 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  1 <= nums[i] <= 10⁵ 
#  
#  Related Topics 数组 数学 👍 23 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            # factor_cnt: 因数的个数
            # factor_sum: 因数的和
            factor_cnt = factor_sum = 0
            i = 1
            while i * i <= num:
                if num % i == 0:
                    factor_cnt += 1
                    factor_sum += i
                    if i * i != num:  # 判断 i 和 num/i 是否相等，若不相等才能将 num/i 看成新的因数
                        factor_cnt += 1
                        factor_sum += num // i
                i += 1
            if factor_cnt == 4:
                ans += factor_sum
        return ans
# leetcode submit region end(Prohibit modification and deletion)
