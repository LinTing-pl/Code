# 给定正整数 k ，你需要找出可以被 k 整除的、仅包含数字 1 的最 小 正整数 n 的长度。 
# 
#  返回 n 的长度。如果不存在这样的 n ，就返回-1。 
# 
#  注意： n 不符合 64 位带符号整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：k = 1
# 输出：1
# 解释：最小的答案是 n = 1，其长度为 1。 
# 
#  示例 2： 
# 
#  
# 输入：k = 2
# 输出：-1
# 解释：不存在可被 2 整除的正整数 n 。 
# 
#  示例 3： 
# 
#  
# 输入：k = 3
# 输出：3
# 解释：最小的答案是 n = 111，其长度为 3。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= 10⁵ 
#  
#  Related Topics 哈希表 数学 👍 51 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        # 如果K的因子中含有 2, 5 , 返回-1
        if k % 2 == 0 or k % 5 == 0:
            return -1
        # 相当于  1   除以  9K
        # 计算循环节的长度
        res = 1
        y = 9 * k
        x = 10 % y
        while x != 1:
            res += 1
            x = (10 * x) % y
        return res
# leetcode submit region end(Prohibit modification and deletion)
