# 给你一个列表 nums ，里面每一个元素都是一个整数列表。请你依照下面各图的规则，按顺序返回 nums 中对角线上的整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：nums = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,4,2,7,5,3,8,6,9]
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# 输出：[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
#  
# 
#  示例 3： 
# 
#  输入：nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
# 输出：[1,4,2,5,3,8,6,9,7,10,11]
#  
# 
#  示例 4： 
# 
#  输入：nums = [[1,2,3,4,5,6]]
# 输出：[1,2,3,4,5,6]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  1 <= nums[i].length <= 10^5 
#  1 <= nums[i][j] <= 10^9 
#  nums 中最多有 10^5 个数字。 
#  
#  Related Topics 数组 排序 堆（优先队列） 👍 64 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        rec = []  # 用到了八皇后问题里的  左斜rc_sum 右斜rc_diff
        for i in range(len(nums)):  # 从上至下
            for j in range(len(nums[i])):  # 从左至右
                if i + j < len(rec):  # 左斜 rc_sum
                    rec[i + j].append(nums[i][j])
                else:  # 恰好利用rec的index作为rc_sum
                    rec.append([])
                    rec[i + j].append(nums[i][j])
        res = []
        for sub_list in rec:
            res += sub_list[::-1]  # r越小，越在当前左斜的后面
        return res
# leetcode submit region end(Prohibit modification and deletion)
