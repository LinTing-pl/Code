# n 名士兵站成一排。每个士兵都有一个 独一无二 的评分 rating 。 
# 
#  每 3 个士兵可以组成一个作战单位，分组规则如下： 
# 
#  
#  从队伍中选出下标分别为 i、j、k 的 3 名士兵，他们的评分分别为 rating[i]、rating[j]、rating[k] 
#  作战单位需满足： rating[i] < rating[j] < rating[k] 或者 rating[i] > rating[j] > rating[
# k] ，其中 0 <= i < j < k < n 
#  
# 
#  请你返回按上述条件可以组建的作战单位数量。每个士兵都可以是多个作战单位的一部分。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：rating = [2,5,3,4,1]
# 输出：3
# 解释：我们可以组建三个作战单位 (2,3,4)、(5,4,1)、(5,3,1) 。
#  
# 
#  示例 2： 
# 
#  
# 输入：rating = [2,1,3]
# 输出：0
# 解释：根据题目条件，我们无法组建作战单位。
#  
# 
#  示例 3： 
# 
#  
# 输入：rating = [1,2,3,4]
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == rating.length 
#  3 <= n <= 1000 
#  1 <= rating[i] <= 10^5 
#  rating 中的元素都是唯一的 
#  
#  Related Topics 树状数组 数组 动态规划 👍 103 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        n = len(rating)
        ans = 0
        # 枚举三元组中的 j
        for j in range(1, n - 1):
            iless = imore = kless = kmore = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    iless += 1
                # 注意这里不能直接写成 else
                # 因为可能有评分相同的情况
                elif rating[i] > rating[j]:
                    imore += 1
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    kless += 1
                elif rating[k] > rating[j]:
                    kmore += 1
            ans += iless * kmore + imore * kless
        return ans
# leetcode submit region end(Prohibit modification and deletion)
