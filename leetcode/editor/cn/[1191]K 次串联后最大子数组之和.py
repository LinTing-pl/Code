# 给定一个整数数组 arr 和一个整数 k ，通过重复 k 次来修改数组。 
# 
#  例如，如果 arr = [1, 2] ， k = 3 ，那么修改后的数组将是 [1, 2, 1, 2, 1, 2] 。 
# 
#  返回修改后的数组中的最大的子数组之和。注意，子数组长度可以是 0，在这种情况下它的总和也是 0。 
# 
#  由于 结果可能会很大，需要返回的 10⁹ + 7 的 模 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [1,2], k = 3
# 输出：9
#  
# 
#  示例 2： 
# 
#  
# 输入：arr = [1,-2,1], k = 5
# 输出：2
#  
# 
#  示例 3： 
# 
#  
# 输入：arr = [-1,-2], k = 7
# 输出：0
#  
# 
#  
# 
#  提示： 
#  
# 
#  
#  1 <= arr.length <= 10⁵ 
#  1 <= k <= 10⁵ 
#  -10⁴ <= arr[i] <= 10⁴ 
#  
#  Related Topics 数组 动态规划 👍 94 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # 分三种情况
        # k = 1: 同 53 题 注意 答案非负数
        # k = 2: 最大前缀和 + 最大后缀和， 其实两个合起来同(1)
        # k > 2: sum < 0, 同(2)；否则(2)答案 + sum * (k - 2)
        a = arr * min(k, 2)
        ans = pre = 0  # 答案最小为 0
        for i, x in enumerate(a):
            pre = max(x, pre + x)
            ans = max(ans, pre)
        s = sum(arr)
        if s > 0 and k > 2:
            ans = max(ans, s * (k - 2) + ans)
        return ans % 1000000007
# leetcode submit region end(Prohibit modification and deletion)
