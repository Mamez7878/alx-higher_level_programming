#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= 0 and idx <= len(my_list) - 1:
        return my_list[idx]
    return None
