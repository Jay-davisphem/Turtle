from turtle import *
color("green")
def ugd(x, y):
    up()
    goto(x, y)
    pd()
x = -200
y = 100
for j in range(1, 11):
    for k in range(1, j + 1):
        ugd(x, y)
        write(f"{k:2d}", font=("Times", 8, "bold"))
        x += 20
    x = -200
    y -= 20
    if j == 10:
        done()