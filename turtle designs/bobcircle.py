import turtle

bob=turtle.Turtle()
ally=turtle.Turtle()
charles=turtle.Turtle()
dan=turtle.Turtle()

ally.left(180)
charles.left(90)
dan.left(270)
for times in range (10):
    bob.circle(times * 10)
    ally.circle(times * 10)
    charles.circle(times * 10)
    dan.circle(times * 10)
