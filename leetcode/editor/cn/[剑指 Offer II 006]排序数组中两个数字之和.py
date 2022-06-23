# 给定一个已按照 升序排列 的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。 
# 
#  函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 0 开始计数 ，所以答案数组应当满足 0 <= answer[0]
#  < answer[1] < numbers.length 。 
# 
#  假设数组中存在且只存在一对符合条件的数字，同时一个数字不能使用两次。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：numbers = [1,2,4,6,10], target = 8
# 输出：[1,3]
# 解释：2 与 6 之和等于目标数 8 。因此 index1 = 1, index2 = 3 。
#  
# 
#  示例 2： 
# 
#  
# 输入：numbers = [2,3,4], target = 6
# 输出：[0,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：numbers = [-1,0], target = -1
# 输出：[0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= numbers.length <= 3 * 10⁴ 
#  -1000 <= numbers[i] <= 1000 
#  numbers 按 递增顺序 排列 
#  -1000 <= target <= 1000 
#  仅存在一个有效答案 
#  
# 
#  
# 
#  注意：本题与主站 167 题相似（下标起点不同）：https://leetcode-cn.com/problems/two-sum-ii-input-
# array-is-sorted/ 
#  Related Topics 数组 双指针 二分查找 👍 30 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i, j]
# leetcode submit region end(Prohibit modification and deletion)
