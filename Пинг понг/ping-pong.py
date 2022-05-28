from pygame import *
from random import randint

back_image = 'bb.jpg'
ball_image = 'ball.png'
player_image = 'палка.png'

clock = time.Clock()
FPS = 100

win_length = 700
win_width = 700
window = display.set_mode((win_length, win_width))
display.set_caption('Ping-Pong')
background = transform.scale(image.load(back_image), (win_length, win_width))

mixer.init()
mixer.music.load('mus.ogg')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys_l = key.get_pressed()
        if keys_l[K_s] and self.rect.y < win_width - 150:
            self.rect.y += self.speed
        if keys_l[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    def update_right(self):
        keys_l = key.get_pressed()
        if keys_l[K_DOWN] and self.rect.y < win_width - 150:
            self.rect.y += self.speed
        if keys_l[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed


palyer1 = Player(player_image, 50, 400 , 130, 130, 3)
palyer2 = Player(player_image, 500, 400, 130, 130, 3)
ball = GameSprite(ball_image, 400, 200, 100, 70, 2)

speed_x = 2
speed_y = 2
score_1 = 0
score_2 = 0
max_lost = 7


font.init()
font = font.SysFont('Arial',35)
lose1 = font.render('PLAYER 1 LOSE!', True, (120, 0, 53))
lose2 = font.render('PLAYER 2 LOSE!', True, (120, 0, 53))

run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:
        palyer1.update_left()
        palyer2.update_right()
        window.blit(background,(0,0))

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(palyer1, ball) or sprite.collide_rect(palyer2, ball):
            speed_x *= -1
            speed_y *= 1
        
        if ball.rect.y > win_width-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (250,400))
            
        if ball.rect.x > win_length:
            finish = True
            window.blit(lose2, (250, 400)) 

        palyer1.reset()
        palyer2.reset()
        ball.reset()



    display.update()
    clock.tick(FPS)
