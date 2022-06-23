# 给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。 
# 
#  示例 1： 
# 
#  输入: num = 1775(110111011112)
# 输出: 8
#  
# 
#  示例 2： 
# 
#  输入: num = 7(01112)
# 输出: 4
#  
#  Related Topics 位运算 动态规划 👍 73 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseBits(self, num):
        """
        :type num: int
        :rtype: int
        """
        pre, cur = 0, 0
        res = 1
        for i in range(32):
            if num & (1 << i):
                cur += 1
            else:
                res = max(res, pre + cur)
                pre = cur + 1
                cur = 0
        res = max(res, pre + cur)
        return res
# leetcode submit region end(Prohibit modification and deletion)
