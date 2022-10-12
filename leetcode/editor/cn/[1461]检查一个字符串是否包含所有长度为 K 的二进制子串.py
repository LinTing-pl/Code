# 给你一个二进制字符串 s 和一个整数 k 。如果所有长度为 k 的二进制字符串都是 s 的子串，请返回 true ，否则请返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "00110110", k = 2
# 输出：true
# 解释：长度为 2 的二进制串包括 "00"，"01"，"10" 和 "11"。它们分别是 s 中下标为 0，1，3，2 开始的长度为 2 的子串。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "0110", k = 1
# 输出：true
# 解释：长度为 1 的二进制串包括 "0" 和 "1"，显然它们都是 s 的子串。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "0110", k = 2
# 输出：false
# 解释：长度为 2 的二进制串 "00" 没有出现在 s 中。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 5 * 10⁵ 
#  s[i] 不是'0' 就是 '1' 
#  1 <= k <= 20 
#  
#  Related Topics 位运算 哈希表 字符串 哈希函数 滚动哈希 👍 45 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s) < (1 << k) + k - 1:
            return False

        exists = set(s[i:i + k] for i in range(len(s) - k + 1))
        return len(exists) == (1 << k)
# leetcode submit region end(Prohibit modification and deletion)
