import time

import pygame
from pygame.constants import *


def main():
    """完成整个程序的控制"""
    # 1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # 2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png")
    # 4.创建一个玩家飞机图片,当做真正的飞机
    player = pygame.image.load("./feiji/hero1.png")

    # 定义飞机的坐标
    x = 480 / 2 - 100 / 2
    y = 600

    # 飞机速度
    speed = 10

    # 设定需要显示的背景图
    while True:
        # 3将背景图片贴到窗口中
        screen.blit(background, (0, 0))
        # 5将飞机图片贴到窗口中
        screen.blit(player, (x, y))

        # 遍历所有的事件
        for event in pygame.event.get():
            # 判断事件类型如果是pygame的退出
            if event.type == QUIT:
                # 执行pygame退出
                pygame.quit()
                # python程序的退出
                exit()

        # 监听键盘事件
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            print("上")
            y -= speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            print("下")
            y += speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            print("左")
            x -= speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            print("右")
            x += speed
        if key_pressed[K_SPACE]:
            print("空格")

            # 更新需要显示的内容
        pygame.display.update()
        time.sleep(0.01)


if __name__ == "__main__":
    main()
