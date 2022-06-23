# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。 
# 
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[[],[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  
#  
#  
#  Related Topics 位运算 数组 回溯 👍 811 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import itertools


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        res = []

        def dfs(nums, tmp, k):
            if len(tmp) == k:
                res.append(tmp)
                return
            for i in range(len(nums)):
                dfs(nums[i + 1:], tmp + [nums[i]], k)

        for i in range(len(nums) + 1):
            dfs(nums, [], i)
        res = list(map(lambda x: sorted(x), res))
        ans = []
        for i in res:
            if i not in ans:
                ans.append(i)
        return ans
    # leetcode submit region end(Prohibit modification and deletion)
