# 给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后可以满足 “对于每个 0 <= i < len(arr) / 2，都有 arr[2 * i 
# + 1] = 2 * arr[2 * i]” 时，返回 true；否则，返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [3,1,3,6]
# 输出：false
#  
# 
#  示例 2： 
# 
#  
# 输入：arr = [2,1,2,6]
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：arr = [4,-2,2,-4]
# 输出：true
# 解释：可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= arr.length <= 3 * 10⁴ 
#  arr.length 是偶数 
#  -10⁵ <= arr[i] <= 10⁵ 
#  
#  Related Topics 贪心 数组 哈希表 排序 👍 181 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        num_map = collections.Counter(arr)
        for num in sorted(num_map, key=abs):
            if num_map[num] > num_map[2 * num]:
                return False
            num_map[2 * num] -= num_map[num]
        return True
# leetcode submit region end(Prohibit modification and deletion)
