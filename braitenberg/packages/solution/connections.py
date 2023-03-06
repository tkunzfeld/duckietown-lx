from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    #num = 3
    #width = 320
    #step = int(width / num)
    #for i in range(num):
    #    res[:, (i * step):(i * step + step)] = (i+1) / num

    res[:, 0:100] = 0.2
    res[:, 100:200] = 1
    res[:, 200:350] = 1.5
    #res[:, 350:640] = -0.5
    res[0:250, :] = 0
    res[250:300, :] *= 0.2
    #res[400:450, 0:25] = 5
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    #num = 3
    #width = 320
    #step = int(width / num)
    #for i in range(num):
    #    res[:, (width+i * step):(width+i * step + step)] = 1-i/ num
    #res[:, 0:400] = -0.5
    res[:, 400:500] = 1.5
    res[:, 500:640] = 1
    res[0:250, :] = 0
    res[250:300, :] *= 0.2
    #res[400:450, 615:640] = 5
    return res
