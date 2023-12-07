import turtle as t

t.speed(10)
t.shape("turtle")
t.width(3)

t.left(90)
t.penup()
t.fd(100)
t.left(90)
t.pendown()

t.circle(100, 25)

t.right(90)
t.fillcolor("#8F5C4B")
t.begin_fill()
t.circle(30)
t.end_fill()

t.left(90)
t.circle(100, 7)

t.right(90)
t.fillcolor("#68422F")
t.begin_fill()
t.circle(15)
t.end_fill()

t.left(90)
t.circle(100, 304)

t.left(90)
t.fillcolor("#8F5C4B")
t.begin_fill()
t.circle(30)
t.end_fill()

t.left(90)
t.circle(-100, 7)

t.left(90)
t.fillcolor("#68422F")
t.begin_fill()
t.circle(-15)
t.end_fill()

t.left(90)
t.fillcolor("#8F5C4B")
t.begin_fill()
t.circle(100, 392)
t.end_fill()

t.left(90)
t.penup()
t.fd(70)
t.right(90)
t.fd(12)
t.pendown()

t.fillcolor("black")
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.bk(24)
t.pendown()

t.fillcolor("black")
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.left(90)
t.fd(30)
t.pendown()

t.fillcolor("#FFD1B8")
t.begin_fill()
t.left(180)
t.circle(11, 180)
t.fd(20)
t.circle(11, 180)
t.fd(20)
t.end_fill()

t.penup()
t.left(90)
t.fd(10)
t.pendown()

t.fd(5)
t.left(120)
t.fd(10)
t.left(120)
t.fd(10)
t.left(120)
t.fd(5)

t.penup()
t.left(90)
t.fd(10)
t.pendown()

t.fd(5)
t.right(30)

t.fd(8)
t.left(120)
t.penup()
t.fd(8)
t.pendown()
t.left(120)
t.fd(8)
t.left(120)

t.hideturtle()
t.exitonclick()