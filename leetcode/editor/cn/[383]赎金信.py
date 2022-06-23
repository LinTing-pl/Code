# 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。 
# 
#  如果可以，返回 true ；否则返回 false 。 
# 
#  magazine 中的每个字符只能在 ransomNote 中使用一次。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：ransomNote = "a", magazine = "b"
# 输出：false
#  
# 
#  示例 2： 
# 
#  
# 输入：ransomNote = "aa", magazine = "ab"
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：ransomNote = "aa", magazine = "aab"
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= ransomNote.length, magazine.length <= 10⁵ 
#  ransomNote 和 magazine 由小写英文字母组成 
#  
#  Related Topics 哈希表 字符串 计数 👍 282 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine): return False
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
# leetcode submit region end(Prohibit modification and deletion)
