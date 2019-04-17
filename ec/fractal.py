#!/usr/bin/env python3
import turtle


def tree(branchLen,t):
    right = 40
    left = 2 * right

    diff = 10

    if branchLen > 10:
        t.pd()
        #Go forward branch length
        t.forward(branchLen)
        t.width(t.width() - 0.5)
        #Turn right
        t.right(right)

        #Recursively draw a tree, subtracting diff from branch length
        t.color("red")
        tree(branchLen-diff,t)
        t.left(left)
        t.color("blue")
        tree(branchLen-diff,t)
        t.color("red")
        t.right(right)
        t.pu()
        t.backward(branchLen)

def main():
    
    #Define new turtle
    t = turtle.Turtle()
    myWin = turtle.Screen()
    
    #Hide turtle for faster animating
    t.ht()
    
    
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    t.speed(0) 
    t.width(10)
    #Draw Tree

    tree(75,t)
    myWin.mainloop()
    myWin.exitonclick()

main()
