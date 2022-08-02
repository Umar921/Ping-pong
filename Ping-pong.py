#Создай собственный Шутер!
from pygame import *
from random import randint
win_width = 700
win_height = 500 
window = display.set_mode((win_width,win_height))
clock = time.Clock()
display.set_caption('Pingpong')
FPS = 60
game = True
finish = False

class GameSprite(sprite.Sprite):
#конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
#Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

#каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
#метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
game = True
FPS = 60
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_r(self):
            keys = key.get_pressed()
            if keys[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y <  400:
                self.rect.y += self.speed

    

racket1 = Player('racket.png', 5,win_height / 2, 30, 100 ,10)
racket2 = Player('racket.png', win_width-30, win_height / 2, 30, 100, 10)

speed_x = 3
speed_y = 3
ball = GameSprite('ball.png', 100, 100, 50, 50, 10)
while game:
    window.fill((200,255,255)) 
    if not finish:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        racket1.reset()
        racket2.reset()
        ball.reset()
        racket1.update_l()
        racket2.update_r()
        ball.update()

    if ball.rect.y > win_height - 50 or ball.rect.y <=0:
        speed_y *= -1
    if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
        speed_x *= -1

    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)
