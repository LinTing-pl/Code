# 给你一个二进制串 s （一个只包含 0 和 1 的字符串），我们可以将 s 分割成 3 个 非空 字符串 s1, s2, s3 （s1 + s2 + s3 
# = s）。 
# 
#  请你返回分割 s 的方案数，满足 s1，s2 和 s3 中字符 '1' 的数目相同。 
# 
#  由于答案可能很大，请将它对 10^9 + 7 取余后返回。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "10101"
# 输出：4
# 解释：总共有 4 种方法将 s 分割成含有 '1' 数目相同的三个子字符串。
# "1|010|1"
# "1|01|01"
# "10|10|1"
# "10|1|01"
#  
# 
#  示例 2： 
# 
#  输入：s = "1001"
# 输出：0
#  
# 
#  示例 3： 
# 
#  输入：s = "0000"
# 输出：3
# 解释：总共有 3 种分割 s 的方法。
# "0|0|00"
# "0|00|0"
# "00|0|0"
#  
# 
#  示例 4： 
# 
#  输入：s = "100100010100110"
# 输出：12
#  
# 
#  
# 
#  提示： 
# 
#  
#  s[i] == '0' 或者 s[i] == '1' 
#  3 <= s.length <= 10^5 
#  
#  Related Topics 数学 字符串 👍 9 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        MODULO = 1000000007

        ones = list()
        n = len(s)
        for i, digit in enumerate(s):
            if digit == "1":
                ones.append(i)

        m = len(ones)
        if m % 3 != 0:
            return 0

        if m == 0:
            ways = (n - 1) * (n - 2) // 2
            return ways % MODULO
        else:
            index1, index2 = m // 3, m // 3 * 2
            count1 = ones[index1] - ones[index1 - 1]
            count2 = ones[index2] - ones[index2 - 1]
            ways = count1 * count2
            return ways % MODULO
# leetcode submit region end(Prohibit modification and deletion)
