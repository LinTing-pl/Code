import random
import time
import pygame
from pygame.constants import *


class HeroPlane(pygame.sprite.Sprite):
    def __init__(self, screen):
        # 这个精灵的初始化方法 必须调用
        pygame.sprite.Sprite.__init__(self)

        # 4.创建一个玩家飞机图片,当做真正的飞机
        self.image = pygame.image.load("./feiji/hero1.png")

        # 根据图片image获取矩形对象
        self.rect = self.image.get_rect()  # rect：矩形
        self.rect.topleft = [480 / 2 - 100 / 2, 600]

        # 飞机速度
        self.speed = 15

        # 记录当前的窗口对象
        self.screen = screen

        # 装子弹的列表
        self.bullets = pygame.sprite.Group()

    def key_control(self):
        # 监听键盘事件
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            self.rect.top -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.rect.bottom += self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.rect.left -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.rect.right += self.speed
        if key_pressed[K_SPACE]:
            # 按下空格键发射子弹
            bullet = Bullet(self.screen, self.rect.left, self.rect.top)
            # 把子弹放到列表里
            self.bullets.add(bullet)

    def update(self):
        self.key_control()
        self.display()

    def display(self):
        # 5将飞机图片贴到窗口中
        self.screen.blit(self.image, self.rect)
        # 更新子弹坐标
        self.bullets.update()

        # 把所有子弹全部添加到屏幕
        self.bullets.draw(self.screen)


class EnemyPlane(pygame.sprite.Sprite):
    def __init__(self, screen):
        # 这个精灵的初始化方法 必须调用
        pygame.sprite.Sprite.__init__(self)

        # 4.创建一个玩家飞机图片,当做真正的飞机
        self.image = pygame.image.load("./feiji/enemy0.png")

        # 根据图片image获取矩形对象
        self.rect = self.image.get_rect()  # rect：矩形
        self.rect.topleft = [0, 0]

        # 飞机速度
        self.speed = 15

        # 记录当前的窗口对象
        self.screen = screen

        # 装子弹的列表
        self.bullets = pygame.sprite.Group()

        # 敌机移动方向
        self.direction = 'right'

    def display(self):
        # 5将飞机图片贴到窗口中
        self.screen.blit(self.image, self.rect)
        # 更新子弹坐标
        self.bullets.update()

        # 把所有子弹全部添加到屏幕
        self.bullets.draw(self.screen)

    def update(self):
        self.auto_move()
        self.auto_fire()
        self.display()

    def auto_move(self):
        if self.direction == 'right':
            self.rect.right += self.speed
        elif self.direction == 'left':
            self.rect.right -= self.speed

        if self.rect.right > 480 - 51:
            self.direction = 'left'
        elif self.rect.right < 0:
            self.direction = 'right'

    def auto_fire(self):
        """自动开火 创建子弹对象 添加进列表"""
        random_num = random.randint(1, 10)
        if random_num == 8:
            bullet = EnemyBullet(self.screen, self.rect.left, self.rect.top)
            self.bullets.add(bullet)


# 子弹类
# 属性
class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        # 精灵类初始化
        pygame.sprite.Sprite.__init__(self)

        # 创建图片
        self.image = pygame.image.load('./feiji/bullet.png')

        # 获取矩形对象
        self.rect = self.image.get_rect()
        self.rect.topleft = [x + 100 / 2 - 22 / 2, y - 22]

        # 窗口
        self.screen = screen
        # 速度
        self.speed = 20

    def update(self):
        # 修改子弹坐标
        self.rect.top -= self.speed
        # 如果子弹移出屏幕上方 则销毁子弹对象
        if self.rect.top < -22:
            self.kill()


# 敌方子弹类
# 属性
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        # 精灵类初始化
        pygame.sprite.Sprite.__init__(self)

        # 创建图片
        self.image = pygame.image.load('./feiji/bullet1.png')

        # 获取矩形对象
        self.rect = self.image.get_rect()
        self.rect.topleft = [x + 50 / 2 - 8 / 2, y + 39]

        # 窗口
        self.screen = screen
        # 速度
        self.speed = 20

    def update(self):
        # 修改子弹坐标
        self.rect.top += self.speed
        # 如果子弹移出屏幕上方 则销毁子弹对象
        if self.rect.top > 852:
            self.kill()


class GameSound(object):
    def __init__(self):
        pygame.mixer.init()  # 音乐模块初始化
        pygame.mixer.music.load('./feiji/bg2.ogg')
        pygame.mixer.music.set_volume(0.5)  # 声音大小

    def playBackgroundMusic(self):
        pygame.mixer.music.play(-1)  # 开始播放音乐


def main():
    """完成整个程序的控制"""
    sound = GameSound()
    sound.playBackgroundMusic()

    # 1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # 2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png")

    # 创建一个飞机的对象，注意不要忘记传窗口
    player = HeroPlane(screen)
    # 创建一个敌方飞机的对象，注意不要忘记传窗口
    enemyplane = EnemyPlane(screen)

    # 设定需要显示的背景图
    while True:
        # 3将背景图片贴到窗口中
        screen.blit(background, (0, 0))

        # 遍历所有的事件
        for event in pygame.event.get():
            # 判断事件类型如果是pygame的退出
            if event.type == QUIT:
                # 执行pygame退出
                pygame.quit()
                # python程序的退出
                exit()

        # 执行飞机的按键监听
        player.key_control()
        # 飞机的显示
        player.display()
        # 敌方飞机的显示
        enemyplane.display()
        # 敌机自动移动
        enemyplane.auto_move()
        # 敌机自动开火
        enemyplane.auto_fire()

        # 更新需要显示的内容
        pygame.display.update()
        time.sleep(0.01)


if __name__ == "__main__":
    main()
