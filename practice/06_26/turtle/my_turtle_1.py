import turtle as t
import time

def draw_phone_logo():
    t.begin_fill()
    time.sleep(2)

    t.pensize(3)
    t.fillcolor('black')
    t.left(134)

    for i in range(30):
        t.forward(0.25)
        t.left(1)

    t.right(5)

    for i in range(35):
        t.forward(0.25)
        t.left(1)

    t.left(5)
    t.forward(7.5)

    for i in range(15):
        t.forward(0.175)
        t.right(3)

    t.forward(6.25)
    t.left(5)

    for i in range(50):
        t.forward(0.25)
        t.left(1)

    t.right(3)

    for i in range(50):
        t.forward(0.25)
        t.left(1)
    t.right(5)

    for i in range(45):
        t.forward(0.5)
        t.left(1)

    t.right(5)

    for i in range(40):
        t.forward(0.5)
        t.left(1)

    t.left(5)

    for i in range(20):
        t.forward(0.25)
        t.left(2)

    t.left(5)
    t.forward(3.75)

    for i in range(9):
        t.forward(0.5)
        t.right(3)

    t.forward(0.25)

    for i in range(15):
        t.forward(0.25)
        t.right(1)

    t.right(4)
    t.forward(1.125)
    t.right(1)

    for i in range(27):
        t.forward(0.25)
        t.left(2)

    t.left(8)
    t.forward(1.25)

    for i in range(25):
        t.forward(0.5)
        t.left(1)

    t.right(3)
    t.forward(2.5)
    t.left(83)

    for i in range(75):
        t.forward(0.325)
        t.right(1)

    t.right(4)

    for i in range(24):
        t.forward(0.325)
        t.right(1)

    t.forward(2.415)
    t.end_fill()
    t.penup()
    t.left(132)
    t.forward(25)
    t.right(96)
    t.pendown()
    t.begin_fill()
    t.fillcolor('black')

    for i in range(60):
        t.forward(0.2)
        t.right(1)

    t.right(120)

    for i in range(60):
        t.forward(0.2)
        t.right(1)

    t.hideturtle()
    t.end_fill()

# 터틀 초기화 및 시작 위치 설정
t.speed(0)
t.penup()
t.goto(0, 50)  
t.pendown()

draw_phone_logo()
