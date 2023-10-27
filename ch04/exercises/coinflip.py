# Coin Flip 
import turtle 
import random  
screen = turtle.Screen() 
screen.setup(width=800, height=600)
my_turtle = turtle.Turtle() 
my_turtle.forward(1) 
x = my_turtle.xcor() 
y = my_turtle.ycor()  

while 1: 
    coin_outcomes = [1,2] 
    outcome = random.choice(coin_outcomes) 
    if outcome == 1: 
        outcome = "heads" 
        if outcome == "heads": 
            my_turtle.left(90) 
            my_turtle.forward(50) 
        if x > 400: 
            break
        if x < -400: 
            break
            
                
    else: 
        outcome = "tails" 
        if outcome == "tails": 
            my_turtle.right(90) 
            my_turtle.forward(50) 
        if y > 300: 
           break
        if y < -300: 
           break 
    print("The coin landed on " + outcome + '!') 
turtle.bye()    

