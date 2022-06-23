# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。 
# 
#  进阶：你可以在 O(n) 的时间解决这个问题吗？ 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：nums = [3,10,5,25,2,8]
# 输出：28
# 解释：最大运算结果是 5 XOR 25 = 28. 
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [2,4]
# 输出：6
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [8,10,2]
# 输出：10
#  
# 
#  示例 5： 
# 
#  
# 输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# 输出：127
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  0 <= nums[i] <= 2³¹ - 1 
#  
#  
#  
#  Related Topics 位运算 字典树 数组 哈希表 👍 439 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

class Trie:
    def __init__(self, val):
        self.val = val
        self.child = {}


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(format(max(nums), "b")) - 1
        root = Trie(-1)
        for n in nums:
            curr = root
            for i in range(L, -1, -1):
                v = (n >> i) & 1
                if v not in curr.child:
                    curr.child[v] = Trie(v)
                curr = curr.child[v]
        res = 0
        for n in nums:
            curr = root
            total = 0
            for i in range(L, -1, -1):
                v = (n >> i) & 1
                if 1 - v in curr.child:
                    total = total * 2 + 1
                    curr = curr.child[1 - v]
                else:
                    total = total * 2
                    curr = curr.child[v]
            res = max(res, total)
        return res

# leetcode submit region end(Prohibit modification and deletion)
