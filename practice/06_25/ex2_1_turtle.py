import turtle

screen = turtle.Screen()
screen.title('Spiral of Spirals Fractal - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()
screen.tracer(0,0)

def draw_spiral(x,y,length,direction):
    L = length
    c = 0
    while length>1 or c<20:
        if length>2:
            draw_spiral(x,y,length*0.255,160+direction)
        turtle.up()
        turtle.seth(direction)
        turtle.goto(x,y)
        if length <= 2: turtle.down()
        turtle.fd(length)
        x,y = turtle.xcor(), turtle.ycor()
        length *= 0.93
        direction += 20
        c += 1

draw_spiral(500,-500,300,90)
screen.update()
ts=turtle.getscreen()
ts.getcanvas().postscript(file = "spiral.eps")






# ------------------------------------------------------------
# import turtle as t

# t.clear
# t.shape('turtle')

# color = ['red','green','yellow','orange','blue']

# shape = 4

# t.speed(30)
# t.hideturtle()
# t.bgcolor('black')
# t.pencolor('blue')

# t.colormode(255)
# for _ in range (300):
#   t.color((255-_,255,_))
#   t.forward(_)
#   t.right(360 /5 + _ )



# t.mainloop

#   # t.color((178,204,255))
