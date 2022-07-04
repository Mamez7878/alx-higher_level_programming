#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy = my_list[:]
    if idx >= 0 and idx <= len(cpy) - 1:
        cpy[idx] = element
    return cpy
