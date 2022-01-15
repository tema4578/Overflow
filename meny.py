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
            colorkey = image.get_at((50, 50))
            print(colorkey)
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    if fl:
        image = pygame.transform.flip(image, True, False)
    return image


def help(screen):
    font = pygame.font.SysFont('Comic Sans MS', 40)
    text = font.render(f"Уровни", True, (1, 50, 32))
    text_2 = font.render(f"Переливашки!!", True, (255, 186, 0), (128, 166, 255))
    text_3 = pygame.font.SysFont('Comic Sans MS', 37).render(f"Результаты", True, (1, 50, 32))
    text_x = 600 // 2 - text.get_width() // 2
    text_y = 400 // 2 - text.get_height() // 2
    screen.blit(text, (text_x + 110, text_y // 2))
    screen.blit(text_2, (text_x - 80, text_y // 2 - 70))
    screen.blit(text_3, (text_x - 140, text_y // 2))


def help_23(screen):
    font = pygame.font.SysFont('Comic Sans MS', 45)
    text = font.render(f"Уровни", True, (1, 50, 32))
    text_2 = pygame.font.SysFont('Comic Sans MS', 40).render(f"Назад", True, (1, 50, 32))
    c = 100
    for i in range(5):
        screen.blit(font.render(f"{i}", True, (1, 50, 32)), (c, 100))
        c += 100
    screen.blit(text, (230, 20))
    screen.blit(text_2, (400, 230))


def fanction():
    sprite_Button = pygame.sprite.Group()
    sprite_Button_levels = pygame.sprite.Group()
    pygame.init()
    size = 600, 350
    screen = pygame.display.set_mode(size)
    running = True

    class Button_levels(pygame.sprite.Sprite):
        def __init__(self, group, x, y, image, name):
            super().__init__(group)
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.name = name
            self.flag = True

        def flag(self):
            return self.flag

        def update(self, *args):
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos):
                if a1.flag and not self.name:
                    a1.flag = False
                elif not self.name:
                    a1.flag = True
            if args and args[0].type == pygame.MOUSEMOTION and \
                    self.rect.collidepoint(args[0].pos):
                self.image = self.image
            else:
                self.image = self.image

    class Button(pygame.sprite.Sprite):
        def __init__(self, group, x, y, image):
            super().__init__(group)
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.flag = True

        def flag(self):
            return self.flag

        def update(self, *args):
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos):

                if a1.flag:
                    a1.flag = False
                else:
                    a1.flag = True
            if args and args[0].type == pygame.MOUSEMOTION and \
                    self.rect.collidepoint(args[0].pos):
                self.image = self.image
            else:
                self.image = self.image

    class FON(pygame.sprite.Sprite):

        def __init__(self, group, x, y, image):
            super().__init__(group)
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    FON(sprite_Button_levels, 0, 0,
        pygame.transform.scale(
            load_image(f"warm-save-wallpaper-dark-texture_1258-284.jpg"),
            (600, 400)))
    c = 80
    for _ in range(1, 6):
        Button_levels(sprite_Button_levels, c, 100,
                      pygame.transform.scale(load_image(
                          f"yellow-and-black-square-geometric-shapes-on-bac3kgrou4nd_52701-867.jpg"),
                          (70, 70)), _)
        c += 100

    FON(sprite_Button, 0, 0,
        pygame.transform.scale(load_image("black-and-white-splashes-ink_76542-209.jpg"),
                               (600, 400)))
    FON(sprite_Button, 0, 250,
        pygame.transform.scale(load_image("736.jpg", -1), (1832 // 6, 712 // 6)))
    Button(sprite_Button, 100, 160, pygame.transform.scale(load_image("254216.jpg", -1), (150, 70)))
    a1 = Button(sprite_Button, 340, 160,
                pygame.transform.scale(load_image("2524316.jpg", -1), (150, 70)))
    Button_levels(sprite_Button_levels, 400, 230,
                       pygame.transform.scale(load_image(
                           "yellow-and-black-square-geometric-shapes-on-bac3kgrou4nd_52701-867.jpg"),
                           (120, 70)), False)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                sprite_Button.update(event)
                sprite_Button_levels.update(event)
            if event.type == pygame.MOUSEMOTION:
                sprite_Button.update(event, True)
        if not a1.flag:
            screen.fill((0, 0, 0))
            sprite_Button_levels.draw(screen)
            help_23(screen)
        else:
            sprite_Button.draw(screen)
            help(screen)
        pygame.display.flip()
    pygame.quit()


fanction()
