# 把符合下列属性的数组 arr 称为 山脉数组 ： 
# 
#  
#  arr.length >= 3 
#  存在下标 i（0 < i < arr.length - 1），满足
#  
#  arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
#  arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 
#  
#  
#  
# 
#  给出一个整数数组 arr，返回最长山脉子数组的长度。如果不存在山脉子数组，返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [2,1,4,7,3,2,5]
# 输出：5
# 解释：最长的山脉子数组是 [1,4,7,3,2]，长度为 5。
#  
# 
#  示例 2： 
# 
#  
# 输入：arr = [2,2,2]
# 输出：0
# 解释：不存在山脉子数组。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10⁴ 
#  0 <= arr[i] <= 10⁴ 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你可以仅用一趟扫描解决此问题吗？ 
#  你可以用 O(1) 空间解决此问题吗？ 
#  
#  Related Topics 数组 双指针 动态规划 枚举 👍 238 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0

        n = len(arr)
        left = [0] * n
        for i in range(1, n):
            left[i] = (left[i - 1] + 1 if arr[i - 1] < arr[i] else 0)

        right = [0] * n
        for i in range(n - 2, -1, -1):
            right[i] = (right[i + 1] + 1 if arr[i + 1] < arr[i] else 0)

        ans = 0
        for i in range(n):
            if left[i] > 0 and right[i] > 0:
                ans = max(ans, left[i] + right[i] + 1)

        return ans
# leetcode submit region end(Prohibit modification and deletion)
