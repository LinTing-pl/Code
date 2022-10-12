# 给你一个可能含有 重复元素 的整数数组 nums ，请你随机输出给定的目标数字 target 的索引。你可以假设给定的数字一定存在于数组中。 
# 
#  实现 Solution 类： 
# 
#  
#  Solution(int[] nums) 用数组 nums 初始化对象。 
#  int pick(int target) 从 nums 中选出一个满足 nums[i] == target 的随机索引 i 。如果存在多个有效的索引，则每
# 个索引的返回概率应当相等。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["Solution", "pick", "pick", "pick"]
# [[[1, 2, 3, 3, 3]], [3], [1], [3]]
# 输出
# [null, 4, 0, 2]
# 
# 解释
# Solution solution = new Solution([1, 2, 3, 3, 3]);
# solution.pick(3); // 随机返回索引 2, 3 或者 4 之一。每个索引的返回概率应该相等。
# solution.pick(1); // 返回 0 。因为只有 nums[0] 等于 1 。
# solution.pick(3); // 随机返回索引 2, 3 或者 4 之一。每个索引的返回概率应该相等。
#  
# 
#  
# 
#  
#  
#  
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  target 是 nums 中的一个整数 
#  最多调用 pick 函数 10⁴ 次 
#  
#  
#  
#  
# 
#  
#  Related Topics 水塘抽样 哈希表 数学 随机化 👍 238 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.hs = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.hs[num].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.hs[target])

    # Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# leetcode submit region end(Prohibit modification and deletion)
