# 给你一个以二进制形式表示的数字 s 。请你返回按下述规则将其减少到 1 所需要的步骤数： 
# 
#  
#  
#  如果当前数字为偶数，则将其除以 2 。 
#  
#  
#  如果当前数字为奇数，则将其加上 1 。 
#  
#  
# 
#  题目保证你总是可以按上述规则将测试用例变为 1 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "1101"
# 输出：6
# 解释："1101" 表示十进制数 13 。
# Step 1) 13 是奇数，加 1 得到 14 
# Step 2) 14 是偶数，除 2 得到 7
# Step 3) 7  是奇数，加 1 得到 8
# Step 4) 8  是偶数，除 2 得到 4  
# Step 5) 4  是偶数，除 2 得到 2 
# Step 6) 2  是偶数，除 2 得到 1  
#  
# 
#  示例 2： 
# 
#  输入：s = "10"
# 输出：1
# 解释："10" 表示十进制数 2 。
# Step 1) 2 是偶数，除 2 得到 1 
#  
# 
#  示例 3： 
# 
#  输入：s = "1"
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 500 
#  s 由字符 '0' 或 '1' 组成。 
#  s[0] == '1' 
#  
#  Related Topics 位运算 字符串 👍 37 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 字符串转为2进制下的十进制
        s = int(s, 2)
        cnt = 0
        while s > 1:
            # 判断最后一位是否为1，不管结果如何都算一步
            if s & 1 == 1:
                s += 1
            elif s & 1 == 0:
                s = s >> 1
            cnt += 1
        return cnt
# leetcode submit region end(Prohibit modification and deletion)
