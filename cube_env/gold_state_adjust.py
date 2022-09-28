import os
from gym.envs.classic_control import rendering
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname("cube2by2"))))
import cube22
# from cube22 import *
import clear_state

gold_cell = clear_state._goldlist()

# This definition determines whether cube is complete.
def state_judgement(cube_state):
    present_state = []
    for dimension_position in cube_state:
        for dimension_piece in dimension_position:
            for dimension_floor in dimension_piece:
                present_state.append(dimension_floor)
                
    for state_kind_number in gold_cell:
        if state_kind_number == present_state:
            return True
