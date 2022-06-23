# 给你两个整数 n 和 start。你的任务是返回任意 (0,1,2,,...,2^n-1) 的排列 p，并且满足： 
# 
#  
#  p[0] = start 
#  p[i] 和 p[i+1] 的二进制表示形式只有一位不同 
#  p[0] 和 p[2^n -1] 的二进制表示形式也只有一位不同 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 2, start = 3
# 输出：[3,2,0,1]
# 解释：这个排列的二进制表示是 (11,10,00,01)
#      所有的相邻元素都有一位是不同的，另一个有效的排列是 [3,1,0,2]
#  
# 
#  示例 2： 
# 
#  输出：n = 3, start = 2
# 输出：[2,6,7,5,4,0,1,3]
# 解释：这个排列的二进制表示是 (010,110,111,101,100,000,001,011)
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 16 
#  0 <= start < 2^n 
#  
#  Related Topics 位运算 数学 回溯 👍 42 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        N = pow(2, n)
        res = [0] * N
        for i in range(N):
            res[i] = i ^ (i >> 1)  # 二进制码到格雷码(gray code)
        # start的格雷码(gray code)到二进制码
        p = 2 << (n - 1)
        start_bin = 0
        while p:
            start_bin |= (start_bin >> 1 & p) ^ (start & p)
            p >>= 1
        return res[start_bin:] + res[:start_bin]
# leetcode submit region end(Prohibit modification and deletion)
