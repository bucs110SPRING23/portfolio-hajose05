#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week) 
classes_per_week = 5 
cost_per_class = cost_per_week / classes_per_week 
print('You owe ',cost_per_class,' carbon based organism')  
print(weeks, type(weeks)) 
print(classes, type(weeks))  
print(tuition, type(tuition)) 
print(cost_per_week, type(cost_per_week)) 
print(classes_per_week, type(classes_per_week)) 
print(cost_per_class, type(cost_per_class)) 

#Part B 
import random
var = ['Eggplants', 'Yams', 'carrots', 'tomatoes', 'spinach'] 
Random_Vegetable = random.choice(var) 
print(Random_Vegetable) 
