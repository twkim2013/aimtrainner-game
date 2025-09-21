import pygame
import random
import math
import pygame_widgets
from pygame_widgets.button import Button
import time
from loginscreen import *
from config import *
import but

from config import run
name = login()
run()

t = pygame.time.get_ticks()

radius = 30
x = random.randint(0,1280)
y = random.randint(0,720)
c = 0
b = (255, 255, 255)
def score():
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {c}', True, (100, 100, 100))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
def changing_cordinates(xpos, ypos, x_1 = x, y_1=y):

    # print(f'position ofc ircle {x_1, y_1}')
    # print(f'position of click{pos, ypos}')
    print(math.sqrt((xpos - x_1+35)**2 + (ypos- y_1+25)**2))
    global t
    if math.sqrt((xpos - (x+35))**2 + (ypos- (y+25))**2) < radius:
        x_1 = random.randint(0,1280)
        y_1 = random.randint(0,720)
        
        print(math.sqrt((xpos - x_1+x/2)**2 + (ypos- y_1+y/2)**2))
        t = pygame.time.get_ticks()
        screen.fill(b)
        #pygame.draw.circle(screen, (155, 155, 155), (x_1, y_1), radius)
        screen.blit(aim_pic, (x_1, y_1))
        pygame.display.flip()
    if math.sqrt((xpos - (x_1+35))**2 + (ypos- (y_1+25))**2) < radius:
        x_1 = random.randint(0,1280)
        y_1 = random.randint(0,720)
        print(math.sqrt((xpos - x_1+35)**2 + (ypos- y_1+25)**2))
        screen.fill(b)
        global c
        c+=1
        score()

        
        
        #pygame.draw.circle(screen, (155, 155, 155), (x_1, y_1), radius)
        screen.blit(aim_pic, (x_1, y_1))
        t = pygame.time.get_ticks()
        pygame.display.flip()
    return x_1, y_1
aim_pic = pygame.image.load(r'c:\Users\kjh948\Downloads\Target-icon-Round-red-striped-aim-board-Graphics-37082013-1.png')
aim_pic = pygame.transform.scale(aim_pic, (70,50))






x_1 = ()
y_1  = ()

color = (255, 0, 0)
delay = 0.5

pygame.display.flip()
smallfont = pygame.font.SysFont('Corbel',35)
t1 = pygame.time.get_ticks()
# rendering a text written in
# this font
BLUE=(255,255,255)

deltaTime_2 = 5

def time_button():
    global deltaTime_2
    deltaTime_2 = (pygame.time.get_ticks() - t1 ) / (1000.0)
    font = pygame.font.Font(None, 36)
    pygame.draw.rect(screen,BLUE,(500,0,300,40))
    time_text = font.render(f'time: {int(deltaTime_2)}', True, (100, 100, 100))
    screen.blit(time_text, (500, 10))
    
    pygame.display.flip()


flag = False
flag_2 = False
running = True
flag = but.press() 
while running:
    
    if flag == True:
        time_button()
    
        flag_2 = True
        #pygame.draw.circle(screen, (255,255,255), (x, y), radius)
        screen.blit(aim_pic, (x_1, y_1))
        pygame.display.flip()
    if not flag:
        pass
    print(flag)
    
    
    deltaTime = (pygame.time.get_ticks() - t ) / 1000.0
    
    
    # print(deltaTime)
    if flag_2:
        time_button()
        
    
    pygame.display.update()
        
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            xpos = pos[0]
            ypos = pos[-1]
            if x_1 and y_1:
                x_1,y_1 = changing_cordinates(xpos, ypos, x_1, y_1)
                
            else:
                x_1,y_1 = changing_cordinates(xpos, ypos)
            
            pygame.display.flip()
        if delay < deltaTime and flag:
            x_1 = random.randint(0,1280)
            y_1 = random.randint(0,720)
            
            
            
            screen.fill(b)
            score()
            


            #pygame.draw.circle(screen, (155, 155, 155), (x_1, y_1), radius)
            screen.blit(aim_pic, (x_1, y_1))
            pygame.display.update()
           
            pygame_widgets.update(event)  # Call once every loop to allow widgets to render and listen
            t = pygame.time.get_ticks()
        
        if c == 3:
            running = False
            
            
            file = open(r'C:\Users\kjh948\Desktop\football\codes.py\ai\test.txt', 'r')
            strings = file.read()
            file.close()
            file = open(r'C:\Users\kjh948\Desktop\football\codes.py\ai\test.txt', 'w')
            
            

            # nice_file = open(r'C:\Users\kjh948\Desktop\football\codes.py\aimtrainergame\Python-Aim-Trainer\aimtrainerresults.txt', 'w')

            nice_file = open(r'C:\Users\kjh948\Desktop\football\codes.py\aimtrainergame\Python-Aim-Trainer\aimtrainerresults.txt', 'r')
            prev_record = nice_file.read()
            nice_file.close()

            prev_record = prev_record.split(":").split("\n")

            nice_file = open(r'C:\Users\kjh948\Desktop\football\codes.py\aimtrainergame\Python-Aim-Trainer\aimtrainerresults.txt', 'w')

            
            if strings == '':
                pass
            else:
                print(strings)
                strings = strings.split(', ')
                strings = list(map(float,strings))  
                strings.append(deltaTime_2)
                strings = sorted(strings)  
            
            for i in range(len(strings)):
                nice_file.write(f'{i+1}:{name}{strings[i]}\n')   

            strings = list(map(str, strings))
            strings = ', '.join(strings)
            file.write(strings)
            print(deltaTime_2)
            file.close()
            nice_file.close()
            

   

        
        if flag == None:
            pygame_widgets.update(event) 



            

                