import random

import pygame
from pygame.constants import *
import time


# 玩家飞机
class PlayerPlane(object):
    def __init__(self, screen):
        # 3创建一个图片，作玩家飞机
        self.player = pygame.image.load("./feiji/hero1.png")
        # 飞机的坐标
        self.x = 480 / 2 - 100 / 2
        self.y = 600
        # 飞机速度
        self.speed = 10
        # 记录当前的窗口对象
        self.screen = screen
        # 装子弹的列表
        self.bullets = []

    def key_control(self):
        # 监听键盘事件
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.x -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.x += self.speed
        if key_pressed[K_w] or key_pressed[K_UP]:
            self.y -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.y += self.speed
        if key_pressed[K_SPACE]:
            # 按下空格键发射子弹
            bullet = Bullet(self.screen, self.x, self.y)
            # 把子弹放进列表
            self.bullets.append(bullet)

    def display(self):
        # 5将飞机图片贴到窗口中
        self.screen.blit(self.player, (self.x, self.y))
        # 遍历所有子弹
        for bullet in self.bullets:
            # 让子弹飞，修改子弹y坐标
            bullet.auto_move()
            # 将子弹显示在窗口
            bullet.display()


# 敌机
class EnemyPlane(object):
    def __init__(self, screen):
        # 3创建一个图片，作玩家飞机
        self.player = pygame.image.load("./feiji/enemy0.png")  # 51*39
        # 飞机的坐标
        self.x = 0
        self.y = 0
        # 飞机速度
        self.speed = 10
        # 记录当前的窗口对象
        self.screen = screen
        # 装子弹的列表
        self.bullets = []
        # 敌机移动方向
        self.direction = 'right'

    def display(self):
        # 5将飞机图片贴到窗口中
        self.screen.blit(self.player, (self.x, self.y))
        # 遍历所有子弹
        for bullet in self.bullets:
            # 让子弹飞，修改子弹y坐标
            bullet.auto_move()
            # 将子弹显示在窗口
            bullet.display()

    def auto_move(self):
        if self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        if self.x > 480 - 51:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'

    def auto_fire(self):
        """自动开火 创建敌机子弹对象 添加进列表"""
        random_num = random.randint(1, 10)
        if random_num == 8:
            bullet = EnemyBullet(self.screen, self.x, self.y)
            self.bullets.append(bullet)


# 子弹类
# 属性
class Bullet(object):
    def __init__(self, screen, x, y):
        # 坐标
        self.x = x + 100 / 2 - 22 / 2
        self.y = y - 22
        # 图片
        self.image = pygame.image.load("./feiji/bullet.png")
        # 窗口
        self.screen = screen
        # 速度
        self.speed = 10

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def auto_move(self):
        # """让子弹飞"""
        self.y -= self.speed


# 敌机子弹类
# 属性
class EnemyBullet(object):
    def __init__(self, screen, x, y):
        # 坐标
        self.x = x + 50 / 2 - 8 / 2
        self.y = y + 39
        # 图片
        self.image = pygame.image.load("./feiji/bullet1.png")  # 9*39
        # 窗口
        self.screen = screen
        # 速度
        self.speed = 10

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def auto_move(self):
        # """让子弹飞"""
        self.y += self.speed


class GameSound(object):
    def __init__(self):
        pygame.mixer.init()  # 音乐模块初始化
        pygame.mixer.music.load('./feiji/bg2.ogg')
        pygame.mixer.music.set_volume(0.5)

    def playBackgroundMusic(self):
        pygame.mixer.music.play(-1)


def main():
    """完成整个程序的控制"""
    sound = GameSound()
    sound.playBackgroundMusic()

    # 1创建一个窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # 2创建一个图片，作背景
    background = pygame.image.load("./feiji/background.png")
    # 创建玩家飞机
    player = PlayerPlane(screen)
    # 创建敌方飞机
    enemyplane = EnemyPlane(screen)
    while True:
        # 4将背景图片贴到窗口中
        screen.blit(background, (0, 0))

        # 获取事件
        for event in pygame.event.get():
            # 判断事件类型
            if event.type == pygame.QUIT:
                # 执行pygame退出
                pygame.quit()
                # python程序退出
                exit()
        # 执行飞机监听
        player.key_control()
        # 显示玩家飞机
        player.display()
        # 显示敌方飞机
        enemyplane.display()
        # 敌机自动移动
        enemyplane.auto_move()
        # 敌机自动开火
        enemyplane.auto_fire()
        # 4更新需要显示的内容
        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
