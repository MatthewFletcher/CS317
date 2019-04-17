#!/usr/bin/env python3
from turtle import *
 
def f(length, depth):
   if depth == 0:
     forward(length)
   else:
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)
     left(120)
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)

def main():
    f(400, 3)
    exitonclick()

if __name__ == "__main__":
    main()
