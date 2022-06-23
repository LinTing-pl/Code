# 定义一个函数 f(s)，统计 s 中（按字典序比较）最小字母的出现频次 ，其中 s 是一个非空字符串。 
# 
#  例如，若 s = "dcce"，那么 f(s) = 2，因为字典序最小字母是 "c"，它出现了 2 次。 
# 
#  现在，给你两个字符串数组待查表 queries 和词汇表 words 。对于每次查询 queries[i] ，需统计 words 中满足 f(
# queries[i]) < f(W) 的 词的数目 ，W 表示词汇表 words 中的每个词。 
# 
#  请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是第 i 次查询的结果。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：queries = ["cbd"], words = ["zaaaz"]
# 输出：[1]
# 解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。
#  
# 
#  示例 2： 
# 
#  
# 输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# 输出：[1,2]
# 解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= queries.length <= 2000 
#  1 <= words.length <= 2000 
#  1 <= queries[i].length, words[i].length <= 10 
#  queries[i][j]、words[i][j] 都由小写英文字母组成 
#  
#  Related Topics 数组 哈希表 字符串 二分查找 排序 👍 51 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """

        def f(s):
            l = [0] * 26
            for ss in s:
                l[ord(ss) - ord('a')] += 1
            for i in range(26):
                if l[i] > 0:
                    return l[i]

        def biset(ww, x):
            i = 0
            j = n_w - 1
            while i < j:
                mid = i + (j - i) // 2
                if ww[mid] > x:
                    j = mid - 1
                else:
                    i = mid + 1
            # 找到的可能>x，也可能<=x，当<=x时 根据后面的n_w - t，这里要返回第一个大于x的下标，所以 i+1
            if ww[i] > x:
                return i
            else:
                return i + 1

        n_w = len(words)
        ww = [0] * n_w
        for i in range(n_w):
            ww[i] = f(words[i])
        ww.sort()
        ans = list()
        for i in range(len(queries)):
            t = biset(ww, f(queries[i]))
            ans.append(n_w - t)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
