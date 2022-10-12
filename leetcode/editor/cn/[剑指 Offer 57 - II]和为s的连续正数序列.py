# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。 
# 
#  序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：target = 9
# 输出：[[2,3,4],[4,5]]
#  
# 
#  示例 2： 
# 
#  输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#  
# 
#  
# 
#  限制： 
# 
#  
#  1 <= target <= 10^5 
#  
# 
#  
#  Related Topics 数学 双指针 枚举 👍 419 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        i, j = 1, 2
        ans = []
        while j < target:
            if sum(range(i, j + 1)) < target:
                j += 1
            elif sum(range(i, j + 1)) > target:
                i += 1
            else:
                ans.append(range(i, j + 1))
                i += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
