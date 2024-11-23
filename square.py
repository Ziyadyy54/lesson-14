import turtle
turtle.Screen().bgcolor("Yellow")
turtle.color("Orange")
scr=turtle.Screen()
scr.setup(1000,1000)
turtle.title("this is a square")
sidesamount=4
length=60
angle=360/sidesamount
abc=turtle.Turtle()
for i in range(sidesamount):
    abc.forward(length)
    abc.right(angle)
turtle.done()