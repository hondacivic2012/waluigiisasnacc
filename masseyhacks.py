from pygame import*
import time
import random

print("Select level, then press L. Press L again to play a different level.")

screen=display.set_mode((600,600))

running=True

##Loading Images##
waluigi = transform.smoothscale(image.load("waluigi.jpg"), (45,45))
map1 = transform.smoothscale(image.load("maze#1.png"), (600,600))
map2 = transform.smoothscale(image.load("maze#2.png"), (600,600))

drawlist = []
previousx, previousy = 0,0
playerx, playery = 0,0
def levelselect():
        global playerx, playery
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
            drawlist.append(map1)
            selected=True
            playerx, playery = 262.5, 400
        draw.rect(screen,(255,255,255),(250,100,100,100))
        textsurface = myfont.render('2',False,(0,0,0))
        screen.blit(textsurface,(275,100))
        
        if mousex>=250 and mousex <=350 and mousey>=100 and mousey<=200 and mousedown:
            playerx, playery = 28, 467
            drawlist.append(map2)
            selected=True
        draw.rect(screen,(255,255,255),(400,100,100,100))
        textsurface = myfont.render('3',False,(0,0,0))
        screen.blit(textsurface,(425,100))
        
        if mousex>=400 and mousex <=500 and mousey>=100 and mousey<=200 and mousedown:
            drawlist.append(map3)
            selected=True
        draw.rect(screen,(255,255,255),(100,250,100,100))
        textsurface = myfont.render('4',False,(0,0,0))
        screen.blit(textsurface,(125,250))
        
        if mousex>=100 and mousex <=200 and mousey>=250 and mousey<=350 and mousedown:
            drawlist.append(map4)
            screen.blit(map4,(0,0))
            selected=True
        draw.rect(screen,(255,255,255),(250,250,100,100))
        textsurface = myfont.render('5',False,(0,0,0))
        screen.blit(textsurface,(275,250))
        
        if mousex>=250 and mousex <=350 and mousey>=250 and mousey<=350 and mousedown:
            drawlist.append(map5)
            selected=True
        draw.rect(screen,(255,255,255),(400,250,100,100))
        textsurface = myfont.render('6',False,(0,0,0))
        screen.blit(textsurface,(425,250))
        if mousex>=400 and mousex <=500 and mousey>=250 and mousey<=350 and mousedown:
            drawlist.append(map6)
            selected=True
        draw.rect(screen,(255,255,255),(100,400,100,100))
        textsurface = myfont.render('7',False,(0,0,0))
        screen.blit(textsurface,(125,400))
        
        if mousex>=100 and mousex <=200 and mousey>=400 and mousey<=500 and mousedown:
            drawlist.append(map7)
            selected=True
        draw.rect(screen,(255,255,255),(250,400,100,100))
        textsurface = myfont.render('8',False,(0,0,0))
        screen.blit(textsurface,(275,400))
        
        if mousex>=250 and mousex <=350 and mousey>=400 and mousey<=500 and mousedown:
            drawlist.append(map8)
            selected=True
        draw.rect(screen,(255,255,255),(400,400,100,100))
        textsurface = myfont.render('9',False,(0,0,0))
        screen.blit(textsurface,(425,400))
        
        if mousex>=400 and mousex <=500 and mousey>=400 and mousey<=500 and mousedown:
            drawlist.append(map9)
            selected=True
       
selected=False


speed = 3
l,r,d,u = 0,0,0,0
movement = False

font.init()
while running == True:
    screen.fill((0,0,0))
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        elif evt.type == KEYDOWN:
            if evt.key == K_l:
                if selected:
                    selected=False
                else:
                    selected=True
                    
    #Player Interface                
    if selected==False:          
        levelselect()
    else:
        if len(drawlist) != 0:
            screen.blit(drawlist[-1],(0,0))
        screen.blit(waluigi,(playerx,playery))
    
    
    #Movement with restrictions                    
    keys = key.get_pressed()
    
    if (previousx, previousy) == (playerx, playery):
        movement = False

    if movement == False:
        if keys[K_LEFT]:
            l = True
        if keys[K_RIGHT]:
            r = True
        if keys[K_UP]:
            u = True
        if keys[K_DOWN]:
            d = True

    previousx,previousy=playerx,playery
    if l and playerx> 0:
        previousx = playerx
        playerx -= speed
        r,u,d = 0,0,0
        movement = True
    if r and playerx < 555:
        previousx = playerx
        playerx += speed
        l,u,d = 0,0,0
        movement = True
    if u and playery > 0:
        previousy = playery
        playery -= speed
        l,r,d = 0,0,0
        movement = True
    if d and playery < 555:
        previousy = playery
        playery += speed
        l,r,u = 0,0,0
        movement = True

    display.flip()
quit()
