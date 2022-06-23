# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。 
# 
#  请注意，你可以假定字符串里不包括任何不可打印的字符。 
# 
#  示例: 
# 
#  输入: "Hello, my name is John"
# 输出: 5
# 解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。
#  
#  Related Topics 字符串 👍 167 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            if (i == 0 or s[i - 1] == " ") and s[i] != " ":
                count += 1
        return count
# leetcode submit region end(Prohibit modification and deletion)
