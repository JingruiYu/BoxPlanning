import numpy as np
import itertools
from enum import Enum
import itertools

INT_MAX = 999
weight_long = 1
weight_width = 5
weight_height = 3

class cost_type(Enum):
    height_one = 1
    height_two = 2

def cost_fun(target, use_size):
    cost = 0
    # long
    if target[0] < use_size[0]:
        return INT_MAX
    else:
        cost = cost + weight_height * (target[0] - use_size[0])

    # width
    if target[1] < use_size[1]:
        return INT_MAX
    else:
        cost = cost + weight_width * (target[1] - use_size[1])

    # hight
    if target[2] < use_size[2]:
        return INT_MAX
    else:
        cost = cost + weight_height * (target[2] - use_size[2])
    
    return cost

def target_fun(target, use_size):
    cost = 0
    # long
    if target[0] < use_size[0]:
        return INT_MAX
    else:
        cost = cost + (target[0] - use_size[0])*2

    # width
    if target[1] < use_size[1]:
        return INT_MAX
    else:
        cost = cost + target[1] - use_size[1]

    # hight
    if target[2] < use_size[2]*2:
        return INT_MAX
    else:
        cost = cost + (target[2] - use_size[2])*0.5
    
    return cost

def cal_cost(target_size, use_size, use_cost_type):
    if use_cost_type == cost_type.height_two:
       return target_fun(target_size, use_size)
    elif use_cost_type == cost_type.height_one:
        return cost_fun(target_size, use_size)

    

def check_available(combin, available_size_table, target_size, use_cost_type):
    long = 0
    width = 0
    high = 0
    for i_size in combin:
        row = i_size-1
        long = available_size_table[row,0] if available_size_table[row,0] > long else long
        width = width + available_size_table[row,1]
        high = available_size_table[row,2] if available_size_table[row,2] > high else high
    
    use_size = np.array([long, width, high])
    cost = cal_cost(target_size, use_size, use_cost_type)
    return cost

def find_all_combinations(all_idx, num):
    all_combinations = []
    for i in range(1,num+1):
        for i_combinations in itertools.combinations_with_replacement(all_idx, i):
            i_arry = np.array(i_combinations, dtype=int)
            all_combinations.append(i_arry)
    return  all_combinations

def find_solver(target_size, available_size_table, use_cost_type, most_num):
    [row, col] = available_size_table.shape
    idx_arry = np.arange(1,row+1)
    res_arry = np.ones((5,most_num+1))*INT_MAX

    all_combinations = find_all_combinations(idx_arry, most_num)
    for combin in all_combinations:
        cost = check_available(combin, available_size_table, target_size, use_cost_type)
        
        if cost < res_arry[4,0]:
            res_arry[4,0] = cost
            for i in range(len(combin)):
                res_arry[4,i+1] = combin[i]
            res_arry = res_arry[np.argsort(res_arry[:,0])]
    print(res_arry)

            

        