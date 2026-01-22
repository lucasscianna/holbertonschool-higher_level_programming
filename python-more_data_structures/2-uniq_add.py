#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    for number in my_list:
        if number not in unique_list:
           unique_list.append(number)
    total = 0
    for number in unique_list:
        total += number
    return total
