# 给你一个字符串 path，其中 path[i] 的值可以是 'N'、'S'、'E' 或者 'W'，分别表示向北、向南、向东、向西移动一个单位。 
# 
#  你从二维平面上的原点 (0, 0) 处开始出发，按 path 所指示的路径行走。 
# 
#  如果路径在任何位置上与自身相交，也就是走到之前已经走过的位置，请返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：path = "NES"
# 输出：false 
# 解释：该路径没有在任何位置相交。 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：path = "NESWW"
# 输出：true
# 解释：该路径经过原点两次。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= path.length <= 10⁴ 
#  path[i] 为 'N'、'S'、'E' 或 'W' 
#  
#  Related Topics 哈希表 字符串 👍 34 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        dirs = {"N": (-1, 0),
                "S": (1, 0),
                "W": (0, -1),
                "E": (0, 1), }
        x, y = 0, 0
        vis = {(x, y)}
        for ch in path:
            dx, dy = dirs[ch]
            x, y = x + dx, y + dy
            if (x, y) in vis:
                return True
            vis.add((x, y))
        return False
# leetcode submit region end(Prohibit modification and deletion)
