# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[
# j]) 都应当满足：
#  
#  answer[i] % answer[j] == 0 ，或 
#  answer[j] % answer[i] == 0 
#  
# 
#  如果存在多个有效解子集，返回其中任何一个均可。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[1,2]
# 解释：[1,3] 也会被视为正确答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,4,8]
# 输出：[1,2,4,8]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  1 <= nums[i] <= 2 * 10⁹ 
#  nums 中的所有整数 互不相同 
#  
#  Related Topics 数组 数学 动态规划 排序 👍 438 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        f, g = [0] * n, [0] * n
        for i in range(n):
            length, prev = 1, i
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if f[j] + 1 > length:
                        length = f[j] + 1
                        prev = j
            f[i] = length
            g[i] = prev
        max_len = idx = -1
        for i in range(n):
            if f[i] > max_len:
                idx = i
                max_len = f[i]
        ans = []
        while len(ans) < max_len:
            ans.append(nums[idx])
            idx = g[idx]
        ans.reverse()
        return ans
# leetcode submit region end(Prohibit modification and deletion)
