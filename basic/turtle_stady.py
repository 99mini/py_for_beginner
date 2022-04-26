import turtle as t
import math

a = 50
b = 50 * math.sqrt(3)
c = 100

t.screensize(1000,1000)

t.circle(c)

t.begin_fill()
t.color("red")

# 빗변
t.left(90)
t.forward(c*2)

# 밑변
t.right(120)
t.forward(a*2)

# 높이
t.right(90)
t.forward(b*2)

t.end_fill()

t.penup()
t.backward(b)
t.left(90)
t.forward(b)
t.left(90)
t.pendown()

t.circle(b)

t.penup()
t.left(90)
t.forward(b)
t.right(90)
t.forward(b)
t.left(90)
t.forward(a)
t.right(90)
t.forward(a)
t.left(90)
t.pendown()

t.circle(a)