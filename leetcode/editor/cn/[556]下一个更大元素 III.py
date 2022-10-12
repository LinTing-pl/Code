# 给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。 
# 
#  注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12
# 输出：21
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 21
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2³¹ - 1 
#  
#  Related Topics 数学 双指针 字符串 👍 204 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n, stack = list(str(n)), []
        for i in range(len(n) - 1, -1, -1):
            j = -1
            while stack and n[stack[-1]] > n[i]:  # 单调递增栈
                j = stack.pop()  # 找到栈内最小的大于当前元素的值
            if j >= 0:
                tmp = n[i]
                n[i] = n[j]
                n[j] = tmp  # 调换找到的值
                n = n[:i + 1] + sorted(n[i + 1:])  # 后面的值重排
                n = int(''.join(n))
                return n if n <= 2**31-1 else -1
            stack.append(i)
        return -1
# leetcode submit region end(Prohibit modification and deletion)
