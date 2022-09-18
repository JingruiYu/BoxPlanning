import numpy as np
from find_solver import cost_type, find_solver

target_size = np.array([44,43,28])
size_table = np.loadtxt("candidate_size_1.txt")

find_solver(target_size, size_table, cost_type.height_one, 3)