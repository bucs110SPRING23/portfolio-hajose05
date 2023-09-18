import turtle 
side_number = input('We are making a shape. How many sides should it have ') 
side_length = input('How long should each side be? ')  
internal_angle = 360/(int(side_number)) 
Leonardo = turtle.Turtle() 
Leonardo.shape('triangle') 
Leonardo.color('purple') 
for _ in range(int(side_number)): 
  Leonardo.forward(int(side_length)) 
  Leonardo.left(internal_angle)  
