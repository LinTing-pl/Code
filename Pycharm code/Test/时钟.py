#!/Users/env python
# -*- coding:utf-8 -*-
# @author：麟听

from datetime import *
import turtle


def Skip(step):
    """抬起画笔，向前运动一段距离放下"""
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()


def mkHand(name, length):
    """建立表针形状,名字"""
    turtle.reset()  # 重置
    Skip(-length * 0.1)
    turtle.begin_poly()  # 开始记录多边形的顶点。
    turtle.forward(length * 1.1)
    turtle.end_poly()  # 停止记录多边形的顶点。
    handForm = turtle.get_poly()  # 返回最后记录的多边形。
    turtle.addshape(name, handForm)  # 添加表针名字,形状


def Init():
    """建立三个表针Turtle"""
    global secHand, minHand, hourHand, printer  # 全局变量
    turtle.mode("logo")  # 顺时针 turtle朝北
    mkHand("secHand", 135)  # 建立秒针
    mkHand("minHand", 125)  # 建立分针
    mkHand("hourHand", 90)  # 建立时针
    secHand = turtle.Turtle()
    secHand.shape("secHand")
    minHand = turtle.Turtle()
    minHand.shape("minHand")
    hourHand = turtle.Turtle()
    hourHand.shape("hourHand")

    secHand.shapesize(1, 1, 2)
    secHand.speed(10)
    minHand.shapesize(1, 1, 3)
    minHand.speed(10)
    hourHand.shapesize(1, 1, 4)
    hourHand.speed(10)

    printer = turtle.Turtle()  # 建立输出文字Turtle
    printer.hideturtle()  # 隐藏画笔的turtle形状


def SetupClock(radius):
    """建立表的外框"""
    turtle.reset()  # 重置
    turtle.pensize(7)  # 画笔粗细
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            turtle.forward(20)
            Skip(-radius - 20)

            Skip(radius + 20)
            if i == 0:
                turtle.write(int(12), align="center", font=("宋体", 14, "bold"))
            elif i == 30:
                Skip(25)
                turtle.write(int(i / 5), align="center", font=("宋体", 14, "bold"))
                Skip(-25)
            elif i == 25 or i == 35:
                Skip(20)
                turtle.write(int(i / 5), align="center", font=("宋体", 14, "bold"))
                Skip(-20)
            else:
                turtle.write(int(i / 5), align="center", font=("宋体", 14, "bold"))
            Skip(-radius - 20)
        else:
            turtle.dot(5)
            Skip(-radius)
        turtle.right(6)


def Week(t):
    """获取星期几"""
    week = ["", "星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday() + 1]


def Date(t):
    """获取年月日"""
    y = t.year
    m = t.month
    d = t.day
    return "%s年 %d月%d日" % (y, m, d)


def Tick():
    """ 绘制表针的动态显示"""
    t = datetime.today()  # 获取实时时间
    second = t.second
    minute = t.minute
    hour = t.hour
    secHand.setheading(6 * second)  # 秒针朝向
    minHand.setheading(6 * minute)  # 分针朝向
    hourHand.setheading(30 * hour)  # 时针朝向

    turtle.tracer(False)  # 打开/关闭turtle动画
    printer.penup()
    printer.forward(65)
    printer.write(Week(t), align="center",
                  font=("宋体", 14, "bold"))
    printer.back(130)
    printer.write(Date(t), align="center",
                  font=("宋体", 14, "bold"))
    printer.home()  # turtle回到原点 turtle朝北
    turtle.tracer(True)

    turtle.ontimer(Tick, 100)  # 100ms后继续调用tick


def main():
    # 并为更新图纸设置延迟。
    turtle.tracer(False)  # 打开/关闭turtle动画
    Init()
    SetupClock(160)
    turtle.tracer(True)
    Tick()
    turtle.mainloop()


if __name__ == "__main__":
    main()
