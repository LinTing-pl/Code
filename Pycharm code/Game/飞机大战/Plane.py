#!/Users/env python
# -*- coding:utf-8 -*-
# @author：麟听 WeChat:15019763969
import random
import time

import pygame


class Player(pygame.sprite.Sprite):
    bullets = pygame.sprite.Group()

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.plane_image = pygame.image.load('./feiji/hero1.png')
        self.rect = self.plane_image.get_rect()
        self.rect.topleft = (Manage.screen_size[0] / 2 - self.rect.center[0], Manage.screen_size[1] * 0.7)
        self.bullets = pygame.sprite.Group()
        self.plane_speed = 8

    def key_control(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            self.rect.left -= self.plane_speed
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            self.rect.left += self.plane_speed
        if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
            self.rect.top -= self.plane_speed
        if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
            self.rect.top += self.plane_speed
        if key_pressed[pygame.K_SPACE]:
            bullet = Bullet(self.screen, self.rect)
            self.bullets.add(bullet)
            Player.bullets.add(bullet)

    def display(self):
        self.screen.blit(self.plane_image, self.rect)
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
        self.screen = screen
        self.plane_image = pygame.image.load('./feiji/enemy0.png')
        self.rect = self.plane_image.get_rect()
        self.rect.topleft = (random.randint(0, (Manage.screen_size[0] - self.rect[2])), -self.rect[3] / 2)
        self.bullets = pygame.sprite.Group()
        self.plane_speed = 2.5
        self.move_option = random.choice([True, False])
        self.plane_direction = 'right'

    def auto_move(self):
        self.rect.top += self.plane_speed
        if self.move_option:
            if self.rect[0] > random.randint(int(Manage.screen_size[0] * 2 / 3), Manage.screen_size[0]):
                self.plane_direction = 'left'
            if self.rect[0] < random.randint(0, int(Manage.screen_size[0] * 1 / 3)):
                self.plane_direction = 'right'
            if self.plane_direction == 'right':
                self.rect.left += self.plane_speed / 2
            if self.plane_direction == 'left':
                self.rect.left -= self.plane_speed / 2

    def auto_fire(self):
        if random.randint(0, 50) == 10:
            bullet = EnemyPlaneBullet(self.screen, self.rect)
            self.bullets.add(bullet)
            EnemyPlane.bullets.add(bullet)

    def display(self):
        self.screen.blit(self.plane_image, self.rect)
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
        self.screen = screen
        self.bullet_image = pygame.image.load('./feiji/bullet.png')
        self.rect = self.bullet_image.get_rect()
        self.rect.topleft = (rect.centerx - self.rect.centerx, rect.top - self.rect[3] / 2)
        self.bullet_speed = 15

    def auto_move(self):
        self.rect.top -= self.bullet_speed

    def display(self):
        self.screen.blit(self.bullet_image, self.rect)

    def update(self):
        self.auto_move()
        self.display()


class EnemyPlaneBullet(pygame.sprite.Sprite):
    def __init__(self, screen, rect):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.bullet_image = pygame.image.load('./feiji/bullet1.png')
        self.rect = self.bullet_image.get_rect()
        self.rect.topleft = (rect.centerx - self.rect.centerx, rect.top + self.rect[3])
        self.bullet_speed = 5

    def auto_move(self):
        self.rect.top += self.bullet_speed

    def display(self):
        self.screen.blit(self.bullet_image, self.rect)

    def update(self):
        self.auto_move()
        self.display()


# class Collide(pygame.sprite.Group):
#     def __init__(self, group1, group2, option1, option2):
#         pygame.sprite.Group.__init__(self)
#         self.group1 = group1
#         self.group2 = group2
#         self.option1 = option1
#         self.option2 = option2
#
#     def iscollide(self):
#         return pygame.sprite.groupcollide(self.group1, self.group2, self.option1, self.option2)


class Boom(object):
    def __init__(self, screen, obj):
        self.screen = screen
        self.obj = obj
        self.rect = []
        if self.obj == 'Player':
            self.boom_image_list1 = [pygame.image.load('./feiji/hero_blowup_n' + str(i) + '.png') for i in range(1, 5)]
        elif self.obj == 'EnemyPlane':
            self.boom_image_list2 = [pygame.image.load('./feiji/enemy0_down' + str(i) + '.png') for i in range(1, 5)]
        self.option = False

    def switch(self, rect):
        self.option = True
        self.rect = rect

    def display(self):
        if self.option:
            return
        else:
            for i in range(len(self.boom_image_list)):
                self.screen.blit(self.boom_image_list1[i], self.rect)
            self.option = False


class Map(object):
    def __init__(self, screen):
        self.screen = screen
        self.image_level1 = pygame.image.load('./feiji/img_bg_level_1.jpg')
        self.image_level1_1 = self.image_level1
        self.img_l1_y1 = 0
        self.img_l1_y2 = -self.image_level1_1.get_rect().bottom

    def auto_move(self):
        if self.img_l1_y1 <= self.image_level1_1.get_rect().bottom:
            self.img_l1_y1 += 0.8
            self.img_l1_y2 += 0.8
            if self.img_l1_y1 > self.image_level1_1.get_rect().bottom:
                self.img_l1_y1 = 0
                self.img_l1_y2 = -self.image_level1_1.get_rect().bottom

    def display(self):
        self.screen.blit(self.image_level1, (0, self.img_l1_y1))
        self.screen.blit(self.image_level1_1, (0, self.img_l1_y2))

    def update(self):
        self.auto_move()
        self.display()


class Manage(object):
    screen_size = (512, 768)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(Manage.screen_size)
        pygame.display.set_caption('飞机大战')
        self.map = Map(self.screen)
        self.players = pygame.sprite.Group()
        self.enemyplanes = pygame.sprite.Group()
        self.enemy_generate_ID = 10
        # self.collide1 = Collide(self.players, self.enemyplanes, True, True)
        # self.collide2 = Collide(self.players, EnemyPlane.bullets, True, True)
        # self.collide3 = Collide(Player.bullets, self.enemyplanes, True, True)
        self.player_boom = Boom(self.screen, 'Player')
        self.enemyplane_boom = Boom(self.screen, 'EnemyPlane')

    def player_generate(self):
        plane = Player(self.screen)
        self.players.add(plane)

    def enemyplane_generate(self):
        plane = EnemyPlane(self.screen)
        self.enemyplanes.add(plane)

    # def iscollide(self, group1, group2, option1, option2):
    #     pygame.sprite.groupcollide(group1, group2, option1, option2)

    def main(self):
        self.player_generate()
        pygame.time.set_timer(self.enemy_generate_ID, 1800)
        while True:
            self.map.update()
            for event in pygame.event.get():
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    exit()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == self.enemy_generate_ID:
                    self.enemyplane_generate()
            collide1 = pygame.sprite.groupcollide(self.players, self.enemyplanes, True, True)
            if collide1:
                Player.bullets.empty()
                EnemyPlane.bullets.empty()
            collide2 = pygame.sprite.groupcollide(Player.bullets, self.enemyplanes, True, True)
            if collide2:
                EnemyPlane.bullets.empty()
            collide3 = pygame.sprite.groupcollide(self.players, EnemyPlane.bullets, True, True)
            if collide3:
                Player.bullets.empty()

            # if self.collide1.iscollide():
            #     print(self.collide1.iscollide())
            #     # self.player_boom.switch()
            #     # Player.bullets.empty()
            #     # EnemyPlane.bullets.empty()
            # if self.collide2.iscollide():
            #     print(self.collide1.iscollide())
            #     # Player.bullets.empty()
            # if self.collide3.iscollide():
            #     print(self.collide1.iscollide())
            #     # EnemyPlane.bullets.empty()
            self.players.update()
            self.enemyplanes.update()
            time.sleep(0.01)
            pygame.display.update()


if __name__ == '__main__':
    manage = Manage()
    manage.main()
