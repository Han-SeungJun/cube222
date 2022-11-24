import os
from gym.envs.classic_control import rendering
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname("cube2by2"))))
import cube22
import clear_state

# This definition determines whether cube is complete.
def state_judgement(_object):
    gold_cell = clear_state._goldlist()
    present_state = clear_state.cube_state_array(_object.myCube)
                
    for state_kind_number in gold_cell:
        if present_state == state_kind_number:
            return True
