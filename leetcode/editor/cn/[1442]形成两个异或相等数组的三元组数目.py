# 给你一个整数数组 arr 。 
# 
#  现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。 
# 
#  a 和 b 定义如下： 
# 
#  
#  a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] 
#  b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k] 
#  
# 
#  注意：^ 表示 按位异或 操作。 
# 
#  请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [2,3,1,6,7]
# 输出：4
# 解释：满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
#  
# 
#  示例 2： 
# 
#  输入：arr = [1,1,1,1,1]
# 输出：10
#  
# 
#  示例 3： 
# 
#  输入：arr = [2,3]
# 输出：0
#  
# 
#  示例 4： 
# 
#  输入：arr = [1,3,5,7,9]
# 输出：3
#  
# 
#  示例 5： 
# 
#  输入：arr = [7,11,12,9,5,2,7,17,22]
# 输出：8
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 300 
#  1 <= arr[i] <= 10^8 
#  
#  Related Topics 位运算 数组 哈希表 数学 前缀和 👍 207 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        s = [0]
        for val in arr:
            s.append(s[-1] ^ val)

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    if s[i] == s[k + 1]:
                        ans += 1

        return ans
# leetcode submit region end(Prohibit modification and deletion)
