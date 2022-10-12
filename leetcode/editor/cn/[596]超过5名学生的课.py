# 表: Courses 
# 
#  
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | student     | varchar |
# | class       | varchar |
# +-------------+---------+
# (student, class)是该表的主键列。
# 该表的每一行表示学生的名字和他们注册的班级。
#  
# 
#  
# 
#  编写一个SQL查询来报告 至少有5个学生 的所有类。 
# 
#  以 任意顺序 返回结果表。 
# 
#  查询结果格式如下所示。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: 
# Courses table:
# +---------+----------+
# | student | class    |
# +---------+----------+
# | A       | Math     |
# | B       | English  |
# | C       | Math     |
# | D       | Biology  |
# | E       | Math     |
# | F       | Computer |
# | G       | Math     |
# | H       | Math     |
# | I       | Math     |
# +---------+----------+
# 输出: 
# +---------+ 
# | class   | 
# +---------+ 
# | Math    | 
# +---------+
# 解释: 
# -数学课有6个学生，所以我们包括它。
# -英语课有1名学生，所以我们不包括它。
# -生物课有1名学生，所以我们不包括它。
# -计算机课有1个学生，所以我们不包括它。 
#  Related Topics 数据库 👍 227 👎 0


# There is no code of Python type for this problem