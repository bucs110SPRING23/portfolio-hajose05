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
