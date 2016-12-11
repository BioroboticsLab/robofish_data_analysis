import numpy as np
import math

def forward_velocity(dat):
    (r, c) = dat.shape
    fish_num = c/4
    X = np.zeros(shape=(r-1, fish_num))

    for i in range(r-1):
        for j in range(fish_num):
            X[i, j] = np.linalg.norm(dat[i + 1, 2 + j * 4:4 + j * 4] - dat[i, 2 + j * 4:4 + j * 4])

    return X


def turning_velocity(dat):
    (r, c) = dat.shape
    fish_num = c/4
    X = np.zeros(shape=(r-1, fish_num))
    for i in range(1):
        for j in range(fish_num):
            X[i, j] = _angle_difference(dat[i, 4 + j * 4], dat[i+1, 4 + j * 4])

    return X


def _angle_difference(a,b):
    a = _norm_angle(a)
    b = _norm_angle(b)
    return _norm_angle(b-a)

def _norm_angle(theta):
    '''Normalize an angle in radians to [0, 2*pi)
    '''
    return theta % (2*math.pi)