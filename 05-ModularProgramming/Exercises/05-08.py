def drawSquare(x,y,n):
    import turtle
    pen = turtle.Turtle()
    pen.penup()
    pen.ht()
    pen.setposition(x,y)
    pen.pendown()
    for _ in range(4):
        pen.forward(n)
        pen.right(90)
    pen.penup()

startx = [-60,-30,0,30]
starty = [60,30,0,-30]
for i in starty:
    for j in startx:
        drawSquare(j,i,30)




