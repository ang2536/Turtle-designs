from myPolygon import *
import turtle

bob=turtle.Turtle()
turtle.colormode(255)
bob.speed(0)

for times in range(256):
    c=(times,0,255)
    bob.color(c)
    turtle.bgcolor("grey")
    bob.begin_fill()
    print(c)
    polygon(bob,12,20)
    bob.left(50)
    bob.forward(times-40)
    bob.end_fill()
