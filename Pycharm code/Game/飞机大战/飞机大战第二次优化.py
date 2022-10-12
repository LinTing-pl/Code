import random

import pygame
from pygame.constants import *
import time


# 玩家飞机
class PlayerPlane(pygame.sprite.Sprite):
    # 添加所有飞机子弹的组
    bullets = pygame.sprite.Group()

    def __init__(self, screen):
        # 精灵类初始化
        pygame.sprite.Sprite.__init__(self)

        # 3创建一个图片，作玩家飞机
        self.player = pygame.image.load("./feiji/hero1.png")
        # 根据图片image 获取矩形对象
        self.rect = self.player.get_rect()
        self.rect.topleft = [Manager.bg_size[0] / 2 - 100 / 2, 600]
        # 飞机速度
        self.speed = 12
        # 记录当前的窗口对象
        self.screen = screen
        # 装子弹的列表
        self.bullets = pygame.sprite.Group()

    def key_control(self):
        # 监听键盘事件
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.rect.left -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.rect.right += self.speed
        if key_pressed[K_w] or key_pressed[K_UP]:
            self.rect.top -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.rect.bottom += self.speed
        if key_pressed[K_SPACE]:
            # 按下空格键发射子弹
            bullet = Bullet(self.screen, self.rect.left, self.rect.top)
            # 把子弹放进列表
            self.bullets.add(bullet)
            # 把子弹添加到类属性的精灵组里
            PlayerPlane.bullets.add(bullet)

    def update(self):
        self.key_control()
        self.display()

    def display(self):
        # 5将飞机图片贴到窗口中
        self.screen.blit(self.player, self.rect)
        # 更新子弹坐标
        self.bullets.update()
        # 把所有子弹全部添加到窗口
        self.bullets.draw(self.screen)

    @classmethod
    def clear_bullets(cls):
        # 清空子弹
        cls.bullets.empty()


# 敌机
class EnemyPlane(pygame.sprite.Sprite):
    # 敌机所有子弹的组
    enemy_bullets = pygame.sprite.Group()

    def __init__(self, screen):
        # 初始化精灵类
        pygame.sprite.Sprite.__init__(self)

        # 3创建一个图片，作敌方飞机
        self.player = pygame.image.load("./feiji/enemy0.png")  # 51*39
        # 获取图片image的矩形对象
        self.rect = self.player.get_rect()
        x = random.randrange(0, Manager.bg_size[0], 50)
        self.rect.topleft = [x, 0]

        # 飞机速度
        self.speed = 8
        # 记录当前的窗口对象
        self.screen = screen
        # 装子弹的列表
        self.bullets = pygame.sprite.Group()
        # 敌机移动方向
        self.direction = 'right'

    def display(self):
        # 5将飞机图片贴到窗口中
        self.screen.blit(self.player, self.rect)
        # 更新子弹坐标
        self.bullets.update()
        # 把所有子弹全部添加到窗口中
        self.bullets.draw(self.screen)

    def update(self):
        self.auto_move()
        self.auto_fire()
        self.display()

    def auto_move(self):
        if self.direction == 'right':
            self.rect.left += self.speed
        elif self.direction == 'left':
            self.rect.left -= self.speed
        if self.rect.left > Manager.bg_size[0] - 51:
            self.direction = 'left'
        elif self.rect.left < 0:
            self.direction = 'right'
        self.rect.bottom += self.speed

    def auto_fire(self):
        """自动开火 创建敌机子弹对象 添加进列表"""
        random_num = random.randint(1, 10)
        if random_num == 8:
            bullet = EnemyBullet(self.screen, self.rect.left, self.rect.top)
            self.bullets.add(bullet)
            # 把子弹添加到类属性的精灵组里
            EnemyPlane.enemy_bullets.add(bullet)

    @classmethod
    def clear_bullets(cls):
        # 清空子弹
        cls.enemy_bullets.empty()


# 子弹类
# 属性
class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        # 精灵类初始化
        pygame.sprite.Sprite.__init__(self)

        # 图片
        self.image = pygame.image.load("./feiji/bullet.png")

        # 获取矩阵对象
        self.rect = self.image.get_rect()
        self.rect.topleft = [x + 100 / 2, y - 22]

        # 窗口
        self.screen = screen
        # 速度
        self.speed = 20

    def update(self):
        # 修改子弹坐标
        self.rect.top -= self.speed
        # 如果子弹移出屏幕上方，则销毁子弹对象
        if self.rect.top < -22:
            self.kill()


