# 给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。 
# 
#  输入为三个整数：day、month 和 year，分别表示日、月、年。 
# 
#  您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", 
# "Friday", "Saturday"}。 
# 
#  
# 
#  示例 1： 
# 
#  输入：day = 31, month = 8, year = 2019
# 输出："Saturday"
#  
# 
#  示例 2： 
# 
#  输入：day = 18, month = 7, year = 1999
# 输出："Sunday"
#  
# 
#  示例 3： 
# 
#  输入：day = 15, month = 8, year = 1993
# 输出："Sunday"
#  
# 
#  
# 
#  提示： 
# 
#  
#  给出的日期一定是在 1971 到 2100 年之间的有效日期。 
#  
#  Related Topics 数学 👍 111 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        days = 0
        days += 365 * (year - 1971) + (year - 1969) // 4
        days += sum(monthDays[:month - 1])
        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) and month >= 3:
            days += 1
        days += day
        return week[(days + 3) % 7]
# leetcode submit region end(Prohibit modification and deletion)
