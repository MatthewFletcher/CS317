#!/usr/bin/env python3
import random as r
def main():
    class SortStruct():
        def __init__(self, digit, dtype):
            self.digit = digit
            self.dtype = dtype
    arr = [9,8,7,6,5,4,3,2,1]
    list = []
    for i, num in enumerate(arr):
        list.append(SortStruct(num, ''))
        print(list[i].digit, end=' ')

if(__name__=="__main__"):
    main()
