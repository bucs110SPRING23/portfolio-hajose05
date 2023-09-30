import math 
import pygame 
import random 
pygame.display.init() 
screen = pygame.display.set_mode()
screen_size = pygame.display.get_window_size() 
w = screen_size[1] 
l = screen_size[0]
background = pygame.color.Color('black') 
screen.fill(background)
print(screen_size)  
pygame.draw.circle(screen,'red',(screen_size[0]/2,screen_size[1]/2),screen_size[0]/2) 
pygame.draw.line(screen,'black',(0,w/2),(l,w/2)) 
pygame.draw.line(screen,'black',(l/2,0),(l/2,w))
pygame.display.flip()
pygame.time.delay(1000)  

for x in range(0,10): 
    cord_l = random.randrange(0,l) 
    cord_w = random.randrange(0,w) 
    pygame.draw.circle(screen,'blue',(cord_l,cord_w),10)
    pygame.display.flip()
    pygame.time.delay(300)  
