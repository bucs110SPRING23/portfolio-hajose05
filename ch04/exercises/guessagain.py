# Guess the number (AGAIN) 
import random
number = random.randrange(1,1001) 
guessed_number = int(input('Guess a number between 1 and 1000: '))

counter = 0
while True: 
    counter+= 1 
    if guessed_number == number:
        print('Correct! the answer was ' + str(guessed_number))
        break  
    elif guessed_number > number: 
        print('Too high.') 
        guessed_number = int(input('Have another go: '))
         
    elif guessed_number < number: 
        print('Too Low')  
        guessed_number = int(input('Go again: '))  
print('And it only took you ' + str(counter) + ' trys!') 

