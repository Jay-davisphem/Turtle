from turtle import *
speed(1)
def ugd(x, y):
    color("red")
    up()
    goto(x, y)
    pd()
    
ugd(-150, 200)
color("green")
write("Multiplication Table", font=("Times", 11, "bold"))

x = -172
for k in range(1,10):
    ugd(x, 170)
    write(f"{k:3d}", font=("Times", 8, "bold"))
    x += 40
ugd(-225, 160); color("blue"); write("_" * 38)

x = -212
y = 140
for j in range(1, 10):
    for i in range(1, 10):
        x += 40
        ugd(x, y)
        write(f"{(i*j):3d}", font=("Times", 8, "bold"))
    x = -212
    ugd(-212, y)
    write(f"{j:3d}  |", font=("Times", 8, "bold"))
    y -= 30
ugd(-225, y + 20); color("blue"); write("_" * 38)
ugd(-100, y - 20); color("green"); write("Oluwafemi", font=("Times", 11, "bold", "italic"))
ugd(-100, 230); color("blue"); write("With Turtle", font=("Times", 11, "bold", "italic"))
done()