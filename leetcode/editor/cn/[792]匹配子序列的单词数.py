# 给定字符串 s 和字符串数组 words, 返回 words[i] 中是s的子序列的单词个数 。 
# 
#  字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。 
# 
#  
#  例如， “ace” 是 “abcde” 的子序列。 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abcde", words = ["a","bb","acd","ace"]
# 输出: 3
# 解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。
#  
# 
#  Example 2: 
# 
#  
# 输入: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# 输出: 2
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length <= 5 * 10⁴ 
#  1 <= words.length <= 5000 
#  1 <= words[i].length <= 50 
#  words[i]和 s 都只由小写字母组成。 
#  
#  Related Topics 字典树 哈希表 字符串 排序 👍 201 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        heads = [[] for _ in range(26)]
        for word in words:
            it = iter(word)
            heads[ord(next(it)) - ord('a')].append(it)

        for letter in s:
            letter_index = ord(letter) - ord('a')
            old_bucket = heads[letter_index]
            heads[letter_index] = []

            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                if nxt:
                    heads[ord(nxt) - ord('a')].append(it)
                else:
                    ans += 1

        return ans
# leetcode submit region end(Prohibit modification and deletion)
