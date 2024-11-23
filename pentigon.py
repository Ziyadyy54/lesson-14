import turtle
turtle.Screen().bgcolor("Red")
scr=turtle.Screen()
scr.setup(1000,1000)
turtle.title("this is a pentigon")
sidesamount=5
length=60
angle=360/sidesamount
abc=turtle.Turtle()
for i in range(sidesamount):
    abc.forward(length)
    abc.left(angle)
turtle.done()