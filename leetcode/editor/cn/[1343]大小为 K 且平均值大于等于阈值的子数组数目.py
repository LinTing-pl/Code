# 给你一个整数数组 arr 和两个整数 k 和 threshold 。 
# 
#  请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# 输出：3
# 解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （
# threshold 的值)。
#  
# 
#  示例 2： 
# 
#  
# 输入：arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# 输出：6
# 解释：前 6 个长度为 3 的子数组平均值都大于 5 。注意平均值不是整数。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10⁵ 
#  1 <= arr[i] <= 10⁴ 
#  1 <= k <= arr.length 
#  0 <= threshold <= 10⁴ 
#  
#  Related Topics 数组 滑动窗口 👍 38 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        target=k*threshold
        cur=sum(arr[:k])
        ans=0
        n=len(arr)
        for i in range(k,n):
            if cur>=target:
                ans+=1
            cur+=arr[i]
            cur-=arr[i-k]
        if cur>=target:
            ans+=1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
a=Solution()
a.numOfSubarrays([2,2,2,2,5,5,5,8],3,4)