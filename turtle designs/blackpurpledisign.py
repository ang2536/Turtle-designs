from myPolygon import *
import turtle

bob=turtle.Turtle()
turtle.colormode(255)
bob.speed(0)

for times in range(256):
    c=(0,times,times)
    bob.color(c)
    turtle.bgcolor("orange")
    bob.begin_fill()
    print(c)
    polygon(bob,9,100)
    bob.left(100)
    bob.forward(times)
    bob.end_fill()
