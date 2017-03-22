import turtle

bob = turtle.Turtle()
alice = turtle.Turtle()
zeus = turtle.Turtle()

distance = 100

#Triangle
side = 3
angle = 360 / side

bob.forward(distance)
bob.left(angle)
bob.forward(distance)
bob.left(angle)
bob.forward(distance)
bob.left(angle)


#Square
side = 4
angle = 360 / side

alice.forward(distance)
alice.left(angle)
alice.forward(distance)
alice.left(angle)
alice.forward(distance)
alice.left(angle)
alice.forward(distance)
alice.left(angle)

#Pentagon
side = 4
angle = 360 / side
zeus.forward(distance)
zeus.left(angle)
zeus.forward(distance)
zeus.left(angle)
zeus.forward(distance)
zeus.left(angle)
zeus.forward(distance)
zeus.left(angle)
zeus.forward(distance)
zeus.left(angle)

turtle.done()
