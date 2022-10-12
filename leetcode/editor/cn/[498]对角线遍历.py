# 给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,4,7,5,3,6,8,9]
#  
# 
#  示例 2： 
# 
#  
# 输入：mat = [[1,2],[3,4]]
# 输出：[1,2,3,4]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n <= 10⁴ 
#  1 <= m * n <= 10⁴ 
#  -10⁵ <= mat[i][j] <= 10⁵ 
#  
#  Related Topics 数组 矩阵 模拟 👍 297 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if len(mat) == 0:
            return result

        m = len(mat)
        n = len(mat[0])
        count = 0  # i+j==count
        while count < m + n - 1:
            # 向右上走，起点在左下
            if count % 2 == 0:
                x = count if (count < m) else (m - 1)
                y = count - x
                while x >= 0 and y <= n - 1:
                    result.append(mat[x][y])
                    x -= 1
                    y += 1
            # 向左下走，起点在右上
            else:
                y = count if (count < n) else (n - 1)
                x = count - y
                while x <= m - 1 and y >= 0:
                    result.append(mat[x][y])
                    x += 1
                    y -= 1
            count += 1
        return result
# leetcode submit region end(Prohibit modification and deletion)
