# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。 
# 
#  在「杨辉三角」中，每个数是它左上方和右上方的数的和。 
# 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#  
# 
#  示例 2: 
# 
#  
# 输入: numRows = 1
# 输出: [[1]]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= numRows <= 30 
#  
#  Related Topics 数组 动态规划 👍 700 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        r = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return r
        for i in range(2, numRows):
            a = [1, 1]
            for j in range(1, i):
                a.insert(j, r[i - 1][j] + r[i - 1][j - 1])
            r.append(a)
        return r


# leetcode submit region end(Prohibit modification and deletion)
a = Solution()
a.generate(5)
