# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。 
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
# 输入: rowIndex = 3
# 输出: [1,3,3,1]
#  
# 
#  示例 2: 
# 
#  
# 输入: rowIndex = 0
# 输出: [1]
#  
# 
#  示例 3: 
# 
#  
# 输入: rowIndex = 1
# 输出: [1,1]
#  
# 
#  
# 
#  提示: 
# 
#  
#  0 <= rowIndex <= 33 
#  
# 
#  
# 
#  进阶： 
# 
#  你可以优化你的算法到 O(rowIndex) 空间复杂度吗？ 
#  Related Topics 数组 动态规划 👍 370 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        r = [[1], [1, 1]]
        for i in range(2, rowIndex+1):
            a = [1, 1]
            for j in range(1, i):
                a.insert(j, r[i - 1][j] + r[i - 1][j - 1])
            r.append(a)
        return r[rowIndex]


# leetcode submit region end(Prohibit modification and deletion)
a = Solution()
print(a.getRow(3))
