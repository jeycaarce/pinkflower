import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("pink")
t.speed(0)
for i in range(150):
    t.circle(190-i,90)
    t.lt(90)
    t.circle(190-i,90)
    t.lt(18)