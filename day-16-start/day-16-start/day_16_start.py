import turtle

#import module1

#print(module1.variable)

#tommy=turtle.Turtle() # constructs object tommy using class Turtle from module turtle
#print(tommy)

from turtle import Turtle
from turtle import Screen
tommy=Turtle()
tommy.shape("turtle")
for i in range(4):
    tommy.forward(100)
    tommy.left(90)

tommy.color("red")
my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()