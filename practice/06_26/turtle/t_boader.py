import turtle as t

t.clear()

t.home()

t.shape('turtle')

t.penup()

t.goto(150,300)

t.pendown()

t.speed(0)

t.pensize(3)

t.hideturtle()

for i in range(4):

    if i % 2 == 0:

        t.circle(-10,90)

        t.forward(600)

    else:

        t.circle(-10, 90)

        t.forward(300)

t.mainloop()