from myPolygon import *
import turtle

bob=turtle.Turtle()
turtle.colormode(255)
bob.speed(0)

for times in range(256):
    c=(times,200-times,255)
    bob.color(c)
    turtle.bgcolor("black")
    bob.begin_fill()
    print(c)
    polygon(bob,3,200)
    bob.left(90)
    bob.forward(times)
    bob.end_fill()
