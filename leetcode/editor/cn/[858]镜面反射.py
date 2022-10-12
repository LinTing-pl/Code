# 有一个特殊的正方形房间，每面墙上都有一面镜子。除西南角以外，每个角落都放有一个接受器，编号为 0， 1，以及 2。 
# 
#  正方形房间的墙壁长度为 p，一束激光从西南角射出，首先会与东墙相遇，入射点到接收器 0 的距离为 q 。 
# 
#  返回光线最先遇到的接收器的编号（保证光线最终会遇到一个接收器）。 
# 
#  
# 
#  示例： 
# 
#  
# 输入： p = 2, q = 1
# 输出： 2
# 解释： 这条光线在第一次被反射回左边的墙时就遇到了接收器 2 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= p <= 1000 
#  0 <= q <= p 
#  
#  Related Topics 几何 数学 👍 68 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        from fractions import Fraction as F

        x = y = 0
        rx, ry = p, q
        targets = [(p, 0), (p, p), (0, p)]

        while (x, y) not in targets:
            # Want smallest t so that some x + rx, y + ry is 0 or p
            # x + rxt = 0, then t = -x/rx etc.
            t = float('inf')
            for v in [F(-x, rx), F(-y, ry), F(p - x, rx), F(p - y, ry)]:
                if v > 0: t = min(t, v)

            x += rx * t
            y += ry * t

            # update rx, ry
            if x == p or x == 0:  # bounced from east/west wall, so reflect on y axis
                rx *= -1
            if y == p or y == 0:
                ry *= -1

        return 1 if x == y == p else 0 if x == p else 2
# leetcode submit region end(Prohibit modification and deletion)
