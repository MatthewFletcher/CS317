#!/usr/bin/env python3
import turtle

t = turtle.Turtle()

def halfpetal(deg):
    i=0
    res = 1
    rad = 3
    t.width(1)
    while(i<=deg):
        t.width(1+i/100)
        t.forward(rad)
        t.right(res)
        i+=res

def fullpetal(deg):
    halfpetal(deg)
    t.right(180-deg)
    halfpetal(deg)

def flower(count):
    colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
    for i in range(count):
        t.pencolor(colors[i%6])
        t.home()
        t.right(360/count * i)
        t.pd()
        fullpetal(360/count)
        t.pu()
def main():
    t.ht()
    t.speed(9)
    t.width(1)
    t.seth(90)
    flower(12)

    turtle.exitonclick()

if __name__ == "__main__":
    main()
