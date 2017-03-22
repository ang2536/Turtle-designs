import turtle
bob=turtle.Turtle()
bob.speed(0)
'''

for times in range(10):
    print(times)
    bob.circle(100)
    bob.right(36)
    
numbers=[106,92,87,74,43]
for d in numbers:
    print(d)
    bob.circle(d)
    bob.left(360/5)
'''

bob.width(15)
distance=100
colors=["blue" , "green" , "purple" , "magenta" , "pink" , "yellow" , "red"  ,"orange"]
for c in colors:
        print(c)
        bob.color(c)
        bob.forward(distance)
        distance += 20
        bob.left(135)
