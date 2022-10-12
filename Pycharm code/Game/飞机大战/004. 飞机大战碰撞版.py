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
        self.speed = 12

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
        self.speed = 15

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

        self.__bomb = pygame.mixer.Sound('./feiji/bomb.wav')

    def playBackgroundMusic(self):
        pygame.mixer.music.play(-1)  # 开始播放音乐

    def playBombSound(self):
        pygame.mixer.Sound.play(self.__bomb)


class Bomb(object):
    # 初始化碰撞
    def __init__(self, screen, type):
        self.screen = screen
        if type == "enemy":
            # 加载爆炸资源
            self.mImage = [pygame.image.load
                           ("./feiji/enemy0_down" + str(v) + ".png") for v in range(1, 5)]
        else:
            self.mImage = [pygame.image.load
                           ("./feiji/hero_blowup_n" + str(v) + ".png") for v in range(1, 5)]
        # 设置当前爆炸播放索引
        self.mIndex = 0
        # 爆炸设置
        self.mPos = [0, 0]
        # 是否可见
        self.mVisible = False

    def action(self, rect):
        # 触发爆炸方法draw
        # 爆炸的坐标
        self.mPos[0] = rect.left
        self.mPos[1] = rect.top
        # 打开爆炸的开关
        self.mVisible = True

    def draw(self):
        if not self.mVisible:
            return
        self.screen.blit(self.mImage[self.mIndex], (self.mPos[0], self.mPos[1]))
        self.mIndex += 1
        if self.mIndex >= len(self.mImage):
            # 如果下标已经到最后了 代表爆炸结束
            # 下标位置重置 mVisible重置
            self.mIndex = 0
            self.mVisible = False


class Manager(object):
    def __init__(self):
        # 创建窗口
        self.screen = pygame.display.set_mode((480, 852), 0, 32)
        # 创建背景图片
        self.background = pygame.image.load("./feiji/background.png")
        # 初始化一个装玩家精灵的group
        self.players = pygame.sprite.Group()
        # 初始化一个装敌机精灵的group
        self.enemys = pygame.sprite.Group()
        # 初始化一个玩家爆炸的对象
        self.player_bomb = Bomb(self.screen, 'player')
        # 初始化一个敌机爆炸的对象
        self.enemy_bomb = Bomb(self.screen, 'enemy')
        # 初始化一个声音播放的对象
        self.sound = GameSound()

    def exit(self):
        print('退出')
        pygame.quit()
        exit()

    def new_player(self):
        # 创建飞机对象 添加到玩家的组
        player = HeroPlane(self.screen)
        self.players.add(player)

    def new_enemy(self):
        # 创建敌机的对象 添加到敌机的组
        enemy = EnemyPlane(self.screen)
        self.enemys.add(enemy)

    def main(self):
        # 播放背景音乐
        self.sound.playBackgroundMusic()
        # 创建一个玩家
        self.new_player()
        # 创建一个敌机
        self.new_enemy()
        while True:
            # 把背景图片贴到窗口
            self.screen.blit(self.background, (0, 0))
            # 遍历所有的事件
            for event in pygame.event.get():
                # 判断事件类型如果是pygame的退出
                if event.type == QUIT:
                    self.exit()

            # 调用爆炸的对象
            self.player_bomb.draw()
            self.enemy_bomb.draw()

            # 判断碰撞
            iscollide = pygame.sprite.groupcollide(self.players, self.enemys, True, True)

            if iscollide:
                items = list(iscollide.items())[0]
                print(items)
                x = items[0]
                y = items[1][0]
                # 玩家爆炸图片
                self.player_bomb.action(x.rect)
                # 敌机爆炸图片
                self.enemy_bomb.action(y.rect)
                # 爆炸的声音
                self.sound.playBombSound()

            # 玩家飞机和子弹的显示
            self.players.update()
            # 敌机和子弹的显示
            self.enemys.update()

            # 刷新窗口内容
            pygame.display.update()
            time.sleep(0.01)


if __name__ == '__main__':
    manager = Manager()
    manager.main()
