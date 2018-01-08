import pygame
import random
import math
import time
import pygame, sys
import os
from pygame.locals import *
def creds():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    b1 = pygame.image.load("cred.png")
    b1 = pygame.transform.scale(b1, (1000, 600))

    WHITE = pygame.Color(255, 255, 255)
    
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                creds = False
                cover()
        screen.blit(b1, (0, 0))
        x, y = pygame.mouse.get_pos()
        if x > 600:
            x = 100
            creds = False
            cover()
            pygame.display.update()
        myfont = pygame.font.SysFont("monospace", 45)
        
        
        label = myfont.render("GO", 1, WHITE)
        screen.blit(label, (x  - 20, y - 45 ))
        pygame.display.update()
    
def cover():
    pygame.init()
    """sounds = []
        sounds.append(pygame.mixer.Sound('D:/Users/John/Music/Music/FUN.OGG'))
        sounds.append(pygame.mixer.Sound('D:/Users/John/Music/Music/Still Alive.OGG'))
        sounds.append(pygame.mixer.Sound('D:/Users/John/Music/Music/turret.OGG'))
        sounds.append(pygame.mixer.Sound('D:/Users/John/Music/Music/portalend.OGG'))
        for sound in sounds:
            sound.play()   """
    pygame.mixer.music.load("pixel.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    
    
        # This function handles moving each item listed in items.
    def move(items):
        for item in items:
            item[0] += item[2]
            item[1] += item[3]

    # This function removes all items that will never be visible again.
    def removeUseless(items):
        for item in items:
            if item[1] > 600:
                items.remove(item)

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Hero's Fancy")
    DY = 5
    RADIUS = 5
    BLACK = pygame.Color(0,0,0)
    
    clock = pygame.time.Clock()
    WHITE = pygame.Color(255, 255, 255)
    rain = []
    b1 = pygame.image.load("title.png")
    b1 = pygame.transform.scale(b1, (1000, 700))
    
    for i in range(1000):
            r = random.randint(1,255)
            g = random.randint(1,255)
            b = random.randint(1,255)
   
        
    
    while True:
        
            
            
        BLUE = pygame.Color(255,0, 0)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
                

        # Calculate number of new drops to add this iteration, then randomly
        # generate that many unique values.
        numNewRain = random.randint(1, 10)
        xvals = set()
        while len(xvals) < numNewRain:
            x = random.randint(1, 1000)
            xvals.add(x)

        # Add each if these items into the list rain.
        for val in xvals:
            rain.append([val,0,0,DY])
         
        DISPLAYSURF.fill(BLACK)
        DISPLAYSURF.blit(b1, (0, -50))

        # Draw each raindrop individually.
        for item in rain:
            pygame.draw.ellipse(DISPLAYSURF,BLUE, (item[0], item[1], 10, 10), 0)
            
        myfont = pygame.font.SysFont("monospace", 85)

        #    render text
        pygame.display.update()
        x, y = pygame.mouse.get_pos()
        if x > 800:

            cover = False
            opening()
            pygame.display.update()
        myfont = pygame.font.SysFont("monospace", 45)
        
        
        label = myfont.render("PLAY?", 1, WHITE)
        DISPLAYSURF.blit(label, (x  - 70, y - 45 ))
        
        
        pygame.display.update()
        # Move the drops for the next iteration and remove useless ones.
        move(rain)
        removeUseless(rain)
        
        clock.tick(30)

                
                
                    

    
        
    
def opening():
    
    pygame.init()
    pygame.mouse.set_visible( False )
    pup = pygame.image.load("power.png")
    pup = pygame.transform.scale(pup, (85, 100))
    width2 = 400
    height2 = 65
    width3 = 400
    height3 = 65
    myfont = pygame.font.SysFont("monospace", 12)
    pros = []
    label = myfont.render("", 1, (255,255,255))
    white = pygame.Color(255, 255, 255)
    saber = pygame.image.load("saber1.png")
    x, y = pygame.mouse.get_pos()
    width = 400
    height = 65
    drake = pygame.image.load("Drake3.png")
    screen = pygame.display.set_mode((812, 600))
    px = 55
    shell = pygame.image.load("p1.png")
    shell = pygame.transform.scale(shell, (32, 32))
    shells = [] #List for all the shells
    drakex = 640
    drakey = 140
    # 470.
    py = 20
    ex = 0
    ey = 0
    
    imagesright = ['frame1.png','frame2.png','frame3.png','frame4.png']
    imagesleft = ['frame5.png','frame6.png','frame7.png','frame8.png']
    imagesup = ['frame9.png','frame10.png','frame11.png','frame12.png']
    imagesdown = ['frame13.png','frame14.png','frame15.png','frame16.png']
    player = pygame.image.load("frame16.png")
    b1 = pygame.image.load("bedroom.PNG")
    b1 = pygame.transform.scale(b1, (406,300))
    b2 = pygame.image.load("Living.PNG")
    b2 = pygame.transform.scale(b2, (406,300))
    b3 = pygame.image.load("Kitchen.PNG")
    b3 = pygame.transform.scale(b3, (406,300))
    b4 = pygame.image.load("Bathroom.PNG")
    b4 = pygame.transform.scale(b4, (406,300))
    myfont = pygame.font.SysFont("monospace", 15)
    
    label = myfont.render("", 1, (255,255,255))
                    
    #screen.blit(label, (100, 100))
    #screen.fill((0, 0, 0))
    #screen.blit(label, (100, 100))
    
   
    
    counter = 0
    counter2 = 0
    counter3 = 0
    
    while True:
        pro = []
        
        
        if px > 325 and px < 415 and py > 149 and py < 196:
            px = 460
            
            
            
        if px == 415 and py > 149 and py < 196:
            px = 325
            
            
           
            
        if px > 340 and px < 440 and py < 150:
            px = 450
            
     
        if px > 324 and px < 420 and py < 149:
            px = 326
            
   
        
        if px < 35:
            px = 36
            
   
        if px > 731:
            px = 730
        
            
        if py == 200 or py > 200 and py < 220:
            
            py = 195
            
            
         
            
        if py == 65 or py < 65:
            py = 75
        if px > 144 and px < 236 and py > 194 and py < 235:
            py = 320
        if px < 144  and py > 194 and py < 250:
            py = 195
        if px > 196 and px < 326 and py > 196 and py < 260:
            py = 195
        
        if px > 415 and px < 530 and py > 230 and py < 235:
            py = 195
        if px > 596 and px < 775 and py > 230 and py < 235:
            py = 195
        
        if px > 549 and px < 596 and py < 276 and py > 229:
            py = 360
            
        if py > 500:
            py = 490
        if px > 325 and px < 376 and py > 409 and py < 456:
            px = 460
        if px < 459  and px > 377 and py > 409 and py < 456:
            px = 184
        if px > 189 and px < 281 and py > 260 and py < 290:
            py = 185
        if py < 354 and py > 309 and px > 549 and px < 596:
            py = 185
            
        #if px < 351 and px < 380 and py > 365 and py < 455:
         #   px = 450
       
      
            
        
        for event in pygame.event.get():
              #checking pressed keys
            #if keys[pygame.K_UP]:
            if event.type == QUIT:
                sys.exit()
                pygame.quit()

            if event.type == KEYDOWN:
              
                if width3 > 5:
                    
                    shells.append([drakex+15, drakey, 20, shell])
                keys = pygame.key.get_pressed()
            
                if keys[pygame.K_DOWN]:
                    counter2 = (counter2 + 1) % len(imagesdown)
                    player = pygame.image.load(imagesdown[counter2])
                    keys = pygame.key.get_pressed()
                    py = py + 45
                    print("y =", py)
                    
                if keys[pygame.K_UP]:
                    counter2 = (counter2 + 1) % len(imagesup)
                    player = pygame.image.load(imagesup[counter2])
                    keys = pygame.key.get_pressed()
                    py = py - 45
                    velocity = -30
                    print("y = ", py)
                    
                    
                if keys[pygame.K_LEFT]:
                    counter2 = (counter2 + 1) % len(imagesleft)
                    player = pygame.image.load(imagesleft[counter2])
                    keys = pygame.key.get_pressed()
                    px = px - 45
                    print(px)
                if keys[pygame.K_RIGHT]:
                    counter2 = (counter2 + 1) % len(imagesright)
                    player = pygame.image.load(imagesright[counter2])
                    px = px + 45
                    print(px)
                
                    
                    
                        
                        
                    
                    
        for shelly in shells: #Update the position of every shell in the list
            shelly[0] -= shelly[2]
            if shelly[0] < 0:
                del shells[0:2]
            if shelly[0] < px + 25 and shelly[0] > px - 25 and shelly[1] > py - 25 and shelly[1] < py + 25:
                width -= 15
                del shells[0:2]
        """if px >= 780:
            px = 770
        if px <= 20:
            px = 25
        if py >= 580:
            px = 575
        if px <= 20:
            px = 25"""
        if width2 > 2:
            
            if x > drakex - 15 and x < drakex + 15 and y > drakey - 20 and y < drakey + 20:
                width2 -= 15
        
        if width2 > 2:
            
            if px > 415 and px < 812 and py > 30 and py < 230:
            
                for i in range(5):
                    if drakex < px:
                        drakex += .85
                    if drakex > px:
                        drakex -= .85
                    if drakey < py:
                        drakey += .85
                    if drakey > py:
                        drakey-= .85
            else:
                if drakey > 50 and drakey < 195:
                    
                    for i in range(5):
                        
                        if drakey < py:
                            drakey += .85
                        if drakey > py:
                            drakey -= .85
        if width2 > 2:
            
            if py > 200:
                if drakex < 640:
                    drakex += 1
                if drakey > 140:
                    drakey -= 5
                if drakey < 140:
                    drakey += 5
                if drakex > 640:
                    drakex -= 1
        if width2 < 2:
            if drakex < px:
                drakex += 5
            if drakex > px:
                drakex -= 5
            if drakey > py:
                drakey -= 5
            if drakey < py:
                drakey += 5
        if py > 199:
            del shells[0:2]
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                
                if event.key == K_m:
            
                    if px < x:
                        px += 5
                    if px > x:
                        px -= 5
                    if py < y:
                        py += 5
                    if py > y:
                        py -=5
        
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    opening()
        if drakex < px:
            drake = pygame.image.load("Drake5.png")
        if drakex > px:
            drake = pygame.image.load("Drake3.png")
            pygame.display.update()
        
            
        
        screen.fill((0, 0, 0))
        screen.blit(b1, (0, 0))
        screen.blit(b2, (400, 0))
        screen.blit(b3, (0, 300))
        screen.blit(b4, (400, 300))
        # 700, 170
        if px > 680 and py > 130 and py < 170:
            counter = -1
            
        """sounds = []
        sounds.append(pygame.mixer.Sound('D:/Users/John/Music/Music/FUN.OGG'))
        sounds.append(pygame.mixer.Sound('D:/Users/John/Music/Music/Still Alive.OGG'))
        sounds.append(pygame.mixer.Sound('D:/Users/John/Music/Music/turret.OGG'))
        sounds.append(pygame.mixer.Sound('D:/Users/John/Music/Music/portalend.OGG'))
        for sound in sounds:
            sound.play()   """
        if counter >= 0 and width3 > 5:
            screen.blit(pup, (700, 140))
            if drakex > px - 5 and drakex < px + 5 and drakey > py - 5 and drakey < py + 5:
                width -= 10
                width2 -= 5
                
                
        if counter <  0 and width3 > 5:
            if drakex > px - 5 and drakex < px + 5 and drakey > py - 5 and drakey < py + 5:
                width -= 5
                width3 -= 10
            
            
        if width2 < 1:
            if drakex < px:
                
                drake = pygame.image.load("Drake5.png")
                drake = pygame.transform.scale(drake, (210, 192))
            if drakex > px:
                drake = pygame.image.load("Drake3.png")
                drake = pygame.transform.scale(drake, (210, 192))
        if width2 > 2 and width3 > 2:
            
            screen.blit(drake, (drakex, drakey))
            
        if width2 > 0:
            pass
        if width2 < 2 and width3 > 5:
            screen.blit(drake, (drakex, drakey -  100))
            

            screen.blit(label, (drakex - 10, drakey - 10))
        
        
        screen.blit(player, (px, py))
        screen.blit(saber, (x - 25, y - 8))
        for shelly in shells: #Display all shells
            screen.blit(shelly[3], (shelly[0], shelly[1]))
        
        
            
            pygame.draw.rect(screen, white, (150,500,width2,height2), 1)
        if width > 0:
            
            pygame.draw.rect(screen, white, (150,50,width,height), 1)
        if width2 > 0:
            
            pygame.draw.rect(screen, white, (150,500,width2,height2), 1)
        if width2 < 0:
            
            pygame.draw.rect(screen, white, (150,500,width3,height3), 1)
        if width <= 10:
            
            screen.fill((255, 0, 0))
            myfont = pygame.font.SysFont("monospace", 30)
            w = pygame.image.load("w.png")
            
            screen.blit(w, (-100, -200))
            
           
                
           
            label2 = myfont.render("Press enter to restart", 1, (255, 255, 255))
            screen.blit(label2, (200, 400))
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    opening()
                    
        pygame.display.update()
        
def living():
    pygame.init()
    width = 400
    height = 65
    screen = pygame.display.set_mode((812, 600))
    # 645 85
    drakex = 675
    drakey = 85
    px = 50
    # 470.
    py = 400
    ex = 0
    ey = 0
    counter = 0
    imagesright = ['frame1.png','frame2.png','frame3.png','frame4.png']
    imagesleft = ['frame5.png','frame6.png','frame7.png','frame8.png']
    imagesup = ['frame9.png','frame10.png','frame11.png','frame12.png']
    imagesdown = ['frame13.png','frame14.png','frame15.png','frame16.png']
    player = pygame.image.load("frame10.png")
    drake = pygame.image.load("Drake2.png")
    
    b1 = pygame.image.load("bedroom.PNG")
    b1 = pygame.transform.scale(b1, (812, 600))
    b2 = pygame.image.load("Living.PNG")
    b2 = pygame.transform.scale(b2, (812, 600))
    b3 = pygame.image.load("Kitchen.PNG")
    b3 = pygame.transform.scale(b3, (812, 600))
    b4 = pygame.image.load("Bathroom.PNG")
    b4 = pygame.transform.scale(b4, (812, 600))
    myfont = pygame.font.SysFont("monospace", 20)
    
    label = myfont.render("", 1, (255,255,255))
                    
    #screen.blit(label, (100, 100))
    #screen.fill((0, 0, 0))
    #screen.blit(label, (100, 100))
    
    
    
    
    counter = 0
    counter2 = 0
    dy = 45
    dx = 45
    while True:
        
        for event in pygame.event.get():
              #checking pressed keys
            #if keys[pygame.K_UP]:
            if event.type == QUIT:
                sys.exit()
                pygame.quit()

            if event.type == KEYDOWN:
                keys = pygame.key.get_pressed()
            
                if keys[pygame.K_DOWN]:
                    counter2 = (counter2 + 1) % len(imagesdown)
                    player = pygame.image.load(imagesdown[counter2])
                    keys = pygame.key.get_pressed()
                    py += dy
                    #px += dx
                if keys[pygame.K_UP]:
                    counter2 = (counter2 + 1) % len(imagesup)
                    player = pygame.image.load(imagesup[counter2])
                    keys = pygame.key.get_pressed()
                    #py = py - 45
                    py -= dy
                    #px += dx
                if keys[pygame.K_LEFT]:
                    counter2 = (counter2 + 1) % len(imagesleft)
                    player = pygame.image.load(imagesleft[counter2])
                    keys = pygame.key.get_pressed()
                    #px = px - 45
                    #py += dy

                    px -= dx
                if keys[pygame.K_RIGHT]:
                    counter2 = (counter2 + 1) % len(imagesright)
                    player = pygame.image.load(imagesright[counter2])
                    #py += dy
                    px += dx
        """if px >= 780:
            px = 770
        if px <= 20:
            px = 25
        if py >= 580:
            px = 575
        if px <= 20:
            px = 25"""
        for i in range(5):
            if drakex < px:
                drakex += .85
            if drakex > px:
                drakex -= .85
            if drakey < py:
                drakey += .85
            if drakey > py:
                drakey -= .85
        if py == 470:
            opening = False
            living()
            pygame.display.update()
        label = myfont.render("HOMEWORK?!", 1, (255,255,255))
        screen.blit(b2, (0, 0))
        if drakex < px:
            drake = pygame.image.load("Drake5.png")
        if drakex > px:
            drake = pygame.image.load("Drake2.png")
        
                
        screen.blit(drake, (drakex - 30, drakey))
        screen.blit(player, (px, py))
        label2 = myfont.render("LEAVE ME ALONE MOM!", 1, (255,255,255))
        screen.blit(label2, (px - 20, py - 30))
        

        
        # 600 125
        #645 85
        screen.blit(label, (drakex - 25, drakey - 25))
        if drakex > px - 5 and drakex < px + 5 and drakey > py - 5 and drakey < py + 5:
            width -= 15
        
        if px > 750:
            living = False
            bathroom()
            pygame.display.update()

            
        
                
                    
            
            
            for i in range(100000):
                add = random.randint(-35, 35)
                
                screen.blit(label, (250 + add, 300))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        
                        #living = False
                        os.execl(sys.executable, sys.executable, *sys.argv)
                        pygame.display.update()
        white = pygame.Color(255, 255, 255)
        if width <= 10:
            screen.fill((255, 0, 0))
            myfont = pygame.font.SysFont("monospace", 30)
            label = myfont.render("You were grounded for not having homework", 1, (255,255,255))
            screen.blit(label, (50, 250))
            label2 = myfont.render("Press enter to restart")
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    opening()
                    
        if width > 0:
            
            pygame.draw.rect(screen, white, (150,50,width,height), 1)
                    
            
        pygame.display.update()
            
            
        
        pygame.display.update()
creds()

                
    
    
    
    
    