# 敌机子弹类
# 属性
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)

        # 图片
        self.image = pygame.image.load("./feiji/bullet1.png")  # 9*39

        # 坐标
        self.rect = self.image.get_rect()
        self.rect.topleft = [x + 50 / 2 - 8 / 2, y + 39]
        # 窗口
        self.screen = screen
        # 速度
        self.speed = 10

    def update(self):
        # 修改子弹坐标
        self.rect.top += self.speed
        # 如果子弹移出屏幕，则销毁子弹对象
        if self.rect.top > Manager.bg_size[1]:
            self.kill()


class GameSound(object):
    def __init__(self):
        pygame.mixer.init()  # 音乐模块初始化
        pygame.mixer.music.load('./feiji/bg2.ogg')
        pygame.mixer.music.set_volume(0.5)
        self.__bomb = pygame.mixer.Sound("./feiji/bomb.wav")

    def playBackgroundMusic(self):
        pygame.mixer.music.play(-1)

    def playBombSound(self):
        pygame.mixer.Sound.play(self.__bomb)  # 爆炸音乐


class Bomb(object):
    def __init__(self, screen, type):
        self.screen = screen
        if type == 'enemy':
            # 加载爆炸资源
            self.mImage = [pygame.image.load("./feiji/enemy0_down" + str(v) + ".png") for v in range(1, 5)]
        if type == 'player':
            self.mImage = [pygame.image.load("./feiji/hero_blowup_n" + str(v) + ".png") for v in range(1, 5)]
        if type == 'bullet':
            pass
        # 爆炸索引
        self.mIndex = 0
        # 爆炸位置
        self.mPos = [0, 0]
        # 是否可见
        self.mVisible = False

    def action(self, rect):
        # 触发爆炸的方法
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
            # 如果下标已经到最后 代表爆炸结束
            # 下标位置重置 mVisible重置
            self.mIndex = 0
            self.mVisible = False


# 地图
class GameBackGround(object):
    # 初始化地图
    def __init__(self, screen):
        self.mImage1 = pygame.image.load("./feiji/img_bg_level_1.jpg")
        self.mImage2 = pygame.image.load("./feiji/img_bg_level_1.jpg")

        # 窗口
        self.screen = screen
        # 辅助移动地图
        self.y1 = 0
        self.y2 = -Manager.bg_size[1]  # -768

    def move(self):
        self.y1 += 1.5
        self.y2 += 1.5
        if self.y1 > Manager.bg_size[1]:
            self.y1 = 0
        if self.y2 > 0:
            self.y2 = -Manager.bg_size[1]

    # 绘制地图
    def draw(self):
        self.screen.blit(self.mImage1, (0, self.y1))
        self.screen.blit(self.mImage2, (0, self.y2))


