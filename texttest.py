import pygame as pg
from math import sqrt
import random
import math
import time
import pygame, sys
from pygame.locals import *
import cmath



def main():
    screen = pg.display.set_mode((800, 612))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    color = pg.Color('dodgerblue2')
    text = ''
    posX = 50
    posY = 100
    point = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.KEYDOWN:

                """       
                
                if event.key == pg.K_RETURN:
                    print(text)
                    text = ''
                    if "a" in text:
                        print("Works")
                """             
                    
                if event.key == pg.K_1:
                    main=False
                    num1()
                    pg.display.update()
                    
                """           
                    
                elif event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

       
            
          """  
            

        entry = pg.image.load("Entry.PNG")
        entry = pg.transform.scale(entry, (800, 612))
        screen.blit(entry, (0, 0))
        
    

        #txt_surface = font.render(text, True, color)
       #
      #  screen.blit(txt_surface, (posX, posY))

        pg.display.flip()
        clock.tick(30)
def num1():
    FORM = pg.image.load("FSCREEN.PNG")
    FORM = pg.transform.scale(FORM, (800, 612))
    
    DISPLAYSURF = pg.display.set_mode((800, 612))
    BG = pg.image.load("search.PNG")
    BG = pg.transform.scale(BG, (800, 612))
    font = pg.font.Font(None, 32)
    font2 = pg.font.Font(None, 32)
    
    clock = pg.time.Clock()
    color = pg.Color('grey')
    text = ''
    posX = 350
    posY = 120
    point = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.KEYDOWN:
                
                if event.key == pg.K_RETURN:
                    print(text)
                    text = ''
                
                        
                    
                    
                    
                elif event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        texts = str(text)
                
                
                    
            
            
        if "quad" in texts:
            FORM = pg.image.load("FSCREEN.PNG")
            FORM = pg.transform.scale(FORM, (800, 612))
            DISPLAYSURF.blit(FORM, (0, 0))
            pg.display.update()
        
            

                
                
                
               

            # To take coefficient input from the users
            a = float(input('Enter a: '))
            b = float(input('Enter b: '))
            c = float(input('Enter c: '))

            # calculate the discriminant
            d = (b**2) - (4*a*c)

            # find two solutions
            sol1 = (-b-cmath.sqrt(d))/(2*a)
            sol2 = (-b+cmath.sqrt(d))/(2*a)

            print('The solution are {0} and {1}'.format(sol1,sol2))
            num1()
            


                    
        if "area of" in texts:
            PI = 3.14159

            rad = input("What is the radius of your circle?\n")
            r = int(rad)
            AOC = PI*(r**2)
            COC = r*PI
            PI = 3.14159
            print("The area of your circle is ", AOC, ".\n")
            num1()
                



        DISPLAYSURF.blit(BG, (0, 0))
        pg.display.update()
        txt_surface = font.render(text, True, color)
        
        DISPLAYSURF.blit(txt_surface, (posX, posY))

        pg.display.flip()
        clock.tick(30)

    

    
            
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
