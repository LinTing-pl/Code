# 给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。 
# 
#  在执行上述操作后，返回包含相同字母的最长子字符串的长度。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ABAB", k = 2
# 输出：4
# 解释：用两个'A'替换为两个'B',反之亦然。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "AABABBA", k = 1
# 输出：4
# 解释：
# 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
# 子串 "BBBB" 有最长重复字母, 答案为 4。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s 仅由大写英文字母组成 
#  0 <= k <= s.length 
#  
#  Related Topics 哈希表 字符串 滑动窗口 👍 606 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        num = [0] * 26
        n = len(s)
        maxn = left = right = 0
        while right < n:
            num[ord(s[right]) - ord("A")] += 1
            maxn = max(maxn, num[ord(s[right]) - ord("A")])
            if right - left + 1 - maxn > k:
                num[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1
        return right - left
# leetcode submit region end(Prohibit modification and deletion)
