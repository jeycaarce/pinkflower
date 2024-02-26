import turtle

colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "white", "cyan", "magenta"]

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)

for i in range(150):
    t.pencolor(colors[i % len(colors)])
    t.fillcolor(colors[i % len(colors)])
    t.begin_fill()
    t.circle(190-i, 90)
    t.lt(90)
    t.circle(190-i, 90)
    t.lt(18)
    t.end_fill()

turtle.done()