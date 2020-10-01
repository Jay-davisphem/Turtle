from turtle import *
speed(0)
r = 90
a = 50
x = 20
def use(r, a, x=0):
    c = 0
    while c < a:
        pu()
        goto(x, -400+r) #x: 0, -r, r
        pd()
        circle(r)
        x = (-x + 1) if x != 0 else (x + 0)
        r += 3
        c += 1
use(r, a)
use(r, a, -x)
use(r, a, x)
done()