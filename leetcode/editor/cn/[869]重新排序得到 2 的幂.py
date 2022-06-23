# 给定正整数 n ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。 
# 
#  如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 1
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 10
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10⁹ 
#  
#  Related Topics 数学 计数 枚举 排序 👍 148 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
NUMS = set(str(sorted(str(1 << i))) for i in range(30))


class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return str(sorted(str(n))) in NUMS
# leetcode submit region end(Prohibit modification and deletion)
