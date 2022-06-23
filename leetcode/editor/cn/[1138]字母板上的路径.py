# 我们从一块字母板上的位置 (0, 0) 出发，该坐标对应的字符为 board[0][0]。 
# 
#  在本题里，字母板为board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]，如下所示。 
# 
#  
# 
#  我们可以按下面的指令规则行动： 
# 
#  
#  如果方格存在，'U' 意味着将我们的位置上移一行； 
#  如果方格存在，'D' 意味着将我们的位置下移一行； 
#  如果方格存在，'L' 意味着将我们的位置左移一列； 
#  如果方格存在，'R' 意味着将我们的位置右移一列； 
#  '!' 会把在我们当前位置 (r, c) 的字符 board[r][c] 添加到答案中。 
#  
# 
#  （注意，字母板上只存在有字母的位置。） 
# 
#  返回指令序列，用最小的行动次数让答案和目标 target 相同。你可以返回任何达成目标的路径。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：target = "leet"
# 输出："DDR!UURRR!!DDD!"
#  
# 
#  示例 2： 
# 
#  
# 输入：target = "code"
# 输出："RR!DDRR!UUL!R!"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= target.length <= 100 
#  target 仅含有小写英文字母。 
#  
#  Related Topics 哈希表 字符串 👍 43 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        x, y, d = 0, 0, dict()
        for i in range(26):
            d[chr(i + 97)] = (i // 5, i % 5)
        cur, ans = (0, 0), []
        for c in target:
            nxt = d[c]
            dx, dy = nxt[0] - cur[0], nxt[1] - cur[1]
            if dx < 0: ans += ['U'] * (-dx)
            if dy < 0: ans += ['L'] * (-dy)
            if dx > 0: ans += ['D'] * dx
            if dy > 0: ans += ['R'] * dy
            ans.append('!')
            cur = nxt
        return ''.join(ans)
# leetcode submit region end(Prohibit modification and deletion)
