import pygame as pg
import sys

pg.init()
sc = pg.display.set_mode((400, 300))

pg.mixer.music.load('Sound_07433 (mp3cut.net).wav')
#pg.mixer.music.play()

sound1 = pg.mixer.Sound('Sound_07433 (mp3cut.net).wav')
sound2 = pg.mixer.Sound('Sound_07433 (mp3cut.net).wav')

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()



        elif i.type == pg.MOUSEBUTTONUP:
            if i.button == 1:
                sound1.play()
            elif i.button == 3:
                sound2.play()

    pg.time.delay(20)