# 给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。 
# 
#  初始化 A 和 B 的元素数量分别为 m 和 n。 
# 
#  示例: 
# 
#  输入:
# A = [1,2,3,0,0,0], m = 3
# B = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6] 
# 
#  说明: 
# 
#  
#  A.length == n + m 
#  
#  Related Topics 数组 双指针 排序 👍 139 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        for i in range(n):
            A[m] = B[i]
            m += 1
        A.sort()
# leetcode submit region end(Prohibit modification and deletion)
