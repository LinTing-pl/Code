# 给你一个整数数组 nums 和一个正整数 k，请你判断是否可以把这个数组划分成一些由 k 个连续数字组成的集合。 
# 如果可以，请返回 true；否则，返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,3,4,4,5,6], k = 4
# 输出：true
# 解释：数组可以分成 [1,2,3,4] 和 [3,4,5,6]。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# 输出：true
# 解释：数组可以分成 [1,2,3] , [2,3,4] , [3,4,5] 和 [9,10,11]。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,3,2,2,1,1], k = 3
# 输出：true
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [1,2,3,4], k = 3
# 输出：false
# 解释：数组不能分成几个大小为 3 的子数组。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁹ 
#  
# 
#  
# 
#  注意：此题目与 846 重复：https://leetcode-cn.com/problems/hand-of-straights/ 
#  Related Topics 贪心 数组 哈希表 排序 👍 77 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) % k > 0:
            return False
        nums.sort()
        cnt = Counter(nums)
        for x in nums:
            if cnt[x] == 0:
                continue
            for num in range(x, x + k):
                if cnt[num] == 0:
                    return False
                cnt[num] -= 1
        return True
# leetcode submit region end(Prohibit modification and deletion)
