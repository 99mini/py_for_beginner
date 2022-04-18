from turtle import Turtle

def draw(n):
    angle = 180*(1-2/n)
    for i in range(n):
        Turtle.forward(100)
        Turtle.right(180 - angle)
    while True:
        pass
    
draw(3)