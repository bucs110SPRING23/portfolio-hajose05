#Guess the number  
import random

number = random.randrange(1, 11)

for i in range(1, 4):
    guessed_number = int(input('Guess a number between 1 and 10: '))

    if guessed_number == number:
        print('Correct!')
        break  
    elif guessed_number > number:
        print('Too High')
    elif guessed_number < number:
        print('Too Low')

if guessed_number != number:
    print('sorry you are wrong') 

