import pygame
from pygame import *
import time


def main():
    """完成整个程序的控制"""
    # 1创建一个窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # 2创建一个图片，作背景
    background = pygame.image.load("./feiji/background.png")
    # 3创建一个图片，作玩家飞机
    player = pygame.image.load("./feiji/hero1.png")

    x = 480 / 2 - 100 / 2
    y = 600
    # 飞机速度
    speed = 10
    while True:
        # 4将背景图片贴到窗口中
        screen.blit(background, (0, 0))
        # 5将飞机图片贴到窗口中
        screen.blit(player, (x, y))
        # 获取事件
        for event in pygame.event.get():
            # 判断事件类型
            if event.type == pygame.QUIT:
                # 执行pygame退出
                pygame.quit()
                # python程序退出
                exit()
            # 监听键盘事件
            key_pressed = pygame.key.get_pressed()

            if key_pressed[K_a] or key_pressed[K_LEFT]:
                x -= speed
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                x += speed
            if key_pressed[K_w] or key_pressed[K_UP]:
                y -= speed
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                y += speed
            if key_pressed[K_SPACE]:
                print('空格')
        # 4显示窗口中的内容
        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
