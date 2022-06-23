# 给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: s = "leetcode"
# 输出: 0
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "loveleetcode"
# 输出: 2
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "aabb"
# 输出: -1
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s 只包含小写字母 
#  
#  Related Topics 队列 哈希表 字符串 计数 👍 515 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hs = {}
        for i in s:
            hs[i] = hs.get(i, 0) + 1
        for i in range(len(s)):
            if hs[s[i]] == 1:
                return i
        return -1
# leetcode submit region end(Prohibit modification and deletion)
