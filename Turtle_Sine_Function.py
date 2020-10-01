#Sine function
from math import *
from turtle import *
from time import sleep
def ang(x, y, /, *, s=6, n=None, c="black"):
    color(c)
    if not n:
        n = ''
    pu()
    goto(x, y)
    pd()
    write(n, font=("Times", s, "bold"))
def graph(*, x=400, y=200):
    pu(); goto(-x / 2, 0); pd()
    fd(x); lt(30); bk(10); fd(10); rt(30); rt(30); bk(10)
    pu(); goto(0, -y / 2); pd()
    seth(90)
    fd(y); lt(30); bk(10); fd(10); rt(30); rt(30); bk(10)
    seth(0)
def plot(f, *, fx=-200, tx=200, u=3):
    speed(0)
    if f == "cos":
       y = 100 * cos(fx * u * pi / 180)
       pu()
       goto(fx, y)
       pd()
       for x in range(fx, tx + 1):
           y = 100 * cos(x * u * pi / 180)
           goto(x, y)
    elif f == "sin":
        y = 100 * sin(fx * u * pi / 180)
        pu()
        goto(fx, y)
        pd()
        for x in range(fx, tx + 1):
            y = 100 * sin(x * u * pi / 180)
            goto(x, y)
        
def label(u=3):
    speed(3)
    color("black")
    ang((-140 * 3) / u, -15, n="-2\u03c0")  
    ang(((-140 * 3 / 2) + 30) / u, -15, n="-\u03c0")
    ang(-5,-10, n="O")
    ang(((110 * 3 / 2) + 15) / u, -15, n="\u03c0")  
    ang((110 * 3) / u, -15, n="2\u03c0")

    ang(-10, 90, n="1")
    ang(-14, -110, n="-1")
def supp1():    
    ang(-200, 0, s=11, n="Graph of y = sinx & y = cosx", c="grey")
    ang(-150, -100, s=12, n="By David Oluwafemi\n        Using Turtle", c="green")
def supp2():
    ang(-210, 200, s=14, n="Happy Independent Day!", c="green")
    ang(-100, 0, s=10, n="Graph of y = sinx", c="green")
    ang(-150, -100, s=12, n="By David Oluwafemi\n        Using Turtle", c="green")
def legend():
    up()
    goto(-50, 200)
    pd()
    write("Legend: cos:\n                 sin:")
    up()
    goto(70, 206)
    pd()
    begin_fill()
    color("red")
    circle(5, steps=4)
    end_fill()
    up()
    goto(70, 231)
    pd()
    begin_fill()
    color("blue")
    circle(5, steps=4)
    end_fill()
    
#1
supp2()
sleep(2)
reset()
graph()
color("red")
plot("sin",)
label()
sleep(2)
reset()
#2
supp1()
sleep(2)
reset()
graph()
legend()
color("blue")
plot("cos")
color("red")
plot("sin")
label()
sleep(3)
reset()
#
pu()
goto(-150, 0)
pd()
color("green")
write("jay-davisphem.github.io", font=("Times", 10, "bold", "italic"))
hideturtle()
sleep(2)