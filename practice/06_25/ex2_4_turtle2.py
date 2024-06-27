import random
import turtle as t

t.clear()
t.home()
t.shape('turtle')

t.circle(50,360)
t.circle(-50,360)
t.penup()
t.speed(0)

t.colormode(255)

t.dot(20)

for i in range(50):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)
  x = random.randint(-250,250)
  y = random.randint(-250,250)
  t.goto(x,y)

  d = random.randint(0,360)
  t.setheading(d)
  t.shapesize(random.randint(1,5))
  t.stamp()


t.mainloop()