import os
import sys

import pygame


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


def help(screen, number, time):
    font = pygame.font.SysFont('Comic Sans MS', 35)
    text = font.render(f"Bы прошли уровень {number}", 1, (100, 255, 100))
    text_2 = font.render(f"Время {time}", 1, (255, 186, 0), (128, 166, 255))
    text_3 = pygame.font.SysFont('Comic Sans MS', 30).render(f"Выход", 1, (1, 50, 32))
    text_x = 600 // 2 - text.get_width() // 2
    text_y = 400 // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y // 2 - 50))
    screen.blit(text_2, (text_x + 100, text_y // 2 + 40))
    screen.blit(text_3, (430, 260))


def fanction(number, time):
    sprite_Button = pygame.sprite.Group()
    pygame.init()
    size = 600, 350
    screen = pygame.display.set_mode(size)
    running = True

    class Button(pygame.sprite.Sprite):
        image = pygame.transform.scale(load_image("2109.w032.n003.116B.p1.116.jpg"), (100, 50))
        image_2 = pygame.transform.scale(load_image("2109.w032.n003.116B.p1.116 — копия.jpg"), (100, 50))

        def __init__(self, group, x, y):
            super().__init__(group)
            self.image = Button.image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.flag = True

        def flag(self):
            return self.flag

        def update(self, *args):
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos):
                self.flag = False
            if args and args[0].type == pygame.MOUSEMOTION and \
                    self.rect.collidepoint(args[0].pos):
                self.image = Button.image_2
            else:
                self.image = Button.image

    class FON(pygame.sprite.Sprite):
        image = pygame.transform.scale(load_image("5447769.jpg"), (600, 400))

        def __init__(self, group, x, y):
            super().__init__(group)
            self.image = FON.image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    FON(sprite_Button, 0, 0)
    a1 = Button(sprite_Button, 430, 260)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                sprite_Button.update(event)
            if event.type == pygame.MOUSEMOTION:
                sprite_Button.update(event, True)
        if not a1.flag:
            running = False
        sprite_Button.draw(screen)
        help(screen, number, time)
        pygame.display.flip()
    pygame.quit()


fanction(10, 45)
