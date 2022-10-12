# 给你一个数组 events，其中 events[i] = [startDayi, endDayi] ，表示会议 i 开始于 startDayi ，结束于 
# endDayi 。 
# 
#  你可以在满足 startDayi <= d <= endDayi 中的任意一天 d 参加会议 i 。注意，一天只能参加一个会议。 
# 
#  请你返回你可以参加的 最大 会议数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：events = [[1,2],[2,3],[3,4]]
# 输出：3
# 解释：你可以参加所有的三个会议。
# 安排会议的一种方案如上图。
# 第 1 天参加第一个会议。
# 第 2 天参加第二个会议。
# 第 3 天参加第三个会议。
#  
# 
#  示例 2： 
# 
#  
# 输入：events= [[1,2],[2,3],[3,4],[1,2]]
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= events.length <= 10⁵ 
#  events[i].length == 2 
#  1 <= startDayi <= endDayi <= 10⁵ 
#  
#  Related Topics 贪心 数组 堆（优先队列） 👍 211 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        heap = []
        T = 100010
        j = 0
        n = len(events)
        res = 0
        # 枚举每一时刻
        for i in range(1, T):
            # 删掉过期会议
            while heap and heap[0] < i: heapq.heappop(heap)
            # 加入可选会议
            while j < n and events[j][0] == i:
                heapq.heappush(heap, events[j][1])
                j += 1
            # 参加最先结束的会议
            if heap:
                heapq.heappop(heap)
                res += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
