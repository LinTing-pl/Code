# 给你四个整数：n 、a 、b 、c ，请你设计一个算法来找出第 n 个丑数。 
# 
#  丑数是可以被 a 或 b 或 c 整除的 正整数 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3, a = 2, b = 3, c = 5
# 输出：4
# 解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。 
# 
#  示例 2： 
# 
#  
# 输入：n = 4, a = 2, b = 3, c = 4
# 输出：6
# 解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 5, a = 2, b = 11, c = 13
# 输出：10
# 解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。
#  
# 
#  示例 4： 
# 
#  
# 输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
# 输出：1999999984
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n, a, b, c <= 10^9 
#  1 <= a * b * c <= 10^18 
#  本题结果在 [1, 2 * 10^9] 的范围内 
#  
#  Related Topics 数学 二分查找 数论 👍 109 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from fractions import gcd


class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """

        def Lcm3(x, y, z):
            a = (x * y) // gcd(x, y)
            return (a * z) // gcd(a, z)

        '''
        计算有多少个丑数小于等于x
        + x整除a,b,c -整除ab,bc,ac最小公倍数 +整除abc最小公倍数 即为所求
        '''

        def uglynum(x):
            return x // a + x // b + x // c - x // (a * b // gcd(a, b)) - x // (a * c // gcd(a, c)) - x // (
                        b * c // gcd(b, c)) + x // Lcm3(a, b, c)

        '''
        二分搜索，注意只要uglynum(mid)<n left就=mid+1 所以最后得到的left就是所求
        例如测试用例2中  a=2,b=3,c=4
        括号中为丑数                    1,(2),(3),(4),5,(6),7,(8)
        小于等于它们的丑数个数分别为     0, 1 , 2 , 3 ,3, 4, 4, 5 
        若n==4
        如果uglynum(mid)<4 则left一定能直接取到6而不是7
        '''
        left = 1
        right = n * min(a, b, c)
        while left < right:
            mid = (left + right) // 2
            if uglynum(mid) < n:
                left = mid + 1
            else:
                right = mid
        return left
# leetcode submit region end(Prohibit modification and deletion)
