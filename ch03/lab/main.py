#LAB PART A 
import pygame 
import math 
import random
screen = pygame.display.set_mode((800, 800)) 
screen.fill('blue') 
pygame.display.flip() 
pygame.draw.circle(screen, 'red', (400, 400), 400)
pygame.display.flip() 
pygame.draw.line(screen, 'black', (0, 400), (800, 400), 5 )
pygame.draw.line(screen, 'black', (400, 0), (400, 800), 5 ) 
pygame.display.flip() 
#LAB PART B
x1 = 400 
y1 = 400 
for i in range(1,10): 
    x2 = random.randrange(0, 800) 
    y2 = random.randrange(0, 800) 
    distance_from_center = math.hypot(x1-x2, y1-y2) 
    dart_is_in_circle = distance_from_center <= 800/2 
    if dart_is_in_circle: 
        pygame.draw.circle(screen,'green', (x2, y2), 20) 
        pygame.display.flip() 
    else: 
        pygame.draw.circle(screen, 'magenta', (x2, y2), 20) 
        pygame.display.flip()
