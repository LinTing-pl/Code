# 给出非负整数数组 A ，返回两个非重叠（连续）子数组中元素的最大和，子数组的长度分别为 L 和 M。（这里需要澄清的是，长为 L 的子数组可以出现在长为 
# M 的子数组之前或之后。） 
# 
#  从形式上看，返回最大的 V，而 V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... +
#  A[j+M-1]) 并满足下列条件之一： 
# 
#  
# 
#  
#  0 <= i < i + L - 1 < j < j + M - 1 < A.length, 或 
#  0 <= j < j + M - 1 < i < i + L - 1 < A.length. 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
# 输出：20
# 解释：子数组的一种选择中，[9] 长度为 1，[6,5] 长度为 2。
#  
# 
#  示例 2： 
# 
#  
# 输入：A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
# 输出：29
# 解释：子数组的一种选择中，[3,8,1] 长度为 3，[8,9] 长度为 2。
#  
# 
#  示例 3： 
# 
#  
# 输入：A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
# 输出：31
# 解释：子数组的一种选择中，[5,6,0,9] 长度为 4，[0,3,8] 长度为 3。 
# 
#  
# 
#  提示： 
# 
#  
#  L >= 1 
#  M >= 1 
#  L + M <= A.length <= 1000 
#  0 <= A[i] <= 1000 
#  
#  Related Topics 数组 动态规划 滑动窗口 👍 129 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        n = len(nums)
        presum = [0 for _ in range(n + 1)]
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]
        maxL = presum[firstLen]
        maxM = presum[secondLen]
        res = presum[firstLen + secondLen]
        for r in range(firstLen + secondLen + 1, n + 1):  # 当前区间的r端（包含在前面，为一个有效区间的末位）
            # L,M|r(r含)                         #其他情况已经包含在内了 有点像dp的思想
            maxL = max(maxL, presum[r - secondLen] - presum[r - secondLen - firstLen])
            curM = presum[r] - presum[r - secondLen]
            res_LM = maxL + curM
            # M,L|r(r含)
            curL = presum[r] - presum[r - firstLen]
            maxM = max(maxM, presum[r - firstLen] - presum[r - firstLen - secondLen])
            res_ML = maxM + curL

            res = max(res, res_LM, res_ML)

        return res
# leetcode submit region end(Prohibit modification and deletion)
