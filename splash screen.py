import os
import sys

import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)


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


fon = pygame.transform.scale(load_image('imgonline-com-ua-Blur-ykTKkV1kMcGaMH0L.jpg'), size)


def start_screen(x_pos):
    intro_text = ["ИНСТРУКЦИЯ",
                  "Перелейте каждый цвет в свою емкость.",
                  "Верхний цвет можно перелить к такому же цвету ",
                  "или в пустую емкость."]

    screen.blit(fon, (x_pos - 600, 0))
    font = pygame.font.SysFont('Comic Sans MS', 24)
    text_coord = 10
    x = [100, 30, 10, 50]
    for line in intro_text:
        string_rendered = font.render(line, 1, (1, 50, 32), pygame.Color('pink'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = -x_pos + 600 + x[intro_text.index(line)]
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


MYEVENTTYPE = pygame.USEREVENT + 1
all_sprites = pygame.sprite.Group()
running = True
clock = pygame.time.Clock()
v = 160
x_pos = 0
pygame.time.set_timer(MYEVENTTYPE, 15000)
c = 0
while running:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == MYEVENTTYPE:
            c = 1
        if event.type == pygame.QUIT:
            running = False
    if x_pos <= 600 or c == 2:
        start_screen(x_pos)
    elif c == 1:
        x_pos = 600
        c = 2
    else:
        start_screen(600)
    all_sprites.draw(screen)
    all_sprites.update(int(x_pos))
    x_pos += (v * clock.tick() / 1000) * 2
    pygame.display.flip()
pygame.quit()
