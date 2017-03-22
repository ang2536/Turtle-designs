from myPolygon import *
import turtle

bob=turtle.Turtle()
turtle.colormode(255)
bob.speed(0)

for times in range(256):
    c=(255,times,255)
    bob.color(c)
    turtle.bgcolor("grey")
    bob.begin_fill()
    print(c)
    polygon(bob,10,50)
    bob.left(100)
    bob.forward(times-10)
    bob.end_fill()
