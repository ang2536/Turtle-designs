from myPolygon import *
import turtle

bob=turtle.Turtle()
turtle.colormode(255)
bob.speed(0)

for times in range(255):
    c=(times,times,255)
    bob.color(c)
    turtle.bgcolor("brown")
    bob.begin_fill()
    print(c)
    polygon(bob,1,100)
    bob.left(90)
    bob.forward(times)
    bob.end_fill()
