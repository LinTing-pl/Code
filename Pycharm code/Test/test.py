#!/Users/env python
# -*- coding:utf-8 -*-
# @author：麟听 WeChat:15019763969


# ①
# def jiecheng(num):
#     """求阶乘，num为阶乘"""
#     if num > 0:
#         return num * jiecheng(num - 1)
#     else:
#         return 1


# ②
# import math
# def S(radius):
#     """求圆的面积,radius为圆的半径"""
#     return radius**2*math.pi


# ③
# def issushu(num):
#     """判断是否是素数"""
#     if num <= 1:
#         return False
#     if num == 2:
#         return True
#     for i in range(2, int(num / 2) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# def sushu(a, b, start=True, end=False):
#     """求区间所有的素数，默认为[a,b)左闭右开区间"""
#     result = []
#     if start:
#         a = a
#     else:
#         a = a + 1
#     if end:
#         b = b + 1
#     else:
#         b = b
#     for i in range(a, b):
#         if issushu(i):
#             result.append(i)
#     return result


# ④
# def nPingFanHe(num):
#     """求前n项的平方和"""
#     result = sum(map(lambda x: x ** 2, range(1, num + 1)))
#     return result


# ⑤
# def isOushu(num):
#     """判断是否是偶数"""
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
#
# def oushu(a, b, start=True, end=False):
#     """求区间中的偶数，默认[a,b),左闭右开区间"""
#     result = []
#     if start:
#         a = a
#     else:
#         a = a + 1
#     if end:
#         b = b + 1
#     else:
#         b = b
#     for i in range(a, b):
#         if isOushu(i):
#             result.append(i)
#     return result


# ⑥
# def paixu(iterable, button=False):
#     """对可迭代对象排序，button控制升降序，默认为False升序"""
#     obj = sorted(iterable, key=lambda x: x["grade"], reverse=button)
#     return obj


# ⑦
# def datedefference(date1, date2=None):
#     """计算两个日期的时间差，date1:year-month-day;date2默认为None"""
#     import datetime
#     if date2 is None:
#         date2 = datetime.datetime.now()
#     else:
#         date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
#     date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
#     return date2 - date1


# ⑧
# def datedeff(date1, days):
#     """计算时间差，date1:year-month-day；days：天数"""
#     import datetime
#     date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
#     time_gap = datetime.timedelta(days=days)
#     time_result = date1 - time_gap
#     return time_result.strftime("%Y-%m-%d")


# ⑨
# def daterange(begin_date, end_date):
#     """遍历日期，date1:year-month-day；date2:year-month-day"""
#     import datetime
#     begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
#     end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
#     day = datetime.timedelta(days=1)
#     date_list = []
#     while begin_date <= end_date:
#         date_list.append(begin_date)
#         begin_date = begin_date + day
#     return date_list