import os
import random
import sys

import pygame

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
sound1 = pygame.mixer.Sound('Sound_07433 (mp3cut.net).wav')


def load_image(name, colorkey=None, fl=False):
    fullname = os.path.join(name)
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


fon = pygame.transform.scale(load_image('imgonline-com-ua-Blur-ykTKkV1kMcGaMH0L.jpg'), size)


def defr(cc):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    string_rendere = font.render(f'Отменить ход: {cc}', 1, pygame.Color('white'))
    screen.blit(string_rendere, (170, 10))


count_23 = 45

fgf = False


def start_screen(x_pos, flag, flag2):
    global count_23, fgf, co
    if flag2:
        if count_23 != 0:
            count_23 -= 5
            co += 1
        else:
            fgf = True
    intro_text = [f'{count_23}']

    if flag:
        intro_text = ["ИНСТРУКЦИЯ",
                      "Перелейте каждый цвет в свою емкость.",
                      "Верхний цвет можно перелить к такому же цвету ",
                      "или в пустую емкость."]
    if flag:
        screen.blit(fon, (x_pos - 600, 0))
        font = pygame.font.SysFont('Comic Sans MS', 24)
        text_coord = 10
    else:
        text_coord = -12
        font = pygame.font.SysFont('Comic Sans MS', 40)

    x = [100, 30, 10, 50]
    for line in intro_text:
        if flag:
            string_rendered = font.render(line, 1, (1, 50, 32), pygame.Color('pink'))
        elif count_23 == 0:
            string_rendered = font.render(line, 1, pygame.Color('red'))
        else:
            string_rendered = font.render(line, 1, pygame.Color('gold'))

        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        if flag:
            intro_rect.x = -x_pos + 600 + x[intro_text.index(line)]
        else:
            intro_rect.x = 15
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(buttons)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, *args):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            start_screen(24, False, True)


class Bomb(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image("Снимок экрана (77).png"), (30, 100))
    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.flag = True
        self.name = count

    def update(self, *args):
        global rgr
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            if self.flag:
                rgr = True
                self.rect.y -= 20
                rect_sprite.update(self.name, self.flag)
                self.flag = False
                sound1.play()
            else:
                rgr = False
                rect_sprite.update(self.name, self.flag)
                self.rect.y += 20
                self.flag = True
                sound1.play()


class Player(pygame.sprite.Sprite):
    def __init__(self, group, x, y, color):
        super().__init__(group)
        self.image = pygame.Surface((28, 23))
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
buttons = pygame.sprite.Group()
r_x = 200
count = 1
dragon1 = AnimatedSprite(
    pygame.transform.scale(load_image('photoeditorsdk-export.png', -1), (40, 40)), 1, 1, 110, 5)
dragon2 = AnimatedSprite(
    pygame.transform.scale(load_image('photoeditorsdk-export (1).png', -1), (40, 40)), 1, 1, 65, 5)
color = ['GREEN', 'RED', 'BLUE', 'ORANGE', 'beige', 'Brown', 'yellow']
for _ in range(3):
    Bomb(all_sprites, r_x, 200)
    c = 287
    for j in range(4):
        Player(rect_sprite, r_x + 15, c, random.choice(color))
        c -= 23
    r_x += 100
    count += 1
running = True
fps = 60
clock = pygame.time.Clock()
CLK = 20
co = 5
rgr = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)
            buttons.update(event)
    screen.fill((0, 0, 0))
    buttons.draw(screen)
    buttons.update()
    all_sprites.draw(screen)
    rect_sprite.draw(screen)
    all_sprites.update()
    start_screen(24, False, False)
    #clock.tick(5)
    defr(co)
    pygame.display.flip()
pygame.quit()
