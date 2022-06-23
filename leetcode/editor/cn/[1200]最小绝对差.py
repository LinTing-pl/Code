# 给你个整数数组 arr，其中每个元素都 不相同。 
# 
#  请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [4,2,1,3]
# 输出：[[1,2],[2,3],[3,4]]
#  
# 
#  示例 2： 
# 
#  输入：arr = [1,3,6,10,15]
# 输出：[[1,3]]
#  
# 
#  示例 3： 
# 
#  输入：arr = [3,8,-10,23,19,-4,-14,27]
# 输出：[[-14,-10],[19,23],[23,27]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= arr.length <= 10^5 
#  -10^6 <= arr[i] <= 10^6 
#  
#  Related Topics 数组 排序 👍 59 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        diff_min, res, n = float("inf"), [], len(arr)
        for i in range(n - 1):
            if (arr[i + 1] - arr[i]) < diff_min:
                res = []
                res.append([arr[i], arr[i + 1]])
                diff_min = arr[i + 1] - arr[i]
            elif arr[i + 1] - arr[i] == diff_min:
                res.append([arr[i], arr[i + 1]])
        return res
# leetcode submit region end(Prohibit modification and deletion)
