# 累加数 是一个字符串，组成它的数字可以形成累加序列。 
# 
#  一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，序列中的每个后续数字必须是它之前两个数字之和。 
# 
#  给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。 
# 
#  说明：累加序列里的数，除数字 0 之外，不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入："112358"
# 输出：true 
# 解释：累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
#  
# 
#  示例 2： 
# 
#  
# 输入："199100199"
# 输出：true 
# 解释：累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num.length <= 35 
#  num 仅由数字（0 - 9）组成 
#  
# 
#  
# 
#  进阶：你计划如何处理由过大的整数输入导致的溢出? 
#  Related Topics 字符串 回溯 👍 354 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        if n < 3: return False

        def check(p1, p2, j):
            while j < n:
                p = str(int(p1) + int(p2))
                if num[j:j + len(p)] != p:
                    return False
                j += len(p)
                p1, p2 = p2, p
            return True

        for i in range(1, n // 2 + 1) if num[0] != "0" else [1]:
            for j in range(i + 1, n) if num[i] != "0" else [i + 1]:
                p1 = num[:i]
                p2 = num[i:j]
                if check(p1, p2, j):
                    return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
