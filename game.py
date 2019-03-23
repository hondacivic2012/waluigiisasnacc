from pygame import*
import time
import random

screen=display.set_mode((600,600))
running=True

def levelselect():
        screen.fill((200,0,200))
        myfont=font.SysFont('Comic Sans MS', 50)
        textsurface = myfont.render('Pick a Level',False,(225,255,255))
        screen.blit(textsurface,(190,0))

        myfont=font.SysFont('Comic Sans MS', 30)

        mousedown=mouse.get_pressed()[0]
        mousex=mouse.get_pos()[0]
        mousey=mouse.get_pos()[1]

        draw.rect(screen,(255,255,255),(100,100,100,100))
        textsurface = myfont.render('1',False,(0,0,0))
        screen.blit(textsurface,(125,100))
        if mousex>=100 and mousex <=200 and mousey>=100 and mousey<=200 and mousedown:
            draw.rect(screen,(255,0,255),(0,0,100,100))
        draw.rect(screen,(255,255,255),(250,100,100,100))
        textsurface = myfont.render('2',False,(0,0,0))
        screen.blit(textsurface,(275,100))
        if mousex>=250 and mousex <=350 and mousey>=100 and mousey<=200 and mousedown:
            draw.rect(screen,(255,0,255),(0,0,100,100))
        draw.rect(screen,(255,255,255),(400,100,100,100))
        textsurface = myfont.render('3',False,(0,0,0))
        screen.blit(textsurface,(425,100))
        if mousex>=400 and mousex <=500 and mousey>=100 and mousey<=200 and mousedown:
            draw.rect(screen,(255,0,255),(0,0,100,100))

        draw.rect(screen,(255,255,255),(100,250,100,100))
        textsurface = myfont.render('4',False,(0,0,0))
        screen.blit(textsurface,(125,250))
        if mousex>=100 and mousex <=200 and mousey>=250 and mousey<=350 and mousedown:
            draw.rect(screen,(255,0,255),(0,0,100,100))
        draw.rect(screen,(255,255,255),(250,250,100,100))
        textsurface = myfont.render('5',False,(0,0,0))
        screen.blit(textsurface,(275,250))
        if mousex>=250 and mousex <=350 and mousey>=250 and mousey<=350 and mousedown:
            draw.rect(screen,(255,0,255),(0,0,100,100))
        draw.rect(screen,(255,255,255),(400,250,100,100))
        textsurface = myfont.render('6',False,(0,0,0))
        screen.blit(textsurface,(425,250))
        if mousex>=400 and mousex <=500 and mousey>=250 and mousey<=350 and mousedown:
            draw.rect(screen,(255,0,255),(0,0,100,100))

        draw.rect(screen,(255,255,255),(100,400,100,100))
        textsurface = myfont.render('7',False,(0,0,0))
        screen.blit(textsurface,(125,400))
        if mousex>=100 and mousex <=200 and mousey>=400 and mousey<=500 and mousedown:
            draw.rect(screen,(255,0,255),(0,0,100,100))
        draw.rect(screen,(255,255,255),(250,400,100,100))
        textsurface = myfont.render('8',False,(0,0,0))
        screen.blit(textsurface,(275,400))
        if mousex>=250 and mousex <=350 and mousey>=400 and mousey<=500 and mousedown:
            draw.rect(screen,(255,0,255),(0,0,100,100))
        draw.rect(screen,(255,255,255),(400,400,100,100))
        textsurface = myfont.render('9',False,(0,0,0))
        screen.blit(textsurface,(425,400))
        if mousex>=400 and mousex <=500 and mousey>=400 and mousey<=500 and mousedown:
            draw.rect(screen,(255,0,255),(0,0,100,100))

font.init()
while running == True:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    
        levelselect()

    display.flip()
quit()
