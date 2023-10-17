import turtle  
import random

#RACE 1 
window = turtle.Screen() 
window.bgcolor("lightblue")

michelangelo = turtle.Turtle() 
leonardo = turtle.Turtle()
michelangelo.color("orange")
leonardo.color("blue")
michelangelo.shape("turtle")
leonardo.shape("turtle")

michelangelo.up()  
leonardo.up()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)
michelangelo.forward(99) 
leonardo.forward(90) 
michelangelo.right(180)
leonardo.right(180) 
michelangelo.goto(-100,20) 
leonardo.goto(-100,-20)  
michelangelo.right(180) 
leonardo.right(180) 

#RACE 2 
for _ in range(20): 
  leonardo.forward(random.randrange(1,15)) 
  michelangelo.forward(random.randrange(1,20)) 
michelangelo.right(180) 
leonardo.right(180) 
michelangelo.goto(-100,20) 
leonardo.goto(-100,-20)  
michelangelo.right(180) 
leonardo.right(180) 
window.exitonclick()

# PART B 
import pygame 
import math 
pygame.init() 
screen = pygame.display.set_mode((600,600)) 
screen.fill('black') 
pygame.display.flip()  

num_of_sides = [3,4,6,20,100,360,100000] 
side_length = 100
xpos = 300 
ypos = 300
points = []
for j in range(0,7): 
        side = num_of_sides[j]
        for i in range(0,side): 
            angle = 360/side 
            radians = math.radians(angle * i) 
            x = xpos + side_length * math.cos(radians) 
            y = ypos + side_length * math.sin(radians) 
            points.append((x,y)) 

        pygame.draw.polygon(screen,'red',points) 
        pygame.display.flip() 
        pygame.time.wait(1000) 
        screen.fill('black') 
        pygame.display.flip()  
        points = [] 
     
        
