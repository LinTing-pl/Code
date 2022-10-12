# 你有 n 个工作和 m 个工人。给定三个数组： difficulty, profit 和 worker ，其中: 
# 
#  
#  difficulty[i] 表示第 i 个工作的难度，profit[i] 表示第 i 个工作的收益。 
#  worker[i] 是第 i 个工人的能力，即该工人只能完成难度小于等于 worker[i] 的工作。 
#  
# 
#  每个工人 最多 只能安排 一个 工作，但是一个工作可以 完成多次 。 
# 
#  
#  举个例子，如果 3 个工人都尝试完成一份报酬为 $1 的同样工作，那么总收益为 $3 。如果一个工人不能完成任何工作，他的收益为 $0 。 
#  
# 
#  返回 在把工人分配到工作岗位后，我们所能获得的最大利润 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
# 输出: 100 
# 解释: 工人被分配的工作难度是 [4,4,6,6] ，分别获得 [20,20,30,30] 的收益。 
# 
#  示例 2: 
# 
#  
# 输入: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
# 输出: 0 
# 
#  
# 
#  提示: 
# 
#  
#  n == difficulty.length 
#  n == profit.length 
#  m == worker.length 
#  1 <= n, m <= 10⁴ 
#  1 <= difficulty[i], profit[i], worker[i] <= 10⁵ 
#  
#  Related Topics 贪心 数组 双指针 二分查找 排序 👍 84 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = zip(difficulty, profit)
        jobs.sort()
        ans = i = best = 0
        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans
# leetcode submit region end(Prohibit modification and deletion)
