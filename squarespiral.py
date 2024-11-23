import turtle
turtle.Screen().bgcolor("green")
tv=turtle.Turtle()
# tv.setup(1000,1000)
turtle.title("this is a square spiral")
size=0
while True :
    for i in range (4):
        tv.forward(size+1)
        tv.left(90)
        size=size-5
    size=size+1