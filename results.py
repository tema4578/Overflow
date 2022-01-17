import sys
from random import choice
import datetime as dt
import os
import pygame

list_records = [34, 34, 22, 23, 23]


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
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    if fl:
        image = pygame.transform.flip(image, True, False)
    return image


def help(screen):
    font = pygame.font.SysFont('Comic Sans MS', 40)
    text = font.render(f"Уровни", True, (0, 0, 0))
    text_2 = font.render(f"Переливалки!", True, (0, 0, 0))
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
    for i in range(1, 6):
        screen.blit(font.render(f"{i}", True, (1, 50, 32)), (c, 100))
        c += 100
    screen.blit(text, (230, 20))
    screen.blit(text_2, (400, 230))


def help_43(screen):
    font = pygame.font.SysFont('Comic Sans MS', 32)
    text_2 = pygame.font.SysFont('Comic Sans MS', 35).render(f"Назад", True, (0, 0, 0))
    screen.blit(text_2, (450, 250))
    c = 50
    for i in range(1, 6):
        screen.blit(font.render(f"{i}", True, (245, 245, 220)), (100, c))
        screen.blit(pygame.font.SysFont('Comic Sans MS', 31).render(f"{list_records[i - 1]}", True,
                                                                    (245, 245, 220)), (140, c + 2))
        c += 50
    d = 50
    for i in range(5):
        pygame.draw.line(screen, (245, 245, 220), (90, d), (400, d), 2)
        d += 50
    pygame.draw.line(screen, (245, 245, 220), (130, 20), (130, 280), 2)
    text_3 = pygame.font.SysFont('Comic Sans MS', 26).render(f"№", True, (245, 245, 220))
    screen.blit(text_3, (95, 15))
    text_4 = pygame.font.SysFont('Comic Sans MS', 26).render(f"Лучшее время", True, (245, 245, 220))
    screen.blit(text_4, (140, 15))


