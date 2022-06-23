# 给你一个字符串 time ，格式为 hh:mm（小时：分钟），其中某几位数字被隐藏（用 ? 表示）。 
# 
#  有效的时间为 00:00 到 23:59 之间的所有时间，包括 00:00 和 23:59 。 
# 
#  替换 time 中隐藏的数字，返回你可以得到的最晚有效时间。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：time = "2?:?0"
# 输出："23:50"
# 解释：以数字 '2' 开头的最晚一小时是 23 ，以 '0' 结尾的最晚一分钟是 50 。
#  
# 
#  示例 2： 
# 
#  
# 输入：time = "0?:3?"
# 输出："09:39"
#  
# 
#  示例 3： 
# 
#  
# 输入：time = "1?:22"
# 输出："19:22"
#  
# 
#  
# 
#  提示： 
# 
#  
#  time 的格式为 hh:mm 
#  题目数据保证你可以由输入的字符串生成有效的时间 
#  
#  Related Topics 字符串 👍 62 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        time = list(time)
        for i in range(len(time)):
            if time[i] == "?":
                if i == 0:
                    time[i] = "2" if time[i + 1] in "?0123" else "1"
                elif i == 1:
                    time[i] = "3" if time[0] == "2" else "9"
                elif i == 3:
                    time[i] = "5"
                else:
                    time[i] = "9"
        return "".join(time)
# leetcode submit region end(Prohibit modification and deletion)
