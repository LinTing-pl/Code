# 给你一个字符串 s ，它只包含三种字符 a, b 和 c 。 
# 
#  请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "abcabc"
# 输出：10
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "abc", "abca", "abcab", "abcabc", "bca", "bcab", 
# "bcabc", "cab", "cabc" 和 "abc" (相同字符串算多次)。
#  
# 
#  示例 2： 
# 
#  输入：s = "aaacb"
# 输出：3
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "aaacb", "aacb" 和 "acb" 。
#  
# 
#  示例 3： 
# 
#  输入：s = "abc"
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= s.length <= 5 x 10^4 
#  s 只包含字符 a，b 和 c 。 
#  
#  Related Topics 哈希表 字符串 滑动窗口 👍 73 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum1, sum2 = 0, 0
        neednumber = 3
        d = {"a": 1, "b": 1, "c": 1}  # 建立哈希表，用于记录达成题意的子字符串需要的每个字符的个数
        tip1, tip2 = 0, 0
        while tip2 < len(s):  # 采用双指针构建一个滑动窗口
            d[s[tip2]] -= 1
            if d[s[tip2]] == 0:
                neednumber -= 1
            if neednumber == 0:  # 如果此时窗口内部的子字符串符合题意，那么移动左指针，用于计算窗口内部还有几个子字符串串符合题意。
                while neednumber == 0:  # 如果不符合题意，那么不再移动左指针。
                    sum2 += 1  # 这里很重要，如果左指针向左移动一位符合题意，那么说明该窗口中多出一个符合题意得子子字符串。
                    d[s[tip1]] += 1
                    if d[s[tip1]] == 1:
                        neednumber += 1
                    else:
                        pass
                    tip1 += 1
            sum1 += sum2  # 为什么＋sum2，原因在于每次移动右指针后，原先的窗口符合条件的子字符串会被新窗口给覆盖。
            tip2 += 1  # 移动右指针，拓展滑动窗口的大小，找到符合题意得子字符串。
        return sum1
# leetcode submit region end(Prohibit modification and deletion)
