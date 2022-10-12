# 给定一个字符串 s ，检查是否能重新排布其中的字母，使得两相邻的字符不同。 
# 
#  返回 s 的任意可能的重新排列。若不可行，返回空字符串 "" 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "aab"
# 输出: "aba"
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "aaab"
# 输出: ""
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length <= 500 
#  s 只包含小写字母 
#  
#  Related Topics 贪心 哈希表 字符串 计数 排序 堆（优先队列） 👍 408 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
import heapq


class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        res = []
        heap = list(s)
        dic = collections.Counter(heap)
        maxdic = max(dic.values())
        if len(s) % 2 == 0 and maxdic > len(s) // 2:
            return ""
        if len(s) % 2 == 1 and maxdic > len(s) // 2 + 1:
            return ""

        heap = [(-x[1], x[0]) for x in dic.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            _, string1 = heapq.heappop(heap)
            _, string2 = heapq.heappop(heap)
            res.extend([string1, string2])
            dic[string1] -= 1
            dic[string2] -= 1
            if dic[string1] > 0:
                heapq.heappush(heap, (-dic[string1], string1))
            if dic[string2] > 0:
                heapq.heappush(heap, (-dic[string2], string2))
        if heap:
            res.append(heap[0][1])
        return "".join(res)
# leetcode submit region end(Prohibit modification and deletion)
