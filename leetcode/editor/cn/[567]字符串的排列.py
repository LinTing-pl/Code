# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。 
# 
#  换句话说，s1 的排列之一是 s2 的 子串 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
#  
# 
#  示例 2： 
# 
#  
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s1.length, s2.length <= 10⁴ 
#  s1 和 s2 仅包含小写字母 
#  
#  Related Topics 哈希表 双指针 字符串 滑动窗口 👍 670 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        a = [ord(x) - ord('a') for x in s1]
        b = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        for x in a:
            target[x] += 1

        window = [0] * 26
        for i, x in enumerate(b):
            window[x] += 1
            if i >= len(a):
                window[b[i - len(a)]] -= 1

            if window == target:
                return True
        return False

# leetcode submit region end(Prohibit modification and deletion)
