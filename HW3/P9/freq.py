#!/usr/bin/env python3

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    print(len(dict))
    return dict

if __name__ == "__main__":
    print(char_frequency('honorificabilitudinitatibus'))


