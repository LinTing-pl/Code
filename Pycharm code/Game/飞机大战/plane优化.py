import pygame
from pygame.constants import *
import random
import time


class Plane(pygame.sprite.Sprite):
    bullets = pygame.sprite.Group()

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.plane = pygame.image.load('./feiji/hero1.png')
        self.screen = screen
        self.rect = self.plane.get_rect()
        self.rect.topleft = [Manage.map_size[0] / 2 - 100 / 2, 560]
        self.speed = 8
        self.bullets = pygame.sprite.Group()

    def key_control(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            self.rect.top -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.rect.top += self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.rect.left -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.rect.left += self.speed
        if key_pressed[K_SPACE]:
            bullet = Bullet(self.screen, self.rect)
            self.bullets.add(bullet)
            Plane.bullets = self.bullets

    def display(self):
        self.screen.blit(self.plane, self.rect)
        for bullet in self.bullets:
            bullet.update()

    def update(self):
        self.key_control()
        self.display()

    @classmethod
    def cleanbullets(cls):
        cls.bullets.empty()


class EnemyPlane(pygame.sprite.Sprite):
    bullets = pygame.sprite.Group()

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.plane = pygame.image.load('./feiji/enemy0.png')
        self.screen = screen
        self.rect = self.plane.get_rect()
        self.rect.topleft = (random.randint(0, 512 - 51), 0)
        self.speed = 7
        self.dirction = 'right'
        self.bullets = pygame.sprite.Group()

    def auto_move(self):
        self.rect.top += 4
        if self.dirction == 'right':
            self.rect.left += self.speed
        elif self.dirction == 'left':
            self.rect.left -= self.speed
        if self.rect.left >= random.randint(400, 480 - 21):
            self.dirction = 'left'
        elif self.rect.left <= random.randint(0, 75):
            self.dirction = 'right'

    def auto_fire(self):
        if random.randint(1, 20) == 8:
            bullet = EnemyBullet(self.screen, self.rect)
            self.bullets.add(bullet)
            EnemyPlane.bullets = self.bullets

    def display(self):
        self.screen.blit(self.plane, self.rect)
        for bullet in self.bullets:
            bullet.update()

    def update(self):
        self.auto_move()
        self.auto_fire()
        self.display()

    @classmethod
    def cleanbullets(cls):
        cls.bullets.empty()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, rect):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 15
        self.bullet = pygame.image.load('./feiji/bullet.png')
        self.rect = self.bullet.get_rect()
        self.rect.topleft = [rect.left + 100 / 2 - 22 / 2, rect.top - 22]
        self.screen = screen

    def display(self):
        self.screen.blit(self.bullet, self.rect)

    def auto_move(self):
        self.rect.top -= self.speed

    def update(self):
        self.auto_move()
        self.display()


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, screen, rect):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 8
        self.bullet = pygame.image.load('./feiji/bullet1.png')
        self.rect = self.bullet.get_rect()
        self.rect.topleft = [rect.left + 50 / 2 - 8 / 2, rect.top + 21]
        self.screen = screen

    def display(self):
        self.screen.blit(self.bullet, self.rect)

    def auto_move(self):
        self.rect.top += self.speed

    def update(self):
        self.auto_move()
        self.display()


class Bomb(object):
    def __init__(self, screen, boom):
        self.screen = screen
        if boom == 'player':
            self.Images = [pygame.image.load('./feiji/hero_blowup_n' + str(i) + '.png') for i in range(1, 5)]
        else:
            self.Images = [pygame.image.load('./feiji/enemy0_down' + str(i) + '.png') for i in range(1, 5)]
        self.position = [0, 0]
        self.Index = 0
        self.swicth = False

    def action(self, rect):
        self.swicth = True
        self.position = rect

    def draw(self):
        if not self.swicth:
            return
        else:
            self.screen.blit(self.Images[self.Index], self.position)
            self.Index += 1
            if self.Index >= len(self.Images):
                self.Index = 0
                self.swicth = False


