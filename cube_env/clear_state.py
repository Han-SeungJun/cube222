import os
import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname("cube2by2"))))
# from cube22 import *
import cube22
import numpy as np

sample = realCube()
sample.createCube()

def cube_state_array(arr):
    state = []
    for floor_dimension in arr:
        for piece_dimension in floor_dimension:
            for position_dimension in piece_dimension:
                state.append(position_dimension)
    return state

def _goldlist():
    gold_state_list = []

    for xy_rotate in range(4):
        for x_rotate in range(4):
            sample.xRight()
            gold_state_list.append(cube_state_array(sample.myCube))
        sample.yRight()
    
    sample.zRight()
    for z_rotate in range(2):
        for x_rotate in range(4):
            sample.xRight()
            gold_state_list.append(cube_state_array(sample.myCube))
        sample.zRight()
        sample.zRight()
    
    return gold_state_list
