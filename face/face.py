
import turtle
t=turtle
t.speed(0)
#frowning face
t.circle(10)
t.penup()
t.right(180)
t.forward(40)
t.pendown()
t.circle(10)
t.penup()
t.right(90)
t.forward(-80)
t.pendown()
for i in range(180):
    t.forward(1)
    t.right(1)

#happy face
t.penup()
t.forward(80)
t.pendown()
t.circle(10)
t.penup()
t.right(-180)
t.forward(40)
t.pendown()
t.circle(10)
t.penup()
t.right(90)
t.forward(-40)
t.pendown()
for i in range(180):
    t.forward(-1)
    t.left(1)
t.done()