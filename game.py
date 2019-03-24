from pygame import*
import time
import random

print("Use arrow keys to control waluigi. Reach blue line to complete level.")

screen=display.set_mode((600,600))
display.set_caption('Select level, then press L to play a different level.')

imagelist = []

running=True

##Loading Images##
for i in range(1,8):  
    imagelist.append(transform.smoothscale(image.load("maze#"+str(i)+".png"), (600,600)))

drawlist = []

playerx, playery = 0,0
previousx, previousy = playerx, playery
size = 45

level = 0

def levelselect():
        global size,selected
        global playerx, playery
        screen.fill((200,0,200))
        myfont=font.SysFont('Comic Sans MS', 50)
        textsurface = myfont.render('Pick a Level',False,(225,255,255))
        screen.blit(textsurface,(190,0))

        myfont=font.SysFont('Comic Sans MS', 30)

        mousedown=mouse.get_pressed()[0]
        mousex=mouse.get_pos()[0]
        mousey=mouse.get_pos()[1]
        #################################  
        draw.rect(screen,(255,255,255),(100,100,100,100))
        textsurface = myfont.render('1',False,(0,0,0))
        screen.blit(textsurface,(125,100))
        #first
        if mousex>=100 and mousex <=200 and mousey>=100 and mousey<=200 and mousedown:
            drawlist.append(imagelist[0])
            selected=True
            playerx, playery = 145, 470
            size = 100
            level = 1
        #################################    
        draw.rect(screen,(255,255,255),(250,100,100,100))
        textsurface = myfont.render('2',False,(0,0,0))
        screen.blit(textsurface,(275,100))
        #second
        if mousex>=250 and mousex <=350 and mousey>=100 and mousey<=200 and mousedown:
            size = 45
            playerx, playery = 28, 467
            drawlist.append(imagelist[1])
            selected=True
            level = 2
        #################################      
        draw.rect(screen,(255,255,255),(400,100,100,100))
        textsurface = myfont.render('3',False,(0,0,0))
        screen.blit(textsurface,(425,100))
        #third
        if mousex>=400 and mousex <=500 and mousey>=100 and mousey<=200 and mousedown:
            playerx, playery = 20,495
            drawlist.append(imagelist[2])
            size = 38
            selected=True
            level = 3
        #################################      
        draw.rect(screen,(255,255,255),(100,250,100,100))
        textsurface = myfont.render('4',False,(0,0,0))
        screen.blit(textsurface,(125,250))
        #fourth
        if mousex>=100 and mousex <=200 and mousey>=250 and mousey<=350 and mousedown:
            playerx, playery = 95,10
            drawlist.append(imagelist[3])
            size = 31
            selected=True
            level = 4
        #################################      
        draw.rect(screen,(255,255,255),(250,250,100,100))
        textsurface = myfont.render('5',False,(0,0,0))
        screen.blit(textsurface,(275,250))
        #fifth
        if mousex>=250 and mousex <=350 and mousey>=250 and mousey<=350 and mousedown:
            playerx, playery = 65, 550
            size = 28
            drawlist.append(imagelist[4])
            selected=True
            level = 5
        #################################      
        draw.rect(screen,(255,255,255),(400,250,100,100))
        textsurface = myfont.render('6',False,(0,0,0))
        screen.blit(textsurface,(425,250))
        #sixth
        if mousex>=400 and mousex <=500 and mousey>=250 and mousey<=350 and mousedown:
            playerx, playery = 25,565
            size = 20
            drawlist.append(imagelist[5])
            selected=True
            level = 6
        #################################      
        draw.rect(screen,(255,255,255),(100,400,100,100))
        textsurface = myfont.render('7',False,(0,0,0))
        screen.blit(textsurface,(125,400))
        #seventh
        if mousex>=100 and mousex <=200 and mousey>=400 and mousey<=500 and mousedown:
            playerx, playery = 0,0
            size = 16
            drawlist.append(imagelist[6])
            selected=True
            level = 7
        #################################      
        draw.rect(screen,(255,255,255),(250,400,100,100))
        textsurface = myfont.render('8',False,(0,0,0))
        screen.blit(textsurface,(275,400))
        #eighth
        if mousex>=250 and mousex <=350 and mousey>=400 and mousey<=500 and mousedown:
            playerx, playery = 565, 265
            size = 16
            drawlist.append(imagelist[7])
            selected=True
            level = 8
        #################################      
        draw.rect(screen,(255,255,255),(400,400,100,100))
        textsurface = myfont.render('9',False,(0,0,0))
        screen.blit(textsurface,(425,400))
        #nineth
        if mousex>=400 and mousex <=500 and mousey>=400 and mousey<=500 and mousedown:
            drawlist.append(map9)
            selected=True
            level = 9
        #################################  
selected=False

#print([(j,0,i,n)for j in range(0,6) for i in range(248,256) for n in range(248,256)])
speed = 5
l,r,d,u = 0,0,0,0
movement = False

font.init()
while running == True:
    waluigi = transform.smoothscale(image.load("waluigi.jpg"), (size,size))
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
       # elif evt.type == MOUSEBUTTONDOWN:
            #print(mouse.get_pos())

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

    midsides = [(playerx+(size)//2, playery),#top
                    (playerx, playery+(size)//2),#left
                    (playerx+size, playery+(size)//2),#right
                    (playerx+(size)//2, playery+size)]#bottom

    #print(screen.get_at((mouse.get_pos()[0],mouse.get_pos()[1])))

    for s in midsides:
        if len(drawlist) != 0:
            if drawlist[-1].get_at(s) in [(i,0,0,j)for i in range(240,256) for j in range(250,256)]:
                previousx, previousy = playerx, playery
            else:
                if s == midsides[0]:
                    u=False
                if s == midsides[1]:
                    l=False
                if s == midsides[2]:
                    r=False
                if s == midsides[3]:
                    d=False
    for s in midsides:
        if len(drawlist) != 0:
            #print(drawlist[-1].get_at(s))
            if drawlist[-1].get_at(s) in [(0,0,n,m)for n in range(248,256) for m in range(248, 256)]:
                selected = False
                 
    if l and playerx> 0:
        previousx = playerx
        playerx -= speed
        r,u,d = 0,0,0
        movement = True
    if r and playerx < 600-size:
        previousx = playerx
        playerx += speed
        l,u,d = 0,0,0
        movement = True
    if u and playery > 0:
        previousy = playery
        playery -= speed
        l,r,d = 0,0,0
        movement = True
    if d and playery < 600-size:
        previousy = playery
        playery += speed
        l,r,u = 0,0,0
        movement = True
    
    display.flip()
quit()
