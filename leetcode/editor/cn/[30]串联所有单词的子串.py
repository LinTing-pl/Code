# 给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。 
# 
#  注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "barfoothefoobarman", words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# 输出：[6,9,12]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 由小写英文字母组成 
#  1 <= words.length <= 5000 
#  1 <= words[i].length <= 30 
#  words[i] 由小写英文字母组成 
#  
#  Related Topics 哈希表 字符串 滑动窗口 👍 607 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s: return []
        hs = {}
        r = []
        for word in words:
            hs[word] = hs.get(word, 0) + 1
        slen, wlen = len(s), len(words[0])
        tlen = len(words) * wlen
        for i in range(slen - tlen + 1):
            rhs = hs.copy()
            count = i + wlen
            while s[count - wlen:count] in rhs and rhs[s[count - wlen:count]] > 0:
                rhs[s[count - wlen:count]] -= 1
                count += wlen
            if sum(rhs.values()) == 0:
                r.append(i)
        return r
# leetcode submit region end(Prohibit modification and deletion)
