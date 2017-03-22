import turtle

bob=turtle.Turtle()

sides=90
distance=100
angle=270

bob.speed(0)

for times in range(angle):
    bob.forward(times * 6)
    bob.circle(times)
    bob.left(angle)
