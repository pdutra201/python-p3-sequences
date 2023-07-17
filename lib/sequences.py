#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        my_list=[]
        print(my_list)
    elif length == 1:
        my_list = [0]
        print(my_list)
    elif length == 2:
        my_list = [0, 1]
        print(my_list)
    else:
        i = 3
        my_list = [0,1]
        while i <= length:
            my_list.append(my_list[len(my_list)-2]+my_list[len(my_list)-1])
            i += 1
        print(my_list)