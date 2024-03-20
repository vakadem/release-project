import pygame
from pygame import *
from random import randint
import sys
pygame.init()


class GameSprite(sprite.Sprite):
    def __init__ (self, p_image, x, y , speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.height = 37
        self.rect.width = 37
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_hight - 50:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 50:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def __init__(self, p_image, x, y, speed, width, height, direction):
        super().__init__(p_image, x, y, speed, width, height)
        self.direction = direction
    def move_1(self):
        if self.direction == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        if self.rect.y <= 50:
            self.direction = 'down'
        if self.rect.y >= 400:
            self.direction = 'up'
        
    def move_2(self):
        if self.direction == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        if self.rect.y <= 50:
            self.direction = 'down'
        if self.rect.y >= 200:
            self.direction = 'up'
    def move_2_5(self):
        if self.direction == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        if self.rect.y <= 250:
            self.direction = 'down'
        if self.rect.y >= 400:
            self.direction = 'up'
    def move_3(self):
        if self.direction == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        if self.rect.y <= 50:
            self.direction = 'down'
        if self.rect.y >= 400:
            self.direction = 'up'
    def move_4(self):
        if self.direction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        if self.rect.x <= 200:
            self.direction = 'right'
        if self.rect.x >= 450:
            self.direction = 'left'
    def move_5(self):
        if self.direction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        if self.rect.x <= 140:
            self.direction = 'right'
        if self.rect.x >= 450:
            self.direction = 'left'
        
class Wall(sprite.Sprite):
    def __init__(self, width, hight, x, y):
        super().__init__()
        self.image = Surface([width, hight])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hight = hight
        self.width = width
        self.image.fill([0, 255, 0])
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Wall_key(sprite.Sprite):
    def __init__(self, width, hight, x, y, color1, color2, color3):
        super().__init__()
        self.image = Surface([width, hight])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hight = hight
        self.width = width
        self.image.fill([color1, color2, color3])
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


        

win_width = 700
win_hight = 500
window = display.set_mode((win_width, win_hight))
mixer.init()
mixer.music.load("space.ogg")
mixer.music.set_volume(0.1)
mixer.music.play(-1)
sound_gold = mixer.Sound("money.ogg")
sound_kick = mixer.Sound("kick.ogg")

background = transform.scale(image.load("galaxy.jpg"), (win_width, win_hight))
player = Player("hero.png", 0, 225, 4, 50, 50)
enemy_1 = Enemy("cyborg.png", 150, 50, randint(8, 12), 50, 50, 'down')
enemy_2 = Enemy("cyborg.png", 300, 50, randint(3, 4), 50, 50, 'up')
enemy_2_5 = Enemy("cyborg.png", 300, 400, randint(3, 5), 50, 50, 'up')
enemy_3 = Enemy("cyborg.png", 450, 450, 5, 50, 50, 'down')
enemy_4 = Enemy("cyborg.png", 220, 0, randint(7, 8), 50, 50, 'right')
enemy_5 = Enemy("cyborg.png", 450, 450, randint(8, 10), 50, 50, 'left')
finish_gold = GameSprite("treasure.png", 650, 400, 4, 50, 50)
wall1 = Wall(5, 350, 130, 0)
wall2 = Wall(450, 5, 130, 0)
wall3 = Wall(450, 5, 130, 495)
wall4 = Wall(5, 800, 580, 100)
wall5 = Wall(230, 5, 210, 250)
wall6 = Wall(67, 5, 515, 250)
wall_key1 = Wall_key(130, 5, 0, 50, 255, 255, 0)
wall_key2 = Wall_key(5, 100, 580, 0, 255, 0, 0)
key1 = GameSprite("key1.png", 150, 5, 0, 65, 30)
key2 = GameSprite("key2.png", 20, 0, 0, 70, 35)
flag = GameSprite("flag.png", 70, 70, 0, 50, 50)

game = True
clock = time.Clock()
FPS = 60
finish = False

font.init()
f = font.Font(None, 70)
txt_win = f.render("you win", True, [255, 255, 0])
txt_lose = f.render("you lose", True, [255, 0, 0])

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall_key1, wall_key2]


while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))  
        player.reset()
        enemy_1.reset()
        enemy_2.reset()
        enemy_2_5.reset()
        enemy_3.reset()
        enemy_4.reset()
        enemy_5.reset()
        wall1.reset()
        wall2.reset()
        wall3.reset()
        wall4.reset()
        wall5.reset()
        wall6.reset()
        wall_key1.reset()
        wall_key2.reset()
        key1.reset()
        key2.reset()
        flag.reset()
        player.move()
        enemy_1.move_1()
        enemy_2.move_2()
        enemy_2_5.move_2_5()
        enemy_3.move_3()
        enemy_4.move_4()
        enemy_5.move_5()
        finish_gold.reset()
        if sprite.collide_rect(player, enemy_1) or sprite.collide_rect(player, enemy_2) or sprite.collide_rect(player, enemy_2_5) or sprite.collide_rect(player, enemy_3) or sprite.collide_rect(player, enemy_4) or sprite.collide_rect(player, enemy_5):
            sound_kick.play()
            finish = True
            window.blit(txt_lose, [250, 350])
        if sprite.collide_rect(player, finish_gold):
            sound_gold.play()
            finish_gold.rect.x = -300
        if sprite.collide_rect(player, key1):
            wall_key1.rect.x = -300
            key1.rect.x = -300
        if sprite.collide_rect(player, key2):
            wall_key2.rect.x = -300
            key2.rect.x = -300
            
        for walls_obj in walls:

            if sprite.collide_rect(player, walls_obj):
                sound_kick.play()
                finish = True
                window.blit(txt_lose, [250, 350])
                
                

                

    display.update()    
    clock.tick(FPS)