class GameSound(object):
    def __init__(self):
        pygame.mixer.music.load('./feiji/bg2.ogg')
        pygame.mixer.music.set_volume(0.5)
        self.__bomb = pygame.mixer.Sound('./feiji/bomb.wav')

    def bkgroundmusic(self):
        pygame.mixer.music.play(-1)

    def bombsound(self):
        pygame.mixer.Sound.play(self.__bomb)


class Map(object):
    def __init__(self, screen):
        self.screen = screen
        self.image1 = pygame.image.load('./feiji/img_bg_level_1.jpg')
        self.image2 = pygame.image.load('./feiji/img_bg_level_1.jpg')
        self.y1 = 0
        self.y2 = -Manage.map_size[1]

    def auto_move(self):
        if self.y1 <= Manage.map_size[1]:
            self.y1 += 1
            self.y2 += 1
            if self.y1 > Manage.map_size[1]:
                self.y1 = 0
                self.y2 = -Manage.map_size[1]

    def display(self):
        self.screen.blit(self.image1, (0, self.y1))
        self.screen.blit(self.image2, (0, self.y2))


class Manage(object):
    map_size = (512, 768)
    enemyplane_settime_id = 10

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(Manage.map_size, 0, 32)
        self.map = Map(self.screen)
        self.players = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        self.player_boom = Bomb(self.screen, 'player')
        self.enemy_boom = Bomb(self.screen, 'enemy')
        self.sound = GameSound()

    def new_player(self):
        player = Plane(self.screen)
        self.players.add(player)

    def new_enemy(self):
        enemy = EnemyPlane(self.screen)
        self.enemys.add(enemy)

    def draw_text(self, text, x, y, textheight=30, fontcolor=(255, 0, 255), bkgroundcolor=None):
        font_obj = pygame.font.Font('./feiji/baddf.ttf', textheight)
        text_obj = font_obj.render(text, True, fontcolor, bkgroundcolor)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_obj, text_rect)

    def main(self):
        pygame.display.set_caption('Game')
        self.sound.bkgroundmusic()
        self.new_player()
        pygame.time.set_timer(Manage.enemyplane_settime_id, 1500)
        while True:
            self.map.auto_move()
            self.map.display()
            self.draw_text('hp:10000', 0, 0)
            for event in pygame.event.get():
                if pygame.key.get_pressed()[K_ESCAPE]:
                    exit()
                elif event.type == pygame.QUIT:
                    exit()
                elif event.type == Manage.enemyplane_settime_id:
                    self.new_enemy()
            self.player_boom.draw()
            self.enemy_boom.draw()
            iscollide1 = pygame.sprite.groupcollide(self.players, self.enemys, True, True)
            if iscollide1:
                # 玩家飞机与敌机的碰撞
                item = list(iscollide1.items())[0]
                self.player_boom.action(item[0].rect)
                self.enemy_boom.action(item[1][0].rect)
                self.sound.bombsound()
                Plane.bullets.empty()
                EnemyPlane.bullets.empty()
            iscollide2 = pygame.sprite.groupcollide(self.enemys, Plane.bullets, False, False)
            if iscollide2:
                # 玩家子弹与敌机的碰撞
                item = list(iscollide2.items())[0]
                self.enemy_boom.action(item[0].rect)
                self.sound.bombsound()
                EnemyPlane.bullets.empty()
            if self.players.sprites():
                iscollide3 = pygame.sprite.spritecollide(self.players.sprites()[0], EnemyPlane.bullets, True)
                if iscollide3:
                    # 玩家与敌机子弹的碰撞
                    self.player_boom.action(self.players.sprites()[0].rect)
                    self.players.remove(self.players.sprites()[0])
                    self.sound.bombsound()
                    Plane.bullets.empty()
            self.players.update()
            self.enemys.update()
            time.sleep(0.01)
            pygame.display.update()


if __name__ == '__main__':
    manage = Manage()
    manage.main()
