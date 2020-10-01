from turtle import *
x0 = numinput('Enter x0!', 'x0=')
y0 = numinput('Enter y0!', 'y0=')
x1 = numinput('Enter x1!', 'x1=')
y1 = numinput('Enter y1!', 'y1=')
x2 = numinput('Enter x2!', 'x2=')
y2 = numinput('Enter y2!', 'y2=')
check = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
coor = [(x0, y0), (x1, y1), (x2, y2)]
pu()
goto(x0, y0)
write(f'p0({x0}, {y0})')
pd()
goto(x1, y1)
write(f'p1({x1}, {y1})')
if check > 0:
    t = 'is in the left of line p0p1'
elif check == 0:
    t = 'is on the line p0p1'
else:
    t = 'is in the right of line p0p1'
pu()
goto(x2, y2)
write(f'p2({x2}, {y2}) {t}')
pd()
done()