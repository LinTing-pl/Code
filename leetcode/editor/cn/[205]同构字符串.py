# 给定两个字符串 s 和 t ，判断它们是否是同构的。 
# 
#  如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。 
# 
#  每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入：s = "egg", t = "add"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "foo", t = "bar"
# 输出：false 
# 
#  示例 3： 
# 
#  
# 输入：s = "paper", t = "title"
# 输出：true 
# 
#  
# 
#  提示： 
# 
#  
# 
#  
#  1 <= s.length <= 5 * 10⁴ 
#  t.length == s.length 
#  s 和 t 由任意有效的 ASCII 字符组成 
#  
#  Related Topics 哈希表 字符串 👍 433 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s2t = {}
        t2s = {}
        l = len(s)
        for i in range(l):
            x = s[i]
            y = t[i]
            if x in s2t.keys() and s2t.get(x) != y or y in t2s.keys() and t2s.get(y) != x:
                return False
            s2t[x] = y
            t2s[y] = x
        return True
# leetcode submit region end(Prohibit modification and deletion)
