import os
import random
import sys

import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
sound1 = pygame.mixer.Sound('Sound_07433 (mp3cut.net).wav')


def load_image(name, colorkey=None, fl=False):
    fullname = os.path.join(name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    if fl:
        image = pygame.transform.flip(image, True, False)
    return image


class Bomb(pygame.sprite.Sprite):
    image_1 = load_image("buttle.jpg")
    image_boom = load_image("buttle.jpg")
    image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.5, 0.5)

    def __init__(self, group, x, y):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        print(self.rect)
        self.rect.x = x
        self.rect.y = y
        self.flag = True
        self.name = count

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            if self.flag:
                self.rect.y -= 20
                rect_sprite.update(self.name, self.flag)
                self.flag = False
                sound1.play()
            else:
                rect_sprite.update(self.name, self.flag)
                self.rect.y += 20
                self.flag = True
                sound1.play()


class Player(pygame.sprite.Sprite):
    def __init__(self, group, x, y, color):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = pygame.Surface((54, 59))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.flag = True
        self.name = count

    def update(self, *args):
        if args[0] == self.name and args[1]:
            self.rect.y -= 20
        elif args[0] == self.name:
            self.rect.y += 20


all_sprites = pygame.sprite.Group()
rect_sprite = pygame.sprite.Group()
r_x = 200
count = 1
color = ['GREEN', 'RED', 'BLUE', 'ORANGE', 'beige', 'Brown', 'yellow']
for _ in range(5):
    Bomb(all_sprites, r_x, 200)
    c = 400
    for j in range(4):
        Player(rect_sprite, r_x + 40, c, random.choice(color))
        c -= 54
    r_x += 100
    count += 1
running = True
fps = 60
clock = pygame.time.Clock()
CLK = 70
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    rect_sprite.draw(screen)
    all_sprites.update()

    clock.tick(fps)
    pygame.display.flip()
pygame.quit()
