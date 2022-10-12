# 现有一个房间，墙上挂有 n 只已经打开的灯泡和 4 个按钮。在进行了 m 次未知操作后，你需要返回这 n 只灯泡可能有多少种不同的状态。 
# 
#  假设这 n 只灯泡被编号为 [1, 2, 3 ..., n]，这 4 个按钮的功能如下： 
# 
#  
#  将所有灯泡的状态反转（即开变为关，关变为开） 
#  将编号为偶数的灯泡的状态反转 
#  将编号为奇数的灯泡的状态反转 
#  将编号为 3k+1 的灯泡的状态反转（k = 0, 1, 2, ...) 
#  
# 
#  示例 1: 
# 
#  输入: n = 1, m = 1.
# 输出: 2
# 说明: 状态为: [开], [关]
#  
# 
#  示例 2: 
# 
#  输入: n = 2, m = 1.
# 输出: 3
# 说明: 状态为: [开, 关], [关, 开], [关, 关]
#  
# 
#  示例 3: 
# 
#  输入: n = 3, m = 1.
# 输出: 4
# 说明: 状态为: [关, 开, 关], [开, 关, 开], [关, 关, 关], [关, 开, 开].
#  
# 
#  注意： n 和 m 都属于 [0, 1000]. 
#  Related Topics 位运算 深度优先搜索 广度优先搜索 数学 👍 92 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import itertools


class Solution(object):
    def flipLights(self, n, presses):
        """
        :type n: int
        :type presses: int
        :rtype: int
        """
        seen = set()
        for cand in itertools.product((0, 1), repeat=4):
            if sum(cand) % 2 == presses % 2 and sum(cand) <= presses:
                A = []
                for i in range(min(n, 3)):
                    light = 1
                    light ^= cand[0]
                    light ^= cand[1] and i % 2
                    light ^= cand[2] and i % 2 == 0
                    light ^= cand[3] and i % 3 == 0
                    A.append(light)
                seen.add(tuple(A))

        return len(seen)
# leetcode submit region end(Prohibit modification and deletion)
