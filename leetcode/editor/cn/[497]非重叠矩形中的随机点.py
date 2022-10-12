# 给定一个由非重叠的轴对齐矩形的数组 rects ，其中 rects[i] = [ai, bi, xi, yi] 表示 (ai, bi) 是第 i 个矩形的左
# 下角点，(xi, yi) 是第 i 个矩形的右上角角点。设计一个算法来挑选一个随机整数点内的空间所覆盖的一个给定的矩形。矩形周长上的一个点包含在矩形覆盖的空间中
# 。 
# 
#  在一个给定的矩形覆盖的空间内任何整数点都有可能被返回。 
# 
#  请注意 ，整数点是具有整数坐标的点。 
# 
#  实现 Solution 类: 
# 
#  
#  Solution(int[][] rects) 用给定的矩形数组 rects 初始化对象。 
#  int[] pick() 返回一个随机的整数点 [u, v] 在给定的矩形所覆盖的空间内。 
#  
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入: 
# ["Solution","pick","pick","pick","pick","pick"]
# [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
# 输出: 
# [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]
# 
# 解释：
# Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
# solution.pick(); // 返回 [1, -2]
# solution.pick(); // 返回 [1, -1]
# solution.pick(); // 返回 [-1, -2]
# solution.pick(); // 返回 [-2, -2]
# solution.pick(); // 返回 [0, 0] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= rects.length <= 100 
#  rects[i].length == 4 
#  -10⁹ <= ai < xi <= 10⁹ 
#  -10⁹ <= bi < yi <= 10⁹ 
#  xi - ai <= 2000 
#  yi - bi <= 2000 
#  所有的矩形不重叠。 
#  pick 最多被调用 10⁴ 次。 
#  
# 
#  
#  Related Topics 水塘抽样 数学 二分查找 有序集合 前缀和 随机化 👍 54 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from random import randrange


class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects

    def pick(self):
        """
        :rtype: List[int]
        """
        result = []
        count = 0
        for rect in self.rects:
            x1, y1, x2, y2 = rect[0], rect[1], rect[2], rect[3]
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            count += area  # 当前点的总数
            if randrange(count) < area:  # 水塘抽样判断条件
                result = [randrange(x1, x2 + 1), randrange(y1, y2 + 1)]
        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
# leetcode submit region end(Prohibit modification and deletion)
