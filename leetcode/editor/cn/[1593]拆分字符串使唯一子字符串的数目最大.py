# 给你一个字符串 s ，请你拆分该字符串，并返回拆分后唯一子字符串的最大数目。 
# 
#  字符串 s 拆分后可以得到若干 非空子字符串 ，这些子字符串连接后应当能够还原为原字符串。但是拆分出来的每个子字符串都必须是 唯一的 。 
# 
#  注意：子字符串 是字符串中的一个连续字符序列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "ababccc"
# 输出：5
# 解释：一种最大拆分方法为 ['a', 'b', 'ab', 'c', 'cc'] 。像 ['a', 'b', 'a', 'b', 'c', 'cc'] 这样
# 拆分不满足题目要求，因为其中的 'a' 和 'b' 都出现了不止一次。
#  
# 
#  示例 2： 
# 
#  输入：s = "aba"
# 输出：2
# 解释：一种最大拆分方法为 ['a', 'ba'] 。
#  
# 
#  示例 3： 
# 
#  输入：s = "aa"
# 输出：1
# 解释：无法进一步拆分字符串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  
#  1 <= s.length <= 16 
#  
#  
#  s 仅包含小写英文字母 
#  
#  
#  Related Topics 哈希表 字符串 回溯 👍 49 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        # corner case
        if len(s) == 1:
            return 1

        # dfs
        def dfs(i, path):
            if i == n:
                if len(path) > self.res:
                    self.res = len(path)
                return

            for j in range(i, n):
                if s[i:j + 1] not in path:
                    path.add(s[i:j + 1])
                    dfs(j + 1, path)
                    path.discard(s[i:j + 1])
            return

        self.res = float('-inf')
        n = len(s)
        dfs(0, set())  # 从0开始，到j-1为止

        return self.res
# leetcode submit region end(Prohibit modification and deletion)
