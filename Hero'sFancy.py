
import random
import math
import time
import pygame, sys
from pygame.locals import *

pygame.init()

def Cover():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((800, 612))
    pygame.display.set_caption("Hero's Fancy")
    DY = 5
    RADIUS = 5
    BLACK = pygame.Color(0,0,0)
    BLUE = pygame.Color(100,100,255)
    clock = pygame.time.Clock()
    WHITE = pygame.Color(255, 255, 255)
    
    #myfont = pygame.font.SysFont("monospace", 85)

    #pygame.mixer.music.load("Cover.mp3")
    #pygame.mixer.music.play(-1)
    #label = myfont.render("Test!", 1, WHITE)
    #DISPLAYSURF.blit(label, (175, 175))
    #pygame.display.update()
    pygame.mixer.music.load("Cover.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1
                                  )
    while True:
        
        room1 =  pygame.image.load("Cov2.png")
        DISPLAYSURF.blit(room1, (0, 0))
        pygame.display.update()
        
        
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                mainscreen=False
                Roomone()
                pygame.display.update
                
            #elif event.type == KEYDOWN:
             #   isMain=False
              #  mainscreen=False
               # Roomone()
def Roomone():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((800, 612))
    pygame.display.set_caption("Hero's Fancy")
    DY = 5
    RADIUS = 5
    BLACK = pygame.Color(0,0,0)
    BLUE = pygame.Color(100,100,255)
    clock = pygame.time.Clock()
    WHITE = pygame.Color(255, 255, 255)
    
    #myfont = pygame.font.SysFont("monospace", 85)

    #pygame.mixer.music.load("Cover.mp3")
    #pygame.mixer.music.play(-1)
    #label = myfont.render("Test!", 1, WHITE)
    #DISPLAYSURF.blit(label, (175, 175))
    #pygame.display.update()
    pygame.mixer.music.load("Cover.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

    while True:
        
        room1 =  pygame.image.load("roomroom.PNG")
        DISPLAYSURF.blit(room1, (0, 0))
        pygame.display.update()
        
    
        
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                Roomone=False
                Roomtwo()
                
            pygame.display.update 
    
                
def Roomtwo():
   
    
    
    DISPLAYSURF = pygame.display.set_mode((800, 612))
    pygame.display.set_caption("Hero's Fancy")
    DY = 5
    RADIUS = 5
    BLACK = pygame.Color(0,0,0)
    BLUE = pygame.Color(255,255,255)
    clock = pygame.time.Clock()
    WHITE = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0 , 0) 
    pygame.init()
    while True:
        
        room1 =  pygame.image.load("roomroom.png")
        DISPLAYSURF.blit(room1, (0, 0))
        pygame.display.update()
        pygame.mixer.music.load("Cover.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1)

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                Roomtwo=False
                Roomthree()
                    
                pygame.display.update  
            
def Roomthree():
    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((800, 612))
    pygame.display.set_caption("Hero's Fancy")
    DY = 5
    RADIUS = 5
    BLACK = pygame.Color(0,0,0)
    BLUE = pygame.Color(255,255,255)
    clock = pygame.time.Clock()
    WHITE = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0 , 0) 
    while True:
        
        room1 =  pygame.image.load("directions room.png")
        DISPLAYSURF.blit(room1, (0, 0))
        pygame.display.update()
        pygame.mixer.music.load("Main.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:

                Roomthree=False
                Roomfour()
                    
                pygame.display.update()  
        
        
        


def Roomfour():
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    
               
    DISPLAYSURF = pygame.display.set_mode((812, 600))
    
    background = pygame.image.load("Defeat1.png")
    
    dipple = pygame.image.load("Dipple-re2.png")
    rock = pygame.transform.scale(pygame.image.load("rock.png"), (25, 25))
    enemy = pygame.image.load("creeper.png")
    posX = 20
    posY = 300
    #enemy is 186 x 240

    enemyX = 812 - 186
    enemyY = 300
    enemyDY = 20
    enemyHealth = 600
    
    bullets = [] #create a list of bullets
    while True:
        
        pygame.init()
        
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.quit()
                
            if event.type == KEYDOWN:
                if event.key == K_UP:
                        posY -= 40
                if event.key == K_DOWN:
                        posY += 40
                if event.key == K_LEFT:
                        posX -= 40
                if event.key == K_RIGHT:
                        posX += 40
                if event.key == K_SPACE:
                    bullets.append([posX, posY, rock])
                if event.key == K_g:
                        roomfour=False
                        roomfive()
                        
        enemyY += enemyDY

        if enemyY <= 0 or enemyY + 240 >= 600:
            enemyY -= enemyDY
            enemyDY = -enemyDY

        
        DISPLAYSURF.blit(background, (0, 0))        
        DISPLAYSURF.blit(dipple, (posX, posY))
        for bullet in bullets:
          
            if bullet[0]  >= 812 - 186  and bullet[1] >= enemyY and bullet[1]  <= enemyY + 240 and bullet[1] >= enemyY - 240:
                                                                                                                
                bullets.remove(bullet)
                enemyHealth -= 25
               
            
            if bullet[0] == 406:
                bullets.remove(bullet)
                enemyHealth2 -= 100
                
               
            
            
                
            #if bullet[0] != enemyX and bullet[1] != enemyY:
             #   enemyHealth += 1
              #  bullets.remove(bullet)
             

                
                
        if enemyHealth > 0:
            DISPLAYSURF.blit(enemy, (enemyX, enemyY))
        
        if enemyHealth <= 0:        
            pygame.draw.rect(DISPLAYSURF, white, (100, 20, 0, 50))
        else:
            pygame.draw.rect(DISPLAYSURF, white, (100, 20, enemyHealth, 50), 1)
        if enemyHealth <= 0:
            myfont = pygame.font.SysFont("monospace", 25)

    #    render text
            label = myfont.render("Level Passed! Press G to continue.", 1, white)
            DISPLAYSURF.blit(label, (150, 300))
            pygame.display.update()
    
                
            
        
        
        for bullet in bullets:
            bullet[0] += 20
            
        for bullet in bullets:
            DISPLAYSURF.blit(bullet[2], (bullet[0]+40, bullet[1]+30))
        pygame.display.update()        
def roomfive():
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    
               
    DISPLAYSURF = pygame.display.set_mode((812, 600))
    
    background = pygame.image.load("fightroom2.png")
    
    dipple = pygame.image.load("Dipple-re2.png")
    rock = pygame.transform.scale(pygame.image.load("rock.png"), (25, 25))
    enemy = pygame.image.load("smallenemy.png")
    rock2 = pygame.image.load("rock.png")
    
    posX = 20
    posY = 300
    #enemy is 186 x 240

    enemyX = 812 - 186
    enemyY = 300
    enemyDY = 20
    enemyHealth = 600
    enemyHealth = 600
    
    bullets = [] #create a list of bullets
    while True:
        
        pygame.init()
        
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.quit()
                
            if event.type == KEYDOWN:
                if event.key == K_UP:
                        posY -= 40
                if event.key == K_DOWN:
                        posY += 40
                if event.key == K_LEFT:
                        posX -= 40
                if event.key == K_RIGHT:
                        posX += 40
                if event.key == K_SPACE:
                    bullets.append([posX, posY, rock])
                if event.key == K_f:
                        roomfive=False
                        roomsix()
                        
        #enemyY += enemyDY

        #if enemyY <= 0 or enemyY + 240 >= 600:
         #   enemyY -= enemyDY
          #  enemyDY = -enemyDY

        
        DISPLAYSURF.blit(background, (0, 0))        
        DISPLAYSURF.blit(dipple, (posX, posY))
        for bullet in bullets:
        
            if bullet[0]  >= 812 - 186 and bullet[0]   and bullet[1] >= enemyY and bullet[1] <= enemyY + 240 and bullet[1] >= enemyY - 240:
                                                                                                                
                bullets.remove(bullet)
                enemyHealth -= 25
               
            
            if bullet[0] == 406:
                bullets.remove(bullet)
                enemyHealth -= 100

   
                
           # if bullet[0] != enemyX and bullet[1] != enemyY:
           #     enemyHealth += 1
            #    bullets.remove(bullet)
             

                
                
        if enemyHealth > 0:
            DISPLAYSURF.blit(enemy, (enemyX, enemyY))
        
        #if enemyHealth > 0:
            #DISPLAYSURF.blit(enemy, (enemyX - 200, enemyY - 200))
        
        
        if enemyHealth <= 0:        
            pygame.draw.rect(DISPLAYSURF, white, (100, 20, 0, 50))
        else:
            pygame.draw.rect(DISPLAYSURF, white, (100, 20, enemyHealth, 50), 1)
        if enemyHealth <= 0:
            myfont = pygame.font.SysFont("monospace", 25)

    #    render text
            label = myfont.render("Level Passed! Press F to continue.", 1, white)
            DISPLAYSURF.blit(label, (150, 300))
            pygame.display.update()
        for bullet in bullets:
            bullet[0] += 20
        
        for bullet in bullets:
            DISPLAYSURF.blit(bullet[2], (bullet[0]+40, bullet[1]+30))
  
                
            
        
        
        for bullet in bullets:
            bullet[0] += 20
            
    
        pygame.display.update()    
    
    
    
    
        

        

    pygame.display.update()

def roomsix():
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    
               
    DISPLAYSURF = pygame.display.set_mode((812, 600))
    
    background = pygame.image.load("fightroom.png")
    
    dipple = pygame.image.load("Dipple-re2.png")
    rock = pygame.transform.scale(pygame.image.load("rock.png"), (25, 25))
    enemy = pygame.image.load("Soda.png")
    rock2 = pygame.image.load("rock.png")
    
    posX = 20
    posY = 300
    #enemy is 186 x 240

    enemyX = 812 - 186
    enemyY = 350
    enemyDY = 20
    enemyHealth = 600
    enemyHealth2 = 600
    
    bullets = [] #create a list of bullets
    bullets2 = [] #bullet 2
    while True:
        
        pygame.init()
        
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.quit()
                
            if event.type == KEYDOWN:
                if event.key == K_UP:
                        posY -= 40
                if event.key == K_DOWN:
                        posY += 40
                if event.key == K_LEFT:
                        posX -= 40
                if event.key == K_RIGHT:
                        posX += 40
                if event.key == K_SPACE:
                    bullets.append([enemyX, enemyY, rock])
                if event.key == K_RETURN:
                    bullets2.append([posX, posY, rock])
                    
                    
                    
                if event.key == K_k:
                        roomsix=False
                        CutScene()
                        
                        
        enemyY += enemyDY

        if enemyY <= 0 or enemyY + 240 >= 600:
            enemyY -= enemyDY
            enemyDY = -enemyDY

        
        DISPLAYSURF.blit(background, (0, 0))        
        DISPLAYSURF.blit(dipple, (posX, posY))
        for bullet in bullets:
        
            if bullet[0]  >= 812 - 184  and bullet[1] >= enemyY and bullet[1]  <= enemyY + 240 and bullet[1] >= enemyY - 240:
                                                                                                                
                bullets.remove(bullet)
                enemyHealth -= 25
            if bullet[0] <= posX+10 and bullet[1] >= posY+10:
                enemyHealth2 -= 100
                bullets.remove(bullet)
        for bulleT in bullets2:   
            if bulleT[0]  >= 812 - 184  and bulleT[1] >= enemyY and bulleT[1]  <= enemyY + 240 and bulleT[1] >= enemyY - 240:
                                                                                                                
                bullets2.remove(bulleT)
                enemyHealth -= 25
            if bulleT[0] <= posX+10 and bulleT[1] >= posY+10:
                enemyHealth2 -= 100
                bullets2.remove(bulleT)    
            
            
                
           # if bullet[0] != enemyX and bullet[1] != enemyY:
           #     enemyHealth += 1
            #    bullets.remove(bullet)
             

                
                
        if enemyHealth > 0:
            DISPLAYSURF.blit(enemy, (enemyX, enemyY))
        
        #if enemyHealth > 0:
            #DISPLAYSURF.blit(enemy, (enemyX - 200, enemyY - 200))
        
        
        if enemyHealth <= 0:        
            pygame.draw.rect(DISPLAYSURF, white, (100, 20, 0, 50))
        else:
            pygame.draw.rect(DISPLAYSURF, white, (100, 20, enemyHealth, 50), 1)
     
            
        if enemyHealth2 > 0:
            pygame.draw.rect(DISPLAYSURF, white, (100, 475, enemyHealth2, 50), 1)
            
        if enemyHealth2 <= 0:
            pygame.draw.rect(DISPLAYSURF, white, (100, 475, 0, 50), 1)
        if enemyHealth2 <= 0:
            myfont = pygame.font.SysFont("monospace", 25)

    #    render text
            label = myfont.render("P1 Loses! Press K to continue", 1, white)
        
            DISPLAYSURF.blit(label, (125, 300))
            pygame.display.update()
        if enemyHealth <= 0:
            myfont = pygame.font.SysFont("monospace", 25)

    #    render text
            label = myfont.render("P2 Loses! Press K to continue!", 1, white)
        
            DISPLAYSURF.blit(label, (125, 300))
            pygame.display.update()
        
            
        
            
    
                
            
        
        
        for bullet in bullets:
            bullet[0] -= 20
        for bulleT in bullets2:
            bulleT[0] += 20
        
        for bullet in bullets:
            DISPLAYSURF.blit(bullet[2], (bullet[0]+40, bullet[1]+30))
        for bulleT in bullets2:
            DISPLAYSURF.blit(bulleT[2], (bulleT[0], bulleT[1]))
            
        pygame.display.update() 
        
    
def CutScene():
  
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    
               
    DISPLAYSURF = pygame.display.set_mode((812, 600))
    
    background = pygame.image.load("cutscene.png")
    while True:
        pygame.init()
        DISPLAYSURF.blit(background, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type== KEYDOWN:
                    
                if event.key == K_f:
                        
                    CutScene=False
                    roomroom()
        myfont = pygame.font.SysFont("monospace", 50)

    #    render text
        label = myfont.render("Press F to continue", 1, white)
        
        DISPLAYSURF.blit(label, (125, 550))
        pygame.display.update()
            
            
                
               
                
            
def roomroom():
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    xpos = 50
    ypos = 300
    dx = 25
    dy = 25
               
    DISPLAYSURF = pygame.display.set_mode((812, 600))
    
    background = pygame.image.load("roomroom.png")
    dipple = pygame.image.load("dipple-re2.png")
    
    while True:
        pygame.init()
        
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                   xpos -= dx
                if event.key == K_RIGHT:
                    xpos += dx
                if event.key == K_UP:
                    ypos -= dy
                if event.key== K_DOWN:
                    ypos += dy
        if xpos >= 812:
            roomroom=False
            BossRoom()
     
    
        DISPLAYSURF.blit(background, (0, 0))
        DISPLAYSURF.blit(dipple, (xpos, ypos))
        pygame.display.update()
        

  

            
def BossRoom():
    
    pygame.init()
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    clock = pygame.time.Clock()
    
    pygame.time.set_timer(USEREVENT + 1, 125)
    
               
    DISPLAYSURF = pygame.display.set_mode((812, 600))
    
    background = pygame.image.load("BossRoomfin.png")
    
    dipple = pygame.image.load("Dipple-re2.png")
    rock = pygame.transform.scale(pygame.image.load("rock.png"), (25, 25))
    enemy = pygame.image.load("Grimace2.png")
    rock2 = pygame.image.load("rock.png")
    pygame.mixer.music.load("main.mp3")
    pygame.mixer.music.play(-1)
    jazmine = pygame.image.load("jazmine.png")
    jazmine = pygame.transform.scale(jazmine, (87, 115))
    
    posX = 87
    posY = 150
    #enemy is 186 x 240

    enemyX = 812 - 250
    enemyY = 150
    enemyDY = 20
    enemyHealth = 600
    enemyHealth2 = 600
    
    bullets = [] #create a list of bullets
    bullets2 = [] #bullet 2
    while True:
        
        for event in pygame.event.get():

            

            if event.type == QUIT:
                pygame.quit()
                sys.quit()
                
            if event.type == KEYDOWN:
                if event.key == K_UP:
                        posY -= 40
                if event.key == K_DOWN:
                        posY += 40
                if event.key == K_LEFT:
                        posX -= 40
                if event.key == K_RIGHT:
                        posX += 40
                if event.key == K_RETURN:
                    bullets2.append([posX, posY, rock])
                if event.key == K_k:
                        break
                        
                if event.key == K_f:
                        BossRoom=False
                        CutScene2()
                        
                    
            if event.type == USEREVENT+1:
                if enemyHealth > 0:
                    bullets.append([enemyX, random.randint(1, 400+1), rock])
            
        
                    
                    
                    
                
                        
                        
#        enemyY += enemyDY

  #      if enemyY <= 0 or enemyY + 240 >= 600:
 #           enemyY -= enemyDY
   #         enemyDY = -enemyDY


        
        
        
        DISPLAYSURF.blit(background, (0, 0))        
        DISPLAYSURF.blit(dipple, (posX, posY))
        
        for bullet in bullets:
        #bullets from enemy
            if bullet[0]  >= posX and bullet[0] <= posX+75 and bullet[1] >= posY and bullet[1]  <= posY+104:
                                                                                                                
                bullets.remove(bullet)
                enemyHealth2 -= 25

           # if bullet[0] <= posX and bullet[1] >= posY:
            #    enemyHealth2 -= 25
             #    bullets.remove(bullet)
        #bullets from dipple
        for bulleT in bullets2:   
            if bulleT[0]  >= enemyX and bullet[0] <= enemyX+150  and bulleT[1] >= enemyY and bulleT[1]  <= enemyY + 87:
                                                                                                                
                bullets2.remove(bulleT)
                enemyHealth -= 25
            #if bulleT[0] <= posX+10 and bulleT[1] >= posY+10:
           #     enemyHealth -= 25
             #   bullets2.remove(bulleT)    
            
            
                
           # if bullet[0] != enemyX and bullet[1] != enemyY:
           #     enemyHealth += 1
            #    bullets.remove(bullet)
             

                
                
        if enemyHealth > 0:
            DISPLAYSURF.blit(enemy, (enemyX, enemyY))
        
        #if enemyHealth > 0:
            #DISPLAYSURF.blit(enemy, (enemyX - 200, enemyY - 200))
        
        
        if enemyHealth <= 0:        
            pygame.draw.rect(DISPLAYSURF, white, (100, 20, 0, 50))
            DISPLAYSURF.blit(jazmine, (450, 300))
            
        else:
            pygame.draw.rect(DISPLAYSURF, white, (100, 20, enemyHealth, 50), 1)
     
            
        if enemyHealth2 > 0:
            pygame.draw.rect(DISPLAYSURF, white, (100, 475, enemyHealth2, 50), 1)
            
        if enemyHealth2 <= 0:
            pygame.draw.rect(DISPLAYSURF, white, (100, 475, 0, 50), 1)
            
        if enemyHealth2 <= 0:
            myfont = pygame.font.SysFont("monospace", 25)

    #    render text
            label = myfont.render("You lose! Please Exit!", 1, white)
        
            DISPLAYSURF.blit(label, (125, 300))
        if enemyHealth <= 0:
            myfont = pygame.font.SysFont("monospace", 25)

    #    render text
            label = myfont.render("Grimace Dies! Press F to continue!", 1, white)
        
            DISPLAYSURF.blit(label, (125, 300))
            
            
            
        
            
    
                
            
        
        
        for bullet in bullets:
            bullet[0] -= 20
        for bulleT in bullets2:
            bulleT[0] += 20
        
        for bullet in bullets:
            DISPLAYSURF.blit(bullet[2], (bullet[0], bullet[1]))
        for bulleT in bullets2:
            DISPLAYSURF.blit(bulleT[2], (bulleT[0], bulleT[1]))
            
        pygame.display.update() 
        
    
def CutScene2():
    pygame.init()
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    clock = pygame.time.Clock()
    cut = pygame.image.load("female homosapien.png")
    
    
               
    DISPLAYSURF = pygame.display.set_mode((812, 600))
    while True:
        DISPLAYSURF.blit(cut, (0, 0))
        pygame.display.update()
        
        
                  
            
Cover()

