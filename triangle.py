import turtle
turtle.Screen().bgcolor("Blue")
scr=turtle.Screen()
scr.setup(1000,1000)
turtle.title("this is a triangle")
sidesamount=3
length=60
angle=360/sidesamount
abc=turtle.Turtle()
for i in range(sidesamount):
    abc.forward(length)
    abc.right(angle)
turtle.done()