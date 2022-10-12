# 给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。 
# 
#  整数 a 比整数 b 更接近 x 需要满足： 
# 
#  
#  |a - x| < |b - x| 或者 
#  |a - x| == |b - x| 且 a < b 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [1,2,3,4,5], k = 4, x = 3
# 输出：[1,2,3,4]
#  
# 
#  示例 2： 
# 
#  
# 输入：arr = [1,2,3,4,5], k = 4, x = -1
# 输出：[1,2,3,4]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= arr.length 
#  1 <= arr.length <= 10⁴ 
#  arr 按 升序 排列 
#  -10⁴ <= arr[i], x <= 10⁴ 
#  
#  Related Topics 数组 双指针 二分查找 排序 堆（优先队列） 👍 319 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # 二分法，始终对长度为k的连续子数组进行操作，最终确定起点位置即可，即左端点
        n = len(arr)
        # 最大的起点为n-k，这样才能保证选取长度为k的连续子数组
        left, right = 0, n - k
        while left < right:
            mid = (left + right) // 2
            # mid与mid+k分别为当前的左右端点
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left:left + k]
# leetcode submit region end(Prohibit modification and deletion)
