from random import randint
from pygame import *
import pygame
import sys


#Главное
font.init()
font = font.Font(None,75)
clock = time.Clock()
FPS = 60

window = display.set_mode((750, 500))

display.set_caption('Пинг-Понг(Иван Лучший)')

#Цвета
white = (255, 255, 255)
black = (0, 0, 0)

#Классы для спрайтов(3)
class Raketka1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.points = 0


class Raketka2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.points = 0


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.speed = 2
        self.dx = 1
        self.dy = 1


#Создание Спрайтов
raketka1 = Raketka1()
raketka1.rect.x = 25
raketka1.rect.y = 225

raketka2 = Raketka2()
raketka2.rect.x = 715
raketka2.rect.y = 225
raketka_speed = 10


pong = Ball()
pong.rect.x = 375
pong.rect.y = 250

#Группа Спрайтов
all_sprites = sprite.Group()
all_sprites.add(raketka1, raketka2, pong)

#Функция обновляющая экран постоянно с частотой монитора(60) обновляет экран в ЧЕРНЫЙ(0,0,0)

def redraw():
    #Рисует черный экран
    window.fill(black)

    #Шрифт Посередине
    font = pygame.font.SysFont('Times New Roman', 30)
    text = font.render('ПингПонг за 3 копейки', False, white)
    textRect = text.get_rect()
    textRect.center = (750 // 2,25)
    window.blit(text, textRect)

    #Счет 1го игрока
    p1_score = font.render(str(raketka1.points), False, white)
    p1Rect = p1_score.get_rect()
    p1Rect.center = (50, 50)
    window.blit(p1_score, p1Rect)

    #Счёт 2го игрока
    p2_score = font.render(str(raketka2.points), False, white)
    p2Rect = p2_score.get_rect()
    p2Rect.center = (700, 50)
    window.blit(p2_score, p2Rect)

    #Обновлять все СПРАЙТЫ
    all_sprites.draw(window)

    #Обновления
    pygame.display.update()


game = True

#Игровой цикл
while game:

    # pygame.time.delay(100)

    #Отслеживание на выход
    for e in  event.get():
        if e.type == QUIT:
            game = False


    #Ракетка Движение
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        raketka1.rect.y -= raketka_speed
    if key[pygame.K_s]:
        raketka1.rect.y += raketka_speed
    if key[pygame.K_UP]:
        raketka2.rect.y -= raketka_speed
    if key[pygame.K_DOWN]:
        raketka2.rect.y += raketka_speed

    #Перемещает мячик для понга
    pong.rect.x += pong.speed * pong.dx
    pong.rect.y += pong.speed * pong.dy

    #Отскоки от стены и ракетки
    if pong.rect.y > 490:
        pong.dy = -1

    if pong.rect.y < 1:
        pong.dy = 1

    if pong.rect.x > 740:
        pong.rect.x, pong.rect.y = 375, 250
        pong.dx = -1
        raketka1.points += 1

    if pong.rect.x < 1:
        pong.rect.x, pong.rect.y = 375, 250
        pong.dx = 1
        raketka2.points += 1

    if raketka1.rect.colliderect(pong.rect):
        pong.dx = 1

    if raketka2.rect.colliderect(pong.rect):
        pong.dx = -1

    #Запускает функцию перерисовки выше
    redraw()
    clock.tick(FPS)

#создал примерно за 7 часов(3 дня по 2-3 часа) НУЖНО ДОРАБОТАТЬ МУЗЫКУ И КРАСИВЫЙ ФОН