def fanction():
    sprite_Button = pygame.sprite.Group()
    sprite_Button_levels = pygame.sprite.Group()
    sprite_Button_resultats = pygame.sprite.Group()
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
                    self.rect.collidepoint(args[0].pos) and not self.name:
                a1.flag = True
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos) and self.name == 1 and self.name:
                lstsup = [0, 0, 0]
                lstred = []
                lstgreen = []
                lst = [0, 0, 0, 0, 1, 1, 1, 1]
                lst1 = [1, 1, 1, 1]
                lst2 = [1, 1, 1, 1]
                lst3 = [0, 0, 0, 0]
                CLK = 70
                one_x = 260
                one_y = 380
                two_x = 260
                two_y = 330
                three_x = 260
                three_y = 280
                four_x = 260
                four_y = 230
                q = 0
                five_x = 360
                five_y = 380
                six_x = 360
                six_y = 330
                seven_x = 360
                seven_y = 280
                eight_x = 360
                eight_y = 230
                pygame.init()
                pygame.display.set_caption('first level')
                screen = pygame.display.set_mode((800, 600))
                time = int(str(str(dt.datetime.now().time()).split(':')[-1]).split('.')[0]) + int(
                    str(str(dt.datetime.now().time()).split(':')[1])) * 60 + int(
                    str(str(dt.datetime.now().time()).split(':')[0])) * 360

                class Player(pygame.sprite.Sprite):
                    def __init__(self, group, x, y, color):
                        super().__init__(group)
                        self.image = pygame.Surface((54, 50))
                        self.image.fill(color)
                        self.rect = self.image.get_rect()
                        self.rect.center = (x, y)
                        self.flag = True

                    def q(self, x, y):
                        self.rect.center = (x, y)

                rect_sprite = pygame.sprite.Group()

                def load_image(name, colorkey=None):
                    image = pygame.image.load('buttle.jpg')
                    if colorkey is not None:
                        image = image.convert()
                        if colorkey == -1:
                            colorkey = image.get_at((1, 1))
                    else:
                        image = image.convert_alpha()
                    return image

                class buttle1(pygame.sprite.Sprite):
                    if os.name == 'posix':
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.5, 0.5)
                    else:
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.53, 0.52)

                    def __init__(self, group, x, y):
                        super().__init__(group)
                        self.image = buttle1.image
                        self.rect = self.image.get_rect()
                        self.rect.x = x
                        self.rect.y = y
                        global y1
                        y1 = self.rect.y
                        self.count = 1
                        self.b11 = 0
                        self.b12 = 0

                    def update(self, *args):
                        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                                self.rect.collidepoint(args[0].pos):
                            global five_y, five_x, six_y, six_x, seven_y, seven_x, eight_x, eight_y, \
                                one_y, one_x, two_y, two_x, three_y, three_x, four_x, four_y, y1, q, sup
                            if lst1[3] == 1:
                                self.b11 = 0
                                self.b12 = 0
                                if 'one' in lstred and one_x == 260:
                                    self.b11 += 1
                                if 'one' in lstgreen and one_x == 260:
                                    self.b12 += 1
                                if 'two' in lstred and two_x == 260:
                                    self.b11 += 1
                                if 'two' in lstgreen and two_x == 260:
                                    self.b12 += 1
                                if 'three' in lstred and three_x == 260:
                                    self.b11 += 1
                                if 'three' in lstgreen and three_x == 260:
                                    self.b12 += 1
                                if 'four' in lstred and four_x == 260:
                                    self.b11 += 1
                                if 'four' in lstgreen and four_x == 260:
                                    self.b12 += 1
                                if 'five' in lstred and five_x == 260:
                                    self.b11 += 1
                                if 'five' in lstgreen and five_x == 260:
                                    self.b12 += 1
                                if 'six' in lstred and six_x == 260:
                                    self.b11 += 1
                                if 'six' in lstgreen and six_x == 260:
                                    self.b12 += 1
                                if 'seven' in lstred and seven_x == 260:
                                    self.b11 += 1
                                if 'seven' in lstgreen and seven_x == 260:
                                    self.b12 += 1
                                if 'eight' in lstred and eight_x == 260:
                                    self.b11 += 1
                                if 'eight' in lstgreen and eight_x == 260:
                                    self.b12 += 1
                            if self.b11 != 4 and self.b12 != 4:
                                if q == 0:
                                    if self.count % 2 != 0:
                                        q = 1
                                        self.rect.y -= 50
                                        self.count += 1
                                        y1 -= 50
                                        if one_x == 260:
                                            one_y -= 50
                                        if two_x == 260:
                                            two_y -= 50
                                        if three_x == 260:
                                            three_y -= 50
                                        if four_x == 260:
                                            four_y -= 50
                                        if five_x == 260:
                                            five_y -= 50
                                        if six_x == 260:
                                            six_y -= 50
                                        if seven_x == 260:
                                            seven_y -= 50
                                        if eight_x == 260:
                                            eight_y -= 50
                                else:
                                    if self.count % 2 == 0:
                                        q = 0
                                        self.rect.y += 50
                                        y1 += 50
                                        if one_x == 260:
                                            one_y += 50
                                        if two_x == 260:
                                            two_y += 50
                                        if three_x == 260:
                                            three_y += 50
                                        if four_x == 260:
                                            four_y += 50
                                        if five_x == 260:
                                            five_y += 50
                                        if six_x == 260:
                                            six_y += 50
                                        if seven_x == 260:
                                            seven_y += 50
                                        if eight_x == 260:
                                            eight_y += 50
                                        self.count += 1
                                    else:
                                        if self.count % 2 == 0:
                                            q = 0
                                            self.rect.y += 50
                                            y1 += 50
                                            if one_x == 360:
                                                one_y += 50
                                            if two_x == 360:
                                                two_y += 50
                                            if three_x == 360:
                                                three_y += 50
                                            if four_x == 360:
                                                four_y += 50
                                            if five_x == 360:
                                                five_y += 50
                                            if six_x == 360:
                                                six_y += 50
                                            if seven_x == 360:
                                                seven_y += 50
                                            if eight_x == 360:
                                                eight_y += 50
                                            self.count += 1
                                        else:
                                            global y3, y2
                                            if lst1[3] == 0:
                                                if lst1[2] == 0:
                                                    if lst1[1] == 0:
                                                        if lst1[0] == 0:
                                                            w = 0
                                                            z = 0
                                                            if y2 == 150:
                                                                z = 360
                                                                if lst2[3] == 1:
                                                                    w = 180
                                                                    lst1[0] = 1
                                                                    lst2[3] = 0
                                                                elif lst2[2] == 1:
                                                                    w = 230
                                                                    lst1[0] = 1
                                                                    lst2[2] = 0
                                                                elif lst2[1] == 1:
                                                                    w = 280
                                                                    lst1[0] = 1
                                                                    lst2[1] = 0
                                                                elif lst2[0] == 1:
                                                                    w = 330
                                                                    lst1[0] = 1
                                                                    lst2[0] = 0
                                                            elif y3 == 150:
                                                                z = 460
                                                                if lst3[3] == 1:
                                                                    w = 180
                                                                    lst3[3] = 0
                                                                    lst1[0] = 1
                                                                elif lst3[2] == 1:
                                                                    w = 230
                                                                    lst3[2] = 0
                                                                    lst1[0] = 1
                                                                elif lst3[1] == 1:
                                                                    w = 280
                                                                    lst3[1] = 0
                                                                    lst1[0] = 1
                                                                elif lst3[0] == 1:
                                                                    w = 330
                                                                    lst3[0] = 0
                                                                    lst1[0] = 1
                                                            if one_y == w and one_x == z:
                                                                one_x = 260
                                                                one_y = 380
                                                            elif two_y == w and two_x == z:
                                                                two_x = 260
                                                                two_y = 380
                                                            elif three_y == w and three_x == z:
                                                                three_x = 260
                                                                three_y = 380
                                                            elif four_y == w and four_x == z:
                                                                four_x = 260
                                                                four_y = 380
                                                            elif five_y == w and five_x == z:
                                                                five_x = 260
                                                                five_y = 380
                                                            elif six_y == w and six_x == z:
                                                                six_x = 260
                                                                six_y = 380
                                                            elif seven_y == w and seven_x == z:
                                                                seven_x = 260
                                                                seven_y = 380
                                                            elif eight_y == w and eight_x == z:
                                                                eight_x = 260
                                                                eight_y = 380
                                                        else:
                                                            w = 0
                                                            z = 0
                                                            q = ''
                                                            if y2 == 150:
                                                                z = 360
                                                                if lst2[3] == 1:
                                                                    w = 180
                                                                elif lst2[2] == 1:
                                                                    w = 230
                                                                elif lst2[1] == 1:
                                                                    w = 280
                                                                elif lst2[0] == 1:
                                                                    w = 330
                                                            elif y3 == 150:
                                                                z = 460
                                                                if lst3[3] == 1:
                                                                    w = 180
                                                                elif lst3[2] == 1:
                                                                    w = 230
                                                                elif lst3[1] == 1:
                                                                    w = 280
                                                                elif lst3[0] == 1:
                                                                    w = 330
                                                            q2 = 0
                                                            if one_x == 260:
                                                                q = 'one'
                                                            elif two_x == 260:
                                                                q = 'two'
                                                            elif three_x == 260:
                                                                q = 'three'
                                                            elif four_x == 260:
                                                                q = 'four'
                                                            elif five_x == 260:
                                                                q = 'five'
                                                            elif six_x == 260:
                                                                q = 'six'
                                                            elif seven_x == 260:
                                                                q = 'seven'
                                                            elif eight_x == 260:
                                                                q = 'eight'
                                                            if one_y == w and one_x == z:
                                                                if 'one' in lstred and q in lstred or \
                                                                        'one' in lstgreen and q in lstgreen:
                                                                    q2 = 1
                                                                    one_x = 260
                                                                    one_y = 330
                                                            elif two_y == w and two_x == z:
                                                                if 'two' in lstred and q in lstred or \
                                                                        'two' in lstgreen and q in lstgreen:
                                                                    q2 = 1
                                                                    two_x = 260
                                                                    two_y = 330
                                                            elif three_y == w and three_x == z:
                                                                if 'three' in lstred and q in lstred or \
                                                                        'three' in lstgreen and q in lstgreen:
                                                                    q2 = 1
                                                                    three_x = 260
                                                                    three_y = 330
                                                            elif four_y == w and four_x == z:
                                                                if 'four' in lstred and q in lstred or \
                                                                        'four' in lstgreen and q in lstgreen:
                                                                    q2 = 1
                                                                    four_x = 260
                                                                    four_y = 330
                                                            elif five_y == w and five_x == z:
                                                                if 'five' in lstred and q in lstred or \
                                                                        'five' in lstgreen and q in lstgreen:
                                                                    five_x = 260
                                                                    five_y = 330
                                                            elif six_y == w and six_x == z:
                                                                if 'six' in lstred and q in lstred or \
                                                                        'six' in lstgreen and q in lstgreen:
                                                                    q2 = 1
                                                                    six_x = 260
                                                                    six_y = 330
                                                            elif seven_y == w and seven_x == z:
                                                                if 'seven' in lstred and q in lstred or \
                                                                        'seven' in lstgreen and q in lstgreen:
                                                                    q2 = 1
                                                                    seven_x = 260
                                                                    seven_y = 330
                                                            elif eight_y == w and eight_x == z:
                                                                if 'eight' in lstred and q in lstred or \
                                                                        'eight' in lstgreen and q in lstgreen:
                                                                    q2 = 1
                                                                    eight_x = 260
                                                                    eight_y = 330
                                                            if q2 == 1:
                                                                if y2 == 150:
                                                                    if lst2[3] == 1:
                                                                        w = 180
                                                                        lst1[1] = 1
                                                                        lst2[3] = 0
                                                                    elif lst2[2] == 1:
                                                                        w = 230
                                                                        lst1[1] = 1
                                                                        lst2[2] = 0
                                                                    elif lst2[1] == 1:
                                                                        w = 280
                                                                        lst1[1] = 1
                                                                        lst2[1] = 0
                                                                    elif lst2[0] == 1:
                                                                        w = 330
                                                                        lst1[1] = 1
                                                                        lst2[0] = 0
                                                                elif y3 == 150:
                                                                    if lst3[3] == 1:
                                                                        w = 180
                                                                        lst3[3] = 0
                                                                        lst1[1] = 1
                                                                    elif lst3[2] == 1:
                                                                        w = 230
                                                                        lst3[2] = 0
                                                                        lst1[1] = 1
                                                                    elif lst3[1] == 1:
                                                                        w = 280
                                                                        lst3[1] = 0
                                                                        lst1[1] = 1
                                                                    elif lst3[0] == 1:
                                                                        w = 330
                                                                        lst3[0] = 0
                                                                        lst1[1] = 1
                                                    else:
                                                        w = 0
                                                        z = 0
                                                        q = ''
                                                        if y2 == 150:
                                                            z = 360
                                                            if lst2[3] == 1:
                                                                w = 180
                                                            elif lst2[2] == 1:
                                                                w = 230
                                                            elif lst2[1] == 1:
                                                                w = 280
                                                            elif lst2[0] == 1:
                                                                w = 330
                                                        elif y3 == 150:
                                                            z = 460
                                                            if lst3[3] == 1:
                                                                w = 180
                                                            elif lst3[2] == 1:
                                                                w = 230
                                                            elif lst3[1] == 1:
                                                                w = 280
                                                            elif lst3[0] == 1:
                                                                w = 330
                                                        q2 = 0
                                                        if one_x == 260:
                                                            q = 'one'
                                                        elif two_x == 260:
                                                            q = 'two'
                                                        elif three_x == 260:
                                                            q = 'three'
                                                        elif four_x == 260:
                                                            q = 'four'
                                                        elif five_x == 260:
                                                            q = 'five'
                                                        elif six_x == 260:
                                                            q = 'six'
                                                        elif seven_x == 260:
                                                            q = 'seven'
                                                        elif eight_x == 260:
                                                            q = 'eight'
                                                        if one_y == w and one_x == z:
                                                            if 'one' in lstred and q in lstred or \
                                                                    'one' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                one_x = 260
                                                                one_y = 280
                                                        elif two_y == w and two_x == z:
                                                            if 'two' in lstred and q in lstred or \
                                                                    'two' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                two_x = 260
                                                                two_y = 280
                                                        elif three_y == w and three_x == z:
                                                            if 'three' in lstred and q in lstred or \
                                                                    'three' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                three_x = 260
                                                                three_y = 280
                                                        elif four_y == w and four_x == z:
                                                            if 'four' in lstred and q in lstred or \
                                                                    'four' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                four_x = 260
                                                                four_y = 280
                                                        elif five_y == w and five_x == z:
                                                            if 'five' in lstred and q in lstred or \
                                                                    'five' in lstgreen and q in lstgreen:
                                                                five_x = 260
                                                                five_y = 280
                                                        elif six_y == w and six_x == z:
                                                            if 'six' in lstred and q in lstred or \
                                                                    'six' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                six_x = 260
                                                                six_y = 280
                                                        elif seven_y == w and seven_x == z:
                                                            if 'seven' in lstred and q in lstred or \
                                                                    'seven' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                seven_x = 260
                                                                seven_y = 280
                                                        elif eight_y == w and eight_x == z:
                                                            if 'eight' in lstred and q in lstred or \
                                                                    'eight' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                eight_x = 260
                                                                eight_y = 280
                                                        if q2 == 1:
                                                            if y2 == 150:
                                                                if lst2[3] == 1:
                                                                    w = 180
                                                                    lst1[2] = 1
                                                                    lst2[3] = 0
                                                                elif lst2[2] == 1:
                                                                    w = 230
                                                                    lst1[2] = 1
                                                                    lst2[2] = 0
                                                                elif lst2[1] == 1:
                                                                    w = 280
                                                                    lst1[2] = 1
                                                                    lst2[1] = 0
                                                                elif lst2[0] == 1:
                                                                    w = 330
                                                                    lst1[2] = 1
                                                                    lst2[0] = 0
                                                            elif y3 == 150:
                                                                if lst3[3] == 1:
                                                                    w = 180
                                                                    lst3[3] = 0
                                                                    lst1[2] = 1
                                                                elif lst3[2] == 1:
                                                                    w = 230
                                                                    lst3[2] = 0
                                                                    lst1[2] = 1
                                                                elif lst3[1] == 1:
                                                                    w = 280
                                                                    lst3[1] = 0
                                                                    lst1[2] = 1
                                                                elif lst3[0] == 1:
                                                                    w = 330
                                                                    lst3[0] = 0
                                                                    lst1[2] = 1
                                                else:
                                                    w = 0
                                                    z = 0
                                                    q = ''
                                                    if one_x == 260:
                                                        q = 'one'
                                                    elif two_x == 260:
                                                        q = 'two'
                                                    elif three_x == 260:
                                                        q = 'three'
                                                    elif four_x == 260:
                                                        q = 'four'
                                                    elif five_x == 260:
                                                        q = 'five'
                                                    elif six_x == 260:
                                                        q = 'six'
                                                    elif seven_x == 260:
                                                        q = 'seven'
                                                    elif eight_x == 260:
                                                        q = 'eight'
                                                    if y2 == 150:
                                                        z = 360
                                                        if lst2[3] == 1:
                                                            w = 180
                                                        elif lst2[2] == 1:
                                                            w = 230
                                                        elif lst2[1] == 1:
                                                            w = 280
                                                        elif lst2[0] == 1:
                                                            w = 330
                                                    elif y3 == 150:
                                                        z = 460
                                                        if lst3[3] == 1:
                                                            w = 180
                                                        elif lst3[2] == 1:
                                                            w = 230
                                                        elif lst3[1] == 1:
                                                            w = 280
                                                        elif lst3[0] == 1:
                                                            w = 330
                                                    q2 = 0
                                                    if one_y == w and one_x == z:
                                                        if 'one' in lstred and q in lstred or \
                                                                'one' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            one_x = 260
                                                            one_y = 230
                                                    elif two_y == w and two_x == z:
                                                        if 'two' in lstred and q in lstred or \
                                                                'two' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            two_x = 260
                                                            two_y = 230
                                                    elif three_y == w and three_x == z:
                                                        if 'three' in lstred and q in lstred or \
                                                                'three' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            three_x = 260
                                                            three_y = 230
                                                    elif four_y == w and four_x == z:
                                                        if 'four' in lstred and q in lstred or \
                                                                'four' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            four_x = 260
                                                            four_y = 230
                                                    elif five_y == w and five_x == z:
                                                        if 'five' in lstred and q in lstred or \
                                                                'five' in lstgreen and q in lstgreen:
                                                            five_x = 260
                                                            five_y = 230
                                                    elif six_y == w and six_x == z:
                                                        if 'six' in lstred and q in lstred or \
                                                                'six' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            six_x = 260
                                                            six_y = 230
                                                    elif seven_y == w and seven_x == z:
                                                        if 'seven' in lstred and q in lstred or \
                                                                'seven' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            seven_x = 260
                                                            seven_y = 230
                                                    elif eight_y == w and eight_x == z:
                                                        if 'eight' in lstred and q in lstred or \
                                                                'eight' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            eight_x = 260
                                                            eight_y = 230
                                                    if q2 == 1:
                                                        if y2 == 150:
                                                            if lst2[3] == 1:
                                                                w = 180
                                                                lst1[3] = 1
                                                                lst2[3] = 0
                                                            elif lst2[2] == 1:
                                                                w = 230
                                                                lst1[3] = 1
                                                                lst2[2] = 0
                                                            elif lst2[1] == 1:
                                                                w = 280
                                                                lst1[3] = 1
                                                                lst2[1] = 0
                                                            elif lst2[0] == 1:
                                                                w = 330
                                                                lst1[3] = 1
                                                                lst2[0] = 0
                                                        elif y3 == 150:
                                                            if lst3[3] == 1:
                                                                w = 180
                                                                lst3[3] = 0
                                                                lst1[3] = 1
                                                            elif lst3[2] == 1:
                                                                w = 230
                                                                lst3[2] = 0
                                                                lst1[3] = 1
                                                            elif lst3[1] == 1:
                                                                w = 280
                                                                lst3[1] = 0
                                                                lst1[3] = 1
                                                            elif lst3[0] == 1:
                                                                w = 330
                                                                lst3[0] = 0
                                                                lst1[3] = 1
                            else:
                                lstsup[0] = 1
                                sup = 0
                                for i in lstsup:
                                    if i == 1:
                                        sup += 1
                                if sup == 2:
                                    time2 = int(
                                        str(str(dt.datetime.now().time()).split(':')[-1]).split(
                                            '.')[0]) + int(
                                        str(str(dt.datetime.now().time()).split(':')[
                                                1])) * 60 + int(
                                        str(str(dt.datetime.now().time()).split(':')[0])) * 360
                                    result = time2 - time
                                    q = result % 60
                                    if q < 10:
                                        fanction(1, f'{result // 60}:0{q}')
                                    else:
                                        fanction(1, f'{result // 60}:{q}')

                class buttle2(pygame.sprite.Sprite):
                    if os.name == 'posix':
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.5, 0.5)
                    else:
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.53, 0.52)

                    def __init__(self, group, x, y):
                        super().__init__(group)
                        self.image = buttle2.image
                        self.rect = self.image.get_rect()
                        self.rect.x = x
                        self.rect.y = y
                        global y2
                        y2 = self.rect.y
                        self.count = 1
                        self.b21 = 0
                        self.b22 = 0

                    def update(self, *args):
                        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                                self.rect.collidepoint(args[0].pos):
                            global five_y, five_x, six_y, six_x, seven_y, seven_x, eight_x, eight_y, \
                                one_y, one_x, two_y, two_x, three_y, three_x, four_x, four_y, y2, q, sup
                            if lst2[3] == 1:
                                self.b21 = 0
                                self.b22 = 0
                                if 'one' in lstred and one_x == 360:
                                    self.b21 += 1
                                if 'one' in lstgreen and one_x == 360:
                                    self.b22 += 1
                                if 'two' in lstred and two_x == 360:
                                    self.b21 += 1
                                if 'two' in lstgreen and two_x == 360:
                                    self.b22 += 1
                                if 'three' in lstred and three_x == 360:
                                    self.b21 += 1
                                if 'three' in lstgreen and three_x == 360:
                                    self.b22 += 1
                                if 'four' in lstred and four_x == 360:
                                    self.b21 += 1
                                if 'four' in lstgreen and four_x == 360:
                                    self.b22 += 1
                                if 'five' in lstred and five_x == 360:
                                    self.b21 += 1
                                if 'five' in lstgreen and five_x == 360:
                                    self.b22 += 1
                                if 'six' in lstred and six_x == 360:
                                    self.b21 += 1
                                if 'six' in lstgreen and six_x == 360:
                                    self.b22 += 1
                                if 'seven' in lstred and seven_x == 360:
                                    self.b21 += 1
                                if 'seven' in lstgreen and seven_x == 360:
                                    self.b22 += 1
                                if 'eight' in lstred and eight_x == 360:
                                    self.b21 += 1
                                if 'eight' in lstgreen and eight_x == 360:
                                    self.b22 += 1
                            if self.b21 != 4 and self.b22 != 4:
                                if q == 0:
                                    if self.count % 2 != 0:
                                        q = 1
                                        self.rect.y -= 50
                                        self.count += 1
                                        y2 -= 50
                                        if one_x == 360:
                                            one_y -= 50
                                        if two_x == 360:
                                            two_y -= 50
                                        if three_x == 360:
                                            three_y -= 50
                                        if four_x == 360:
                                            four_y -= 50
                                        if five_x == 360:
                                            five_y -= 50
                                        if six_x == 360:
                                            six_y -= 50
                                        if seven_x == 360:
                                            seven_y -= 50
                                        if eight_x == 360:
                                            eight_y -= 50
                                else:
                                    if self.count % 2 == 0:
                                        q = 0
                                        self.rect.y += 50
                                        y2 += 50
                                        if one_x == 360:
                                            one_y += 50
                                        if two_x == 360:
                                            two_y += 50
                                        if three_x == 360:
                                            three_y += 50
                                        if four_x == 360:
                                            four_y += 50
                                        if five_x == 360:
                                            five_y += 50
                                        if six_x == 360:
                                            six_y += 50
                                        if seven_x == 360:
                                            seven_y += 50
                                        if eight_x == 360:
                                            eight_y += 50
                                        self.count += 1
                                    else:
                                        global y3, y1
                                        if lst2[3] == 0:
                                            if lst2[2] == 0:
                                                if lst2[1] == 0:
                                                    if lst2[0] == 0:
                                                        w = 0
                                                        z = 0
                                                        if y1 == 150:
                                                            z = 260
                                                            if lst1[3] == 1:
                                                                w = 180
                                                                lst2[0] = 1
                                                                lst1[3] = 0
                                                            elif lst1[2] == 1:
                                                                w = 230
                                                                lst2[0] = 1
                                                                lst1[2] = 0
                                                            elif lst1[1] == 1:
                                                                w = 280
                                                                lst2[0] = 1
                                                                lst1[1] = 0
                                                            elif lst1[0] == 1:
                                                                w = 330
                                                                lst2[0] = 1
                                                                lst1[0] = 0
                                                        elif y3 == 150:
                                                            z = 460
                                                            if lst3[3] == 1:
                                                                w = 180
                                                                lst3[3] = 0
                                                                lst2[0] = 1
                                                            elif lst3[2] == 1:
                                                                w = 230
                                                                lst3[2] = 0
                                                                lst2[0] = 1
                                                            elif lst3[1] == 1:
                                                                w = 280
                                                                lst3[1] = 0
                                                                lst2[0] = 1
                                                            elif lst3[0] == 1:
                                                                w = 330
                                                                lst3[0] = 0
                                                                lst2[0] = 1
                                                        if one_y == w and one_x == z:
                                                            one_x = 260
                                                            one_y = 380
                                                        elif two_y == w and two_x == z:
                                                            two_x = 260
                                                            two_y = 380
                                                        elif three_y == w and three_x == z:
                                                            three_x = 260
                                                            three_y = 380
                                                        elif four_y == w and four_x == z:
                                                            four_x = 260
                                                            four_y = 380
                                                        elif five_y == w and five_x == z:
                                                            five_x = 260
                                                            five_y = 380
                                                        elif six_y == w and six_x == z:
                                                            six_x = 260
                                                            six_y = 380
                                                        elif seven_y == w and seven_x == z:
                                                            seven_x = 260
                                                            seven_y = 380
                                                        elif eight_y == w and eight_x == z:
                                                            eight_x = 260
                                                            eight_y = 380
                                                    else:
                                                        w = 0
                                                        z = 0
                                                        q = ''
                                                        if y1 == 150:
                                                            z = 260
                                                            if lst1[3] == 1:
                                                                w = 180
                                                            elif lst1[2] == 1:
                                                                w = 230
                                                            elif lst1[1] == 1:
                                                                w = 280
                                                            elif lst1[0] == 1:
                                                                w = 330
                                                        elif y3 == 150:
                                                            z = 460
                                                            if lst3[3] == 1:
                                                                w = 180
                                                            elif lst3[2] == 1:
                                                                w = 230
                                                            elif lst3[1] == 1:
                                                                w = 280
                                                            elif lst3[0] == 1:
                                                                w = 330
                                                        q2 = 0
                                                        if one_x == 360:
                                                            q = 'one'
                                                        elif two_x == 360:
                                                            q = 'two'
                                                        elif three_x == 360:
                                                            q = 'three'
                                                        elif four_x == 360:
                                                            q = 'four'
                                                        elif five_x == 360:
                                                            q = 'five'
                                                        elif six_x == 360:
                                                            q = 'six'
                                                        elif seven_x == 360:
                                                            q = 'seven'
                                                        elif eight_x == 360:
                                                            q = 'eight'
                                                        if one_y == w and one_x == z:
                                                            if 'one' in lstred and q in lstred or \
                                                                    'one' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                one_x = 360
                                                                one_y = 330
                                                        elif two_y == w and two_x == z:
                                                            if 'two' in lstred and q in lstred or \
                                                                    'two' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                two_x = 360
                                                                two_y = 330
                                                        elif three_y == w and three_x == z:
                                                            if 'three' in lstred and q in lstred or \
                                                                    'three' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                three_x = 360
                                                                three_y = 330
                                                        elif four_y == w and four_x == z:
                                                            if 'four' in lstred and q in lstred or \
                                                                    'four' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                four_x = 360
                                                                four_y = 330
                                                        elif five_y == w and five_x == z:
                                                            if 'five' in lstred and q in lstred or \
                                                                    'five' in lstgreen and q in lstgreen:
                                                                five_x = 360
                                                                five_y = 330
                                                        elif six_y == w and six_x == z:
                                                            if 'six' in lstred and q in lstred or \
                                                                    'six' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                six_x = 360
                                                                six_y = 330
                                                        elif seven_y == w and seven_x == z:
                                                            if 'seven' in lstred and q in lstred or \
                                                                    'seven' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                seven_x = 360
                                                                seven_y = 330
                                                        elif eight_y == w and eight_x == z:
                                                            if 'eight' in lstred and q in lstred or \
                                                                    'eight' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                eight_x = 360
                                                                eight_y = 330
                                                        if q2 == 1:
                                                            if y1 == 150:
                                                                if lst1[3] == 1:
                                                                    w = 180
                                                                    lst2[1] = 1
                                                                    lst1[3] = 0
                                                                elif lst1[2] == 1:
                                                                    w = 230
                                                                    lst2[1] = 1
                                                                    lst1[2] = 0
                                                                elif lst1[1] == 1:
                                                                    w = 280
                                                                    lst2[1] = 1
                                                                    lst1[1] = 0
                                                                elif lst1[0] == 1:
                                                                    w = 330
                                                                    lst2[1] = 1
                                                                    lst1[0] = 0
                                                            elif y3 == 150:
                                                                if lst3[3] == 1:
                                                                    w = 180
                                                                    lst3[3] = 0
                                                                    lst2[1] = 1
                                                                elif lst3[2] == 1:
                                                                    w = 230
                                                                    lst3[2] = 0
                                                                    lst2[1] = 1
                                                                elif lst3[1] == 1:
                                                                    w = 280
                                                                    lst3[1] = 0
                                                                    lst2[1] = 1
                                                                elif lst3[0] == 1:
                                                                    w = 330
                                                                    lst3[0] = 0
                                                                    lst2[1] = 1
                                                else:
                                                    w = 0
                                                    z = 0
                                                    q = ''
                                                    if y1 == 150:
                                                        z = 260
                                                        if lst1[3] == 1:
                                                            w = 180
                                                        elif lst1[2] == 1:
                                                            w = 230
                                                        elif lst1[1] == 1:
                                                            w = 280
                                                        elif lst1[0] == 1:
                                                            w = 330
                                                    elif y3 == 150:
                                                        z = 460
                                                        if lst3[3] == 1:
                                                            w = 180
                                                        elif lst3[2] == 1:
                                                            w = 230
                                                        elif lst3[1] == 1:
                                                            w = 280
                                                        elif lst3[0] == 1:
                                                            w = 330
                                                    q2 = 0
                                                    if one_x == 360:
                                                        q = 'one'
                                                    elif two_x == 360:
                                                        q = 'two'
                                                    elif three_x == 360:
                                                        q = 'three'
                                                    elif four_x == 360:
                                                        q = 'four'
                                                    elif five_x == 360:
                                                        q = 'five'
                                                    elif six_x == 360:
                                                        q = 'six'
                                                    elif seven_x == 360:
                                                        q = 'seven'
                                                    elif eight_x == 360:
                                                        q = 'eight'
                                                    if one_y == w and one_x == z:
                                                        if 'one' in lstred and q in lstred or \
                                                                'one' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            one_x = 360
                                                            one_y = 280
                                                    elif two_y == w and two_x == z:
                                                        if 'two' in lstred and q in lstred or \
                                                                'two' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            two_x = 360
                                                            two_y = 280
                                                    elif three_y == w and three_x == z:
                                                        if 'three' in lstred and q in lstred or \
                                                                'three' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            three_x = 360
                                                            three_y = 280
                                                    elif four_y == w and four_x == z:
                                                        if 'four' in lstred and q in lstred or \
                                                                'four' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            four_x = 360
                                                            four_y = 280
                                                    elif five_y == w and five_x == z:
                                                        if 'five' in lstred and q in lstred or \
                                                                'five' in lstgreen and q in lstgreen:
                                                            five_x = 360
                                                            five_y = 280
                                                    elif six_y == w and six_x == z:
                                                        if 'six' in lstred and q in lstred or \
                                                                'six' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            six_x = 360
                                                            six_y = 280
                                                    elif seven_y == w and seven_x == z:
                                                        if 'seven' in lstred and q in lstred or \
                                                                'seven' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            seven_x = 360
                                                            seven_y = 280
                                                    elif eight_y == w and eight_x == z:
                                                        if 'eight' in lstred and q in lstred or \
                                                                'eight' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            eight_x = 360
                                                            eight_y = 280
                                                    if q2 == 1:
                                                        if y1 == 150:
                                                            if lst1[3] == 1:
                                                                w = 180
                                                                lst2[2] = 1
                                                                lst1[3] = 0
                                                            elif lst1[2] == 1:
                                                                w = 230
                                                                lst2[2] = 1
                                                                lst1[2] = 0
                                                            elif lst1[1] == 1:
                                                                w = 280
                                                                lst2[2] = 1
                                                                lst1[1] = 0
                                                            elif lst1[0] == 1:
                                                                w = 330
                                                                lst2[2] = 1
                                                                lst1[0] = 0
                                                        elif y3 == 150:
                                                            if lst3[3] == 1:
                                                                w = 180
                                                                lst3[3] = 0
                                                                lst2[2] = 1
                                                            elif lst3[2] == 1:
                                                                w = 230
                                                                lst3[2] = 0
                                                                lst2[2] = 1
                                                            elif lst3[1] == 1:
                                                                w = 280
                                                                lst3[1] = 0
                                                                lst2[2] = 1
                                                            elif lst3[0] == 1:
                                                                w = 330
                                                                lst3[0] = 0
                                                                lst2[2] = 1
                                            else:
                                                w = 0
                                                z = 0
                                                q = ''
                                                if y1 == 150:
                                                    z = 260
                                                    if lst1[3] == 1:
                                                        w = 180
                                                    elif lst1[2] == 1:
                                                        w = 230
                                                    elif lst1[1] == 1:
                                                        w = 280
                                                    elif lst1[0] == 1:
                                                        w = 330
                                                elif y3 == 150:
                                                    z = 460
                                                    if lst3[3] == 1:
                                                        w = 180
                                                    elif lst3[2] == 1:
                                                        w = 230
                                                    elif lst3[1] == 1:
                                                        w = 280
                                                    elif lst3[0] == 1:
                                                        w = 330
                                                q2 = 0
                                                if one_x == 360:
                                                    q = 'one'
                                                elif two_x == 360:
                                                    q = 'two'
                                                elif three_x == 360:
                                                    q = 'three'
                                                elif four_x == 360:
                                                    q = 'four'
                                                elif five_x == 360:
                                                    q = 'five'
                                                elif six_x == 360:
                                                    q = 'six'
                                                elif seven_x == 360:
                                                    q = 'seven'
                                                elif eight_x == 360:
                                                    q = 'eight'
                                                if one_y == w and one_x == z:
                                                    if 'one' in lstred and q in lstred or \
                                                            'one' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        one_x = 360
                                                        one_y = 230
                                                elif two_y == w and two_x == z:
                                                    if 'two' in lstred and q in lstred or \
                                                            'two' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        two_x = 360
                                                        two_y = 230
                                                elif three_y == w and three_x == z:
                                                    if 'three' in lstred and q in lstred or \
                                                            'three' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        three_x = 360
                                                        three_y = 230
                                                elif four_y == w and four_x == z:
                                                    if 'four' in lstred and q in lstred or \
                                                            'four' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        four_x = 360
                                                        four_y = 230
                                                elif five_y == w and five_x == z:
                                                    if 'five' in lstred and q in lstred or \
                                                            'five' in lstgreen and q in lstgreen:
                                                        five_x = 360
                                                        five_y = 230
                                                elif six_y == w and six_x == z:
                                                    if 'six' in lstred and q in lstred or \
                                                            'six' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        six_x = 360
                                                        six_y = 230
                                                elif seven_y == w and seven_x == z:
                                                    if 'seven' in lstred and q in lstred or \
                                                            'seven' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        seven_x = 360
                                                        seven_y = 230
                                                elif eight_y == w and eight_x == z:
                                                    if 'eight' in lstred and q in lstred or \
                                                            'eight' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        eight_x = 360
                                                        eight_y = 230
                                                if q2 == 1:
                                                    if y1 == 150:
                                                        if lst1[3] == 1:
                                                            w = 180
                                                            lst2[3] = 1
                                                            lst1[3] = 0
                                                        elif lst1[2] == 1:
                                                            w = 230
                                                            lst2[3] = 1
                                                            lst1[2] = 0
                                                        elif lst1[1] == 1:
                                                            w = 280
                                                            lst2[3] = 1
                                                            lst1[1] = 0
                                                        elif lst1[0] == 1:
                                                            w = 330
                                                            lst2[3] = 1
                                                            lst1[0] = 0
                                                    elif y3 == 150:
                                                        if lst3[3] == 1:
                                                            w = 180
                                                            lst3[3] = 0
                                                            lst2[3] = 1
                                                        elif lst3[2] == 1:
                                                            w = 230
                                                            lst3[2] = 0
                                                            lst2[3] = 1
                                                        elif lst3[1] == 1:
                                                            w = 280
                                                            lst3[1] = 0
                                                            lst2[3] = 1
                                                        elif lst3[0] == 1:
                                                            w = 330
                                                            lst3[0] = 0
                                                            lst2[3] = 1
                            else:
                                lstsup[1] = 1
                                sup = 0
                                for i in lstsup:
                                    if i == 1:
                                        sup += 1
                                if sup == 2:
                                    time2 = int(
                                        str(str(dt.datetime.now().time()).split(':')[-1]).split(
                                            '.')[0]) + int(
                                        str(str(dt.datetime.now().time()).split(':')[
                                                1])) * 60 + int(
                                        str(str(dt.datetime.now().time()).split(':')[0])) * 360
                                    result = time2 - time
                                    q = result % 60
                                    if q < 10:
                                        fanction(1, f'{result // 60}:0{q}')
                                    else:
                                        fanction(1, f'{result // 60}:{q}')

                class buttle3(pygame.sprite.Sprite):
                    if os.name == 'posix':
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.5, 0.5)
                    else:
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.53, 0.52)

                    def __init__(self, group, x, y):
                        super().__init__(group)
                        self.image = buttle3.image
                        self.rect = self.image.get_rect()
                        self.rect.x = x
                        self.rect.y = y
                        global y3
                        y3 = self.rect.y
                        self.count = 1
                        self.b31 = 0
                        self.b32 = 0

                    def update(self, *args):
                        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                                self.rect.collidepoint(args[0].pos):
                            global five_y, five_x, six_y, six_x, seven_y, seven_x, eight_x, eight_y, \
                                one_y, one_x, two_y, two_x, three_y, three_x, four_x, four_y, y3, q, sup
                            if lst3[3] == 1:
                                self.b31 = 0
                                self.b32 = 0
                                if 'one' in lstred and one_x == 460:
                                    self.b31 += 1
                                if 'one' in lstgreen and one_x == 460:
                                    self.b32 += 1
                                if 'two' in lstred and two_x == 460:
                                    self.b31 += 1
                                if 'two' in lstgreen and two_x == 460:
                                    self.b32 += 1
                                if 'three' in lstred and three_x == 460:
                                    self.b31 += 1
                                if 'three' in lstgreen and three_x == 460:
                                    self.b32 += 1
                                if 'four' in lstred and four_x == 460:
                                    self.b31 += 1
                                if 'four' in lstgreen and four_x == 460:
                                    self.b32 += 1
                                if 'five' in lstred and five_x == 460:
                                    self.b31 += 1
                                if 'five' in lstgreen and five_x == 460:
                                    self.b32 += 1
                                if 'six' in lstred and six_x == 460:
                                    self.b31 += 1
                                if 'six' in lstgreen and six_x == 460:
                                    self.b32 += 1
                                if 'seven' in lstred and seven_x == 460:
                                    self.b31 += 1
                                if 'seven' in lstgreen and seven_x == 460:
                                    self.b32 += 1
                                if 'eight' in lstred and eight_x == 460:
                                    self.b31 += 1
                                if 'eight' in lstgreen and eight_x == 460:
                                    self.b32 += 1
                            if self.b31 != 4 and self.b32 != 4:
                                if q == 0:
                                    if self.count % 2 != 0:
                                        q = 1
                                        self.rect.y -= 50
                                        self.count += 1
                                        y3 -= 50
                                        if one_x == 460:
                                            one_y -= 50
                                        if two_x == 460:
                                            two_y -= 50
                                        if three_x == 460:
                                            three_y -= 50
                                        if four_x == 460:
                                            four_y -= 50
                                        if five_x == 460:
                                            five_y -= 50
                                        if six_x == 460:
                                            six_y -= 50
                                        if seven_x == 460:
                                            seven_y -= 50
                                        if eight_x == 460:
                                            eight_y -= 50
                                else:
                                    if self.count % 2 == 0:
                                        q = 0
                                        self.rect.y += 50
                                        y3 += 50
                                        if one_x == 460:
                                            one_y += 50
                                        if two_x == 460:
                                            two_y += 50
                                        if three_x == 460:
                                            three_y += 50
                                        if four_x == 460:
                                            four_y += 50
                                        if five_x == 460:
                                            five_y += 50
                                        if six_x == 460:
                                            six_y += 50
                                        if seven_x == 460:
                                            seven_y += 50
                                        if eight_x == 460:
                                            eight_y += 50
                                        self.count += 1
                                    else:
                                        global y2, y1
                                        if lst3[3] == 0:
                                            if lst3[2] == 0:
                                                if lst3[1] == 0:
                                                    if lst3[0] == 0:
                                                        w = 0
                                                        z = 0
                                                        if y1 == 150:
                                                            z = 260
                                                            if lst1[3] == 1:
                                                                w = 180
                                                                lst3[0] = 1
                                                                lst1[3] = 0
                                                            elif lst1[2] == 1:
                                                                w = 230
                                                                lst3[0] = 1
                                                                lst1[2] = 0
                                                            elif lst1[1] == 1:
                                                                w = 280
                                                                lst3[0] = 1
                                                                lst1[1] = 0
                                                            elif lst1[0] == 1:
                                                                w = 330
                                                                lst3[0] = 1
                                                                lst1[0] = 0
                                                        elif y2 == 150:
                                                            z = 360
                                                            if lst2[3] == 1:
                                                                w = 180
                                                                lst2[3] = 0
                                                                lst3[0] = 1
                                                            elif lst2[2] == 1:
                                                                w = 230
                                                                lst2[2] = 0
                                                                lst3[0] = 1
                                                            elif lst2[1] == 1:
                                                                w = 280
                                                                lst2[1] = 0
                                                                lst3[0] = 1
                                                            elif lst2[0] == 1:
                                                                w = 330
                                                                lst2[0] = 0
                                                                lst3[0] = 1
                                                        if one_y == w and one_x == z:
                                                            one_x = 460
                                                            one_y = 380
                                                        elif two_y == w and two_x == z:
                                                            two_x = 460
                                                            two_y = 380
                                                        elif three_y == w and three_x == z:
                                                            three_x = 460
                                                            three_y = 380
                                                        elif four_y == w and four_x == z:
                                                            four_x = 460
                                                            four_y = 380
                                                        elif five_y == w and five_x == z:
                                                            five_x = 460
                                                            five_y = 380
                                                        elif six_y == w and six_x == z:
                                                            six_x = 460
                                                            six_y = 380
                                                        elif seven_y == w and seven_x == z:
                                                            seven_x = 460
                                                            seven_y = 380
                                                        elif eight_y == w and eight_x == z:
                                                            eight_x = 460
                                                            eight_y = 380
                                                    else:
                                                        w = 0
                                                        z = 0
                                                        q = ''
                                                        if one_x == 460:
                                                            q = 'one'
                                                        elif two_x == 460:
                                                            q = 'two'
                                                        elif three_x == 460:
                                                            q = 'three'
                                                        elif four_x == 460:
                                                            q = 'four'
                                                        elif five_x == 460:
                                                            q = 'five'
                                                        elif six_x == 460:
                                                            q = 'six'
                                                        elif seven_x == 460:
                                                            q = 'seven'
                                                        elif eight_x == 460:
                                                            q = 'eight'
                                                        if y2 == 150:
                                                            z = 360
                                                            if lst2[3] == 1:
                                                                w = 180
                                                            elif lst2[2] == 1:
                                                                w = 230
                                                            elif lst2[1] == 1:
                                                                w = 280
                                                            elif lst2[0] == 1:
                                                                w = 330
                                                        elif y1 == 150:
                                                            z = 260
                                                            if lst1[3] == 1:
                                                                w = 180
                                                            elif lst1[2] == 1:
                                                                w = 230
                                                            elif lst1[1] == 1:
                                                                w = 280
                                                            elif lst1[0] == 1:
                                                                w = 330
                                                        q2 = 0
                                                        if one_y == w and one_x == z:
                                                            if 'one' in lstred and q in lstred or \
                                                                    'one' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                one_x = 460
                                                                one_y = 330
                                                        elif two_y == w and two_x == z:
                                                            if 'two' in lstred and q in lstred or \
                                                                    'two' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                two_x = 460
                                                                two_y = 330
                                                        elif three_y == w and three_x == z:
                                                            if 'three' in lstred and q in lstred or \
                                                                    'three' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                three_x = 460
                                                                three_y = 330
                                                        elif four_y == w and four_x == z:
                                                            if 'four' in lstred and q in lstred or \
                                                                    'four' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                four_x = 460
                                                                four_y = 330
                                                        elif five_y == w and five_x == z:
                                                            if 'five' in lstred and q in lstred or \
                                                                    'five' in lstgreen and q in lstgreen:
                                                                five_x = 460
                                                                five_y = 330
                                                        elif six_y == w and six_x == z:
                                                            if 'six' in lstred and q in lstred or \
                                                                    'six' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                six_x = 460
                                                                six_y = 330
                                                        elif seven_y == w and seven_x == z:
                                                            if 'seven' in lstred and q in lstred or \
                                                                    'seven' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                seven_x = 460
                                                                seven_y = 330
                                                        elif eight_y == w and eight_x == z:
                                                            if 'eight' in lstred and q in lstred or \
                                                                    'eight' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                eight_x = 460
                                                                eight_y = 330
                                                        if q2 == 1:
                                                            if y2 == 150:
                                                                if lst2[3] == 1:
                                                                    w = 180
                                                                    lst3[1] = 1
                                                                    lst2[3] = 0
                                                                elif lst2[2] == 1:
                                                                    w = 230
                                                                    lst3[1] = 1
                                                                    lst2[2] = 0
                                                                elif lst2[1] == 1:
                                                                    w = 280
                                                                    lst3[1] = 1
                                                                    lst2[1] = 0
                                                                elif lst2[0] == 1:
                                                                    w = 330
                                                                    lst3[1] = 1
                                                                    lst2[0] = 0
                                                            elif y1 == 150:
                                                                if lst1[3] == 1:
                                                                    w = 180
                                                                    lst3[1] = 1
                                                                    lst1[3] = 0
                                                                elif lst1[2] == 1:
                                                                    w = 230
                                                                    lst3[1] = 1
                                                                    lst1[2] = 0
                                                                elif lst1[1] == 1:
                                                                    w = 280
                                                                    lst3[1] = 1
                                                                    lst1[1] = 0
                                                                elif lst1[0] == 1:
                                                                    w = 330
                                                                    lst3[1] = 1
                                                                    lst1[0] = 0
                                                else:
                                                    w = 0
                                                    z = 0
                                                    q = ''
                                                    if one_x == 460:
                                                        q = 'one'
                                                    elif two_x == 460:
                                                        q = 'two'
                                                    elif three_x == 460:
                                                        q = 'three'
                                                    elif four_x == 460:
                                                        q = 'four'
                                                    elif five_x == 460:
                                                        q = 'five'
                                                    elif six_x == 460:
                                                        q = 'six'
                                                    elif seven_x == 460:
                                                        q = 'seven'
                                                    elif eight_x == 460:
                                                        q = 'eight'
                                                    if y2 == 150:
                                                        z = 360
                                                        if lst2[3] == 1:
                                                            w = 180
                                                        elif lst2[2] == 1:
                                                            w = 230
                                                        elif lst2[1] == 1:
                                                            w = 280
                                                        elif lst2[0] == 1:
                                                            w = 330
                                                    elif y1 == 150:
                                                        z = 260
                                                        if lst1[3] == 1:
                                                            w = 180
                                                        elif lst1[2] == 1:
                                                            w = 230
                                                        elif lst1[1] == 1:
                                                            w = 280
                                                        elif lst1[0] == 1:
                                                            w = 330
                                                    q2 = 0
                                                    if one_y == w and one_x == z:
                                                        if 'one' in lstred and q in lstred or \
                                                                'one' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            one_x = 460
                                                            one_y = 280
                                                    elif two_y == w and two_x == z:
                                                        if 'two' in lstred and q in lstred or \
                                                                'two' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            two_x = 460
                                                            two_y = 280
                                                    elif three_y == w and three_x == z:
                                                        if 'three' in lstred and q in lstred or \
                                                                'three' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            three_x = 460
                                                            three_y = 280
                                                    elif four_y == w and four_x == z:
                                                        if 'four' in lstred and q in lstred or \
                                                                'four' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            four_x = 460
                                                            four_y = 280
                                                    elif five_y == w and five_x == z:
                                                        if 'five' in lstred and q in lstred or \
                                                                'five' in lstgreen and q in lstgreen:
                                                            five_x = 460
                                                            five_y = 280
                                                    elif six_y == w and six_x == z:
                                                        if 'six' in lstred and q in lstred or \
                                                                'six' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            six_x = 460
                                                            six_y = 280
                                                    elif seven_y == w and seven_x == z:
                                                        if 'seven' in lstred and q in lstred or \
                                                                'seven' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            seven_x = 260
                                                            seven_y = 280
                                                    elif eight_y == w and eight_x == z:
                                                        if 'eight' in lstred and q in lstred or \
                                                                'eight' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            eight_x = 460
                                                            eight_y = 280
                                                    if q2 == 1:
                                                        if y2 == 150:
                                                            if lst2[3] == 1:
                                                                w = 180
                                                                lst3[2] = 1
                                                                lst2[3] = 0
                                                            elif lst2[2] == 1:
                                                                w = 230
                                                                lst3[2] = 1
                                                                lst2[2] = 0
                                                            elif lst2[1] == 1:
                                                                w = 280
                                                                lst3[2] = 1
                                                                lst2[1] = 0
                                                            elif lst2[0] == 1:
                                                                w = 330
                                                                lst3[2] = 1
                                                                lst2[0] = 0
                                                        elif y1 == 150:
                                                            if lst1[3] == 1:
                                                                w = 180
                                                                lst3[2] = 1
                                                                lst1[3] = 0
                                                            elif lst1[2] == 1:
                                                                w = 230
                                                                lst3[2] = 1
                                                                lst1[2] = 0
                                                            elif lst1[1] == 1:
                                                                w = 280
                                                                lst3[2] = 1
                                                                lst1[1] = 0
                                                            elif lst1[0] == 1:
                                                                w = 330
                                                                lst3[2] = 1
                                                                lst1[0] = 0
                                            else:
                                                w = 0
                                                z = 0
                                                q = ''
                                                if one_x == 460:
                                                    q = 'one'
                                                elif two_x == 460:
                                                    q = 'two'
                                                elif three_x == 460:
                                                    q = 'three'
                                                elif four_x == 460:
                                                    q = 'four'
                                                elif five_x == 460:
                                                    q = 'five'
                                                elif six_x == 460:
                                                    q = 'six'
                                                elif seven_x == 460:
                                                    q = 'seven'
                                                elif eight_x == 460:
                                                    q = 'eight'
                                                if y2 == 150:
                                                    z = 360
                                                    if lst2[3] == 1:
                                                        w = 180
                                                    elif lst2[2] == 1:
                                                        w = 230
                                                    elif lst2[1] == 1:
                                                        w = 280
                                                    elif lst2[0] == 1:
                                                        w = 330
                                                elif y1 == 150:
                                                    z = 260
                                                    if lst1[3] == 1:
                                                        w = 180
                                                    elif lst1[2] == 1:
                                                        w = 230
                                                    elif lst1[1] == 1:
                                                        w = 280
                                                    elif lst1[0] == 1:
                                                        w = 330
                                                q2 = 0
                                                if one_y == w and one_x == z:
                                                    if 'one' in lstred and q in lstred or \
                                                            'one' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        one_x = 460
                                                        one_y = 230
                                                elif two_y == w and two_x == z:
                                                    if 'two' in lstred and q in lstred or \
                                                            'two' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        two_x = 460
                                                        two_y = 230
                                                elif three_y == w and three_x == z:
                                                    if 'three' in lstred and q in lstred or \
                                                            'three' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        three_x = 460
                                                        three_y = 230
                                                elif four_y == w and four_x == z:
                                                    if 'four' in lstred and q in lstred or \
                                                            'four' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        four_x = 460
                                                        four_y = 230
                                                elif five_y == w and five_x == z:
                                                    if 'five' in lstred and q in lstred or \
                                                            'five' in lstgreen and q in lstgreen:
                                                        five_x = 460
                                                        five_y = 230
                                                elif six_y == w and six_x == z:
                                                    if 'six' in lstred and q in lstred or \
                                                            'six' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        six_x = 460
                                                        six_y = 230
                                                elif seven_y == w and seven_x == z:
                                                    if 'seven' in lstred and q in lstred or \
                                                            'seven' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        seven_x = 460
                                                        seven_y = 230
                                                elif eight_y == w and eight_x == z:
                                                    if 'eight' in lstred and q in lstred or \
                                                            'eight' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        eight_x = 460
                                                        eight_y = 230
                                                if q2 == 1:
                                                    if y2 == 150:
                                                        if lst2[3] == 1:
                                                            w = 180
                                                            lst3[3] = 1
                                                            lst2[3] = 0
                                                        elif lst2[2] == 1:
                                                            w = 230
                                                            lst3[3] = 1
                                                            lst2[2] = 0
                                                        elif lst2[1] == 1:
                                                            w = 280
                                                            lst3[3] = 1
                                                            lst2[1] = 0
                                                        elif lst2[0] == 1:
                                                            w = 330
                                                            lst3[3] = 1
                                                            lst2[0] = 0
                                                    elif y1 == 150:
                                                        if lst1[3] == 1:
                                                            w = 180
                                                            lst3[3] = 1
                                                            lst1[3] = 0
                                                        elif lst1[2] == 1:
                                                            w = 230
                                                            lst3[3] = 1
                                                            lst1[2] = 0
                                                        elif lst1[1] == 1:
                                                            w = 280
                                                            lst3[3] = 1
                                                            lst1[1] = 0
                                                        elif lst1[0] == 1:
                                                            w = 330
                                                            lst3[3] = 1
                                                            lst1[0] = 0
                            else:
                                lstsup[2] = 1
                                sup = 0
                                for i in lstsup:
                                    if i == 1:
                                        sup += 1
                                if sup == 2:
                                    time2 = int(
                                        str(str(dt.datetime.now().time()).split(':')[-1]).split(
                                            '.')[0]) + int(
                                        str(str(dt.datetime.now().time()).split(':')[
                                                1])) * 60 + int(
                                        str(str(dt.datetime.now().time()).split(':')[0])) * 360
                                    result = time2 - time
                                    q = result % 60
                                    if q < 10:
                                        fanction(1, f'{result // 60}:0{q}')
                                    else:
                                        fanction(1, f'{result // 60}:{q}')

                running = True
                fps = 60
                all_sprites = pygame.sprite.Group()
                buttle1(all_sprites, 250, 200)
                buttle2(all_sprites, 350, 200)
                buttle3(all_sprites, 450, 200)
                num = choice(lst)
                if num == 0:
                    color = 'red'
                    lstred.append('one')
                else:
                    color = 'green'
                    lstgreen.append('one')
                lst.remove(num)
                one = Player(rect_sprite, one_x + 30, one_y + 25, color)
                num = choice(lst)
                if num == 0:
                    color = 'red'
                    lstred.append('two')
                else:
                    color = 'green'
                    lstgreen.append('two')
                lst.remove(num)
                two = Player(rect_sprite, two_x + 30, two_y + 25, color)
                num = choice(lst)
                if num == 0:
                    color = 'red'
                    lstred.append('three')
                else:
                    color = 'green'
                    lstgreen.append('three')
                lst.remove(num)
                three = Player(rect_sprite, three_x + 30, three_y + 25, color)
                num = choice(lst)
                if num == 0:
                    color = 'red'
                    lstred.append('four')
                else:
                    color = 'green'
                    lstgreen.append('four')
                lst.remove(num)
                four = Player(rect_sprite, four_x + 30, four_y + 25, color)
                num = choice(lst)
                if num == 0:
                    color = 'red'
                    lstred.append('five')
                else:
                    color = 'green'
                    lstgreen.append('five')
                lst.remove(num)
                five = Player(rect_sprite, five_x + 30, five_y + 25, color)
                num = choice(lst)
                if num == 0:
                    color = 'red'
                    lstred.append('six')
                else:
                    color = 'green'
                    lstgreen.append('six')
                lst.remove(num)
                six = Player(rect_sprite, six_x + 30, six_y + 25, color)
                num = choice(lst)
                if num == 0:
                    color = 'red'
                    lstred.append('seven')
                else:
                    color = 'green'
                    lstgreen.append('seven')
                lst.remove(num)
                seven = Player(rect_sprite, seven_x + 30, seven_y + 25, color)
                num = choice(lst)
                if num == 0:
                    color = 'red'
                    lstred.append('eight')
                else:
                    color = 'green'
                    lstgreen.append('eight')
                lst.remove(num)
                eight = Player(rect_sprite, eight_x + 30, eight_y + 25, color)

                def run():
                    while True:
                        one.q(one_x + 29, one_y + 25)
                        two.q(two_x + 29, two_y + 25)
                        three.q(three_x + 29, three_y + 25)
                        four.q(four_x + 29, four_y + 25)
                        five.q(five_x + 29, five_y + 25)
                        six.q(six_x + 29, six_y + 25)
                        seven.q(seven_x + 29, seven_y + 25)
                        eight.q(eight_x + 29, eight_y + 25)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                all_sprites.update(event)
                        screen.fill((0, 0, 0))
                        all_sprites.draw(screen)
                        rect_sprite.draw(screen)
                        pygame.display.flip()

                def draw():
                    screen.fill("black")
                    all_sprites.update()
                    all_sprites.draw(screen)
                    pygame.display.flip()

                if __name__ == "__main__":
                    run()
            if args and args[0].type == pygame.MOUSEMOTION and \
                    self.rect.collidepoint(args[0].pos):
                self.image = self.image
            else:
                self.image = self.image

    class Button(pygame.sprite.Sprite):
        def __init__(self, group, x, y, image, fl):
            super().__init__(group)
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.fl = fl
            self.flag = True

        def flag(self):
            return self.flag

        def update(self, *args):
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos) and self.fl:
                a1.flag = False
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos) and not self.fl:
                a1.flag = 2
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
            load_image(f"3.jpeg"),
            (600, 400)))
    c = 80
    for i in range(1, 6):
        Button_levels(sprite_Button_levels, c, 100,
                      pygame.transform.scale(load_image(
                          f"3.jpeg"),
                          (70, 70)), i)
        c += 100

    FON(sprite_Button, 0, 0,
        pygame.transform.scale(load_image("3.jpeg"),
                               (600, 400)))
    FON(sprite_Button, 0, 250,
        pygame.transform.scale(load_image("4.jpeg", -1), (1832 // 6, 712 // 6)))
    a2 = Button(sprite_Button, 100, 160,
                pygame.transform.scale(load_image("5.jpeg", -1), (150, 70)), False)
    a1 = Button(sprite_Button, 340, 160,
                pygame.transform.scale(load_image("5.jpeg", -1), (150, 70)), True)
    Button_levels(sprite_Button_levels, 400, 230,
                  pygame.transform.scale(load_image(
                      "3.jpeg"),
                      (120, 70)), False)
    FON(sprite_Button_resultats, 0, 0, pygame.transform.scale(load_image(
        "3.jpeg"),
        (600, 400)))
    Button_levels(sprite_Button_resultats, 450, 250,
                  pygame.transform.scale(load_image(
                      "3.jpeg"),
                      (100, 50)), False)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if a1.flag and a1.flag != 2:
                    sprite_Button.update(event)
                elif a1.flag != 2:
                    sprite_Button_levels.update(event)
                sprite_Button_resultats.update(event)
            if event.type == pygame.MOUSEMOTION:
                sprite_Button.update(event, True)
        if not a1.flag and a1.flag != 2:
            screen.fill((0, 0, 0))
            sprite_Button_levels.draw(screen)
            help_23(screen)
        elif a1.flag == 2:
            screen.fill((0, 0, 0))
            sprite_Button_resultats.draw(screen)
            help_43(screen)
        else:
            sprite_Button.draw(screen)
            help(screen)
        pygame.display.flip()
    pygame.quit()


fanction()
