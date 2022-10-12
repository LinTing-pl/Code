# 给你一个整数数组 arr 和一个整数 k ，其中数组长度是偶数，值为 n 。 
# 
#  现在需要把数组恰好分成 n / 2 对，以使每对数字的和都能够被 k 整除。 
# 
#  如果存在这样的分法，请返回 True ；否则，返回 False 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# 输出：true
# 解释：划分后的数字对为 (1,9),(2,8),(3,7),(4,6) 以及 (5,10) 。
#  
# 
#  示例 2： 
# 
#  
# 输入：arr = [1,2,3,4,5,6], k = 7
# 输出：true
# 解释：划分后的数字对为 (1,6),(2,5) 以及 (3,4) 。
#  
# 
#  示例 3： 
# 
#  
# 输入：arr = [1,2,3,4,5,6], k = 10
# 输出：false
# 解释：无法在将数组中的数字分为三对的同时满足每对数字和能够被 10 整除的条件。
#  
# 
#  
# 
#  提示： 
# 
#  
#  arr.length == n 
#  1 <= n <= 10⁵ 
#  n 为偶数 
#  -10⁹ <= arr[i] <= 10⁹ 
#  1 <= k <= 10⁵ 
#  
#  Related Topics 数组 哈希表 计数 👍 66 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        mod = [0] * k
        for num in arr:
            mod[num % k] += 1
        if any(mod[i] != mod[k - i] for i in range(1, k // 2 + 1)):
            return False
        return mod[0] % 2 == 0
# leetcode submit region end(Prohibit modification and deletion)
