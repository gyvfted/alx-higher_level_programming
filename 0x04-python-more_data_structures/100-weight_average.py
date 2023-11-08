#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    my_score = 0
    my_weight = 0
    for i in my_list:
        my_score += i[0] * i[1]
        my_weight += i[1]
    return my_score / my_weight