class Manager(object):
    bg_size = (512, 768)
    # 创建敌机生成定时器id
    create_enemy_id = 10
    # 游戏结束倒计时的id
    game_over_id = 11
    # 游戏是否结束
    is_game_over = False
    over_time = 3  # 倒计时时长

    def __init__(self):
        pygame.init()
        # 创建窗口
        self.screen = pygame.display.set_mode(Manager.bg_size, 0, 32)
        # 创建背景图片
        # self.background = pygame.image.load("./feiji/background.png")
        self.map = GameBackGround(self.screen)
        # 初始化一个装玩家精灵的group
        self.players = pygame.sprite.Group()
        # 初始化一个装敌机精灵的group
        self.enemys = pygame.sprite.Group()
        # 初始化一个玩家的爆炸对象
        self.player_bomb = Bomb(self.screen, 'player')
        # 初始化敌机的爆炸对象
        self.enemyplane_bomb = Bomb(self.screen, 'enemy')
        # 初始化一个声音播放对象
        self.sound = GameSound()

    def exit(self):
        print('退出')
        pygame.quit()
        exit()

    def show_over_text(self):
        # 游戏结束，倒计时后重新开始的文字显示
        self.drawtext('gameover%d' % Manager.over_time, 100, Manager.bg_size[1] / 2, fontheight=50,
                      fontcolor=(255, 0, 0))

    def game_over_timer(self):
        self.show_over_text()
        # 倒计时-1
        Manager.over_time -= 1
        if Manager.over_time == 0:
            # 参数2改为1
            pygame.time.set_timer(Manager.game_over_id, 0)
            # 倒计时后重新开始
            Manager.over_time = 3
            Manager.is_game_over = False
            self.start_game()

    def start_game(self):
        # 重新开始游戏，清空一些类属性
        PlayerPlane.clear_bullets()
        EnemyPlane.clear_bullets()
        manager = Manager()
        manager.main()

    def new_player(self):
        # 创建飞机对象 添加到玩家的组
        player = PlayerPlane(self.screen)
        self.players.add(player)

    def new_enemy(self):
        # 创建敌机对象 添加到敌机的组
        enemy = EnemyPlane(self.screen)
        self.enemys.add(enemy)

    def drawtext(self, text, x, y, fontheight=30, fontcolor=(255, 0, 0), background=None):
        # 通过字体文件获取字体对象
        font_obj = pygame.font.Font('./feiji/baddf.ttf', fontheight)
        # 配置要显示的字
        text_obj = font_obj.render(text, True, fontcolor, background)
        # 获取要显示对象的rect
        text_rect = text_obj.get_rect()
        # 设置显示的坐标
        text_rect.topleft = (x, y)
        # 绘制字到指定区域
        self.screen.blit(text_obj, text_rect)

    def main(self):
        # 播放音乐背景
        self.sound.playBackgroundMusic()
        # 创建一个玩家
        self.new_player()
        # 开启敌机生成定时器
        pygame.time.set_timer(Manager.create_enemy_id, 1000)
        while True:
            # 把背景图片贴到窗口
            # self.screen.blit(self.background, (0, 0))
            # 移动地图
            self.map.move()
            # 把地图贴到窗口上
            self.map.draw()
            # 绘制文字
            self.drawtext('hp:10000', 0, 0)
            if Manager.is_game_over:
                # 判断游戏结束才显示结束文字
                self.show_over_text()

            # 遍历所有事件
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit()
                elif event.type == Manager.create_enemy_id:
                    # 创建一个敌机对象
                    self.new_enemy()
                elif event.type == Manager.game_over_id:
                    # 定时器触发
                    self.game_over_timer()
            # 调用爆炸的对象
            self.player_bomb.draw()
            self.enemyplane_bomb.draw()
            # 敌机子弹与玩家飞机的碰撞
            if self.players.sprites():
                isover = pygame.sprite.spritecollide(self.players.sprites()[0], EnemyPlane.enemy_bullets, True)
                if isover:
                    Manager.is_game_over = True  # 标示着游戏结束
                    pygame.time.set_timer(Manager.game_over_id, 1000)  # 开始游戏倒计时
                    print('中弹')
                    self.player_bomb.action(self.players.sprites()[0].rect)
                    # 把玩家飞机从精灵组移除
                    self.players.remove(self.players.sprites()[0])
                    # 爆炸声音
                    self.sound.playBombSound()

            # 判断爆炸
            collide_1 = pygame.sprite.groupcollide(self.players, self.enemys, True, True)

            if collide_1:
                Manager.is_game_over = True  # 标志着游戏结束
                pygame.time.set_timer(Manager.game_over_id, 1000)  # 游戏结束倒计时
                items = list(collide_1.items())[0]
                print(items)
                x = items[0]
                y = items[1][0]
                # 玩家爆炸图片
                self.player_bomb.action(x.rect)
                self.enemyplane_bomb.action(y.rect)
                # 爆炸的声音
                self.sound.playBombSound()
            # 玩家子弹与敌机的碰撞
            if self.enemys.sprites():
                is_enemy = pygame.sprite.spritecollide(self.enemys.sprites()[0], PlayerPlane.bullets, True)
                if is_enemy:
                    self.enemyplane_bomb.action(self.enemys.sprites()[0].rect)
                    self.enemys.remove(self.enemys.sprites()[0])
                    EnemyPlane.enemy_bullets.empty()
                    self.sound.playBombSound()

            # 玩家飞机和子弹的显示
            self.players.update()
            # 敌机和敌机子弹的显示
            self.enemys.update()

            # 刷新窗口内容
            pygame.display.update()
            time.sleep(0.01)


if __name__ == '__main__':
    manage = Manager()
    manage.main()
