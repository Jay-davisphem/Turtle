from turtle import *
#circle(70); goto(0, 0-20); circle(90)
iny = 0
c = 0
r = 30
speed(0)
while c < 50:
    up()
    goto(0, iny)
    pd()
    circle(r)
    r += 4
    iny -= 4
    c += 1
done()