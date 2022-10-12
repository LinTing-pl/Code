# 如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。 
# 
#  给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s： 
# 
#  
#  s 是一个尽可能长的快乐字符串。 
#  s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。 
#  s 中只含有 'a'、'b' 、'c' 三种字母。 
#  
# 
#  如果不存在这样的字符串 s ，请返回一个空字符串 ""。 
# 
#  
# 
#  示例 1： 
# 
#  输入：a = 1, b = 1, c = 7
# 输出："ccaccbcc"
# 解释："ccbccacc" 也是一种正确答案。
#  
# 
#  示例 2： 
# 
#  输入：a = 2, b = 2, c = 1
# 输出："aabbc"
#  
# 
#  示例 3： 
# 
#  输入：a = 7, b = 1, c = 0
# 输出："aabaa"
# 解释：这是该测试用例的唯一正确答案。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= a, b, c <= 100 
#  a + b + c > 0 
#  
#  Related Topics 贪心 字符串 堆（优先队列） 👍 199 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        ans = []
        cnt = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            cnt.sort(key=lambda x: -x[0])
            hasNext = False
            for i, (c, ch) in enumerate(cnt):
                if c <= 0:
                    break
                if len(ans) >= 2 and ans[-2] == ch and ans[-1] == ch:
                    continue
                hasNext = True
                ans.append(ch)
                cnt[i][0] -= 1
                break
            if not hasNext:
                return ''.join(ans)
# leetcode submit region end(Prohibit modification and deletion)
