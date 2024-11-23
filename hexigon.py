import turtle
turtle.Screen().bgcolor("Green")
scr=turtle.Screen()
scr.setup(1000,1000)
turtle.title("this is a hexagon")
sidesamount=6
length=60
angle=360/sidesamount
abc=turtle.Turtle()
for i in range(sidesamount):
    abc.forward(length)
    abc.right(angle)
turtle.done()