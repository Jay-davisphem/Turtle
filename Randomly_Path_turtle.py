from turtle import *
from random import choice as ch
title("Let's Turtle!")
speed(0)
color("grey")
x = -180
for y in range(-180, 180 + 1, 10):
    pu()
    goto(x, y)
    pd()
    fd(360)
y = 180
right(90)
for x in range(-180, 180 + 1, 10):
    pu()
    goto(x, y)
    pd()
    fd(360)
pensize(2)
color("navyblue")
pu()
goto(0, 0)
pd()
speed(0.4)
x = y = 0
while abs(x) < 180 and abs(y) < 180:
    c = ch(("n", "w", "s", "e"))
    if c == "w":
        x -= 10
        seth(180)
        fd(10)
    elif c == "s":
        y -= 10
        seth(270)
        fd(10)
    elif c == "e":
        x += 10
        seth(0)
        fd(10)
    elif c == "n":
        y += 10
        seth(90)
        fd(10)
done()