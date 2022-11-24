import numpy as np
from gym.envs.toy_text import discrete
from collections import defaultdict
import time
import os
from gym.envs.classic_control import rendering
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname("cube2by2"))))
import cube22
# from cube22 import *
import clear_state
import gold_state_adjust

MIX_NUM = 20
TIME = 0.01

class CubeEnv(discrete.DiscreteEnv):
    def __init__(self, mix_num = MIX_NUM, time = TIME,
                 num_floors = 2, num_pieces = 4,
                 num_positions = 3, num_colors = 6):
        self.mix_num = MIX_NUM
        self.time = TIME
        self.num_floors = num_floors
        self.num_pieces = num_pieces
        self.num_positions = num_positions
        self.num_colors = num_colors
        
        self.state = None
        self.steps_beyond_done = None
        
        cube_obj = realCube()
        cube_obj.createCube()
        sample_cube = realCube()
        sample_cube.createCube()
        
        """Color:
        - 1: Y(ellow)
        - 2: B(lue)
        - 3: R(ed)
        - 4: O(range)
        - 5: G(reen)
        - 6: W(hite)

        Destinations:
        - 0: C(lear)

        Actions:
        There are 12 discrete deterministic actions:
        - 0: rotate the upside clockwise
        - 1: rotate the upside counterclockwise
        - 2: rotate the downside clockwise
        - 3: rotate the downside counterclockwise
        - 4: rotate the rightside clockwise
        - 5: rotate the rightside counterclockwise
        - 6: rotate the leftside clockwise
        - 7: rotate the leftside counterclockwise
        - 8: rotate the frontside clockwise
        - 9: rotate the frontside counterclockwise
        - 10: rotate the backside clockwise
        - 11: rotate the backside counterclockwise

        Rewards:
        There is a default per-step reward of -1,
        except for completing the cube, which is +20.
        """
        
        # 큐브 행동 정의
        rotate_up_R = cube_obj.upRight()
        rotate_up_L = cube_obj.upLeft()
        rotate_down_R = cube_obj.downRight()
        rotate_down_L = cube_obj.downLeft()
        rotate_right_R = cube_obj.rightRight()
        rotate_right_L = cube_obj.rightLeft()
        rotate_left_R = cube_obj.leftRight()
        rotate_left_L = cube_obj.leftLeft()
        rotate_front_R = cube_obj.frontRight()
        rotate_front_L = cube_obj.frontLeft()
        rotate_back_R = cube_obj.backRight()
        rotate_back_L = cube_obj.backLeft()
        
        self.action_defs = {0: (0, rotate_up_R), 1: (1, rotate_up_L), 2: (2, rotate_down_R), 3: (3, rotate_down_L),
                            4: (4, rotate_right_R), 5: (5, rotate_right_L), 6: (6,rotate_left_R), 7: (7,rotate_left_L),
                            8: (8,rotate_front_R), 9: (9,rotate_front_L), 10: (10,rotate_back_R), 11: (11,rotate_back_L)}
        # 상태와 행동 개수
        self.nS = num_floors * num_pieces * num_positions
        self.nA = len(self.action_defs)
        self.state = clear_state.cube_state_array(cube_obj.myCube)
        
        gold_cell = clear_state.cube_state_array(sample_cube.myCube)
        
        # 함정상태는 없음
        self.terminal_state = gold_cell
        
        # 전이확률 생략 (q-learning에서 필욘)                
                
    def is_terminal(self, state):
        return state in self.terminal_state

    # Cube_Env.step(action = X) 함수에 해당(행동을 선택하고 취하는 스텝)
    def state2action(self, action_num, _object):
        if (action_num == 0):
            _object.upRight()
        elif (action_num == 1):
            _object.upLeft()
        elif (action_num == 2):
            _object.downRight()
        elif (action_num == 3):
            _object.downLeft()
        elif (action_num == 4):
            _object.rightRight()
        elif (action_num == 5):
            _object.rightLeft()
        elif (action_num == 6):
            _object.leftRight()
        elif (action_num == 7):
            _object.leftLeft()
        elif (action_num == 8):
            _object.frontRight()
        elif (action_num == 9):
            _object.frontLeft()
        elif (action_num == 10):
            _object.backRight()
        elif (action_num == 11):
            _object.backLeft()

    def after_state2action(self, action_num, _object):     # 변환 후 다시 복귀
        if (action_num == 0):
            _object.upLeft()
        elif (action_num == 1):
            _object.upRight()
        elif (action_num == 2):
            _object.downLeft()
        elif (action_num == 3):
            _object.downRight()
        elif (action_num == 4):
            _object.rightLeft()
        elif (action_num == 5):
            _object.rightRight()
        elif (action_num == 6):
            _object.leftLeft()
        elif (action_num == 7):
            _object.leftRight()
        elif (action_num == 8):
            _object.frontLeft()
        elif (action_num == 9):
            _object.frontRight()
        elif (action_num == 10):
            _object.backLeft()
        elif (action_num == 11):
            _object.backRight()
            
    def reset(self, _object):
        _object.createCube()
        _object.mixCube()
        self.state = clear_state.cube_state_array(_object.myCube)
        self.steps_beyond_done = None
        return np.array(self.state)
            
    def step(self, action_num, _object):
        done = False
        if not gold_state_adjust.state_judgement(_object):
            self.state2action(action_num, _object)
            self.state = clear_state.cube_state_array(_object.myCube)
            done = True
            
        if not done:
            reward = 1.0
        elif self.steps_beyond_done is None:
            # Cube just uncomplete!
            self.steps_beyond_done = 0
            reward = 0.0
        else:
            self.steps_beyond_done += 1
            reward = 0.0

        return np.array(self.state[:]), reward, done, {}
