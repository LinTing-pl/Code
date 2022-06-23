# 给你两个长度相同的字符串，s 和 t。 
# 
#  将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的
# 绝对值。 
# 
#  用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。 
# 
#  如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。 
# 
#  如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abcd", t = "bcdf", maxCost = 3
# 输出：3
# 解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。 
# 
#  示例 2： 
# 
#  
# 输入：s = "abcd", t = "cdef", maxCost = 3
# 输出：1
# 解释：s 中的任一字符要想变成 t 中对应的字符，其开销都是 2。因此，最大长度为 1。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "abcd", t = "acde", maxCost = 0
# 输出：1
# 解释：a -> a, cost = 0，字符串未发生变化，所以最大长度为 1。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 10^5 
#  0 <= maxCost <= 10^6 
#  s 和 t 都只含小写英文字母。 
#  
#  Related Topics 字符串 二分查找 前缀和 滑动窗口 👍 168 👎 0


# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        n = len(s)
        record = []
        for i in range(n):
            record.append(abs(ord(t[i]) - ord(s[i])))

        start, end = 0, 0
        windowsum = 0
        res = 0
        for end in range(n):
            # print windowsum, start, end, res
            windowsum += record[end]

            while windowsum > maxCost:
                res = max(res, end - start)
                windowsum -= record[start]
                start += 1
        res = max(res, end - start + 1)
        return res
# leetcode submit region end(Prohibit modification and deletion)
