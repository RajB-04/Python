import random
from turtle import *

colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate']
direction = [0, 90, 180, 270]

tim = Turtle()
tim.width(10)
    

def random_walk(steps):
    for i in range(steps):
        tim.color(random.choice(colors))
        tim.setheading(random.choice(direction))
        tim.forward(30)

random_walk(200)