import turtle 
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("violet")
s.tracer(0)

t = turtle.Turtle()
def drawGaris(x,y):
    t.down()
    t.forward(60)
    t.left(90)
    for i in range(4):
        t.forward(60)
        t.left(90)


sc = turtle.Screen().exitonclick()