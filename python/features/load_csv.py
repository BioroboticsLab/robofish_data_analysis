import numpy as np
import pandas as pd


def load_csv(file_path):
    '''
    load the csv tracking data into numpy matrix
    format of each row: frame_id, fish_1, x, y, rad ,fish_2...
    :param file_path: the path of csv data
    :return: the formative numpy matrix
    '''
    df = pd.read_csv(file_path, sep=',',delimiter=';',header=None)
    dat = df.values

    # if the last element of each line is not number, delete it.
    if np.isnan(dat.min()):
        (r,c) = dat.shape
        dat = dat[~np.isnan(dat)]
        dat = np.reshape(dat, (r, c - 1))

    # if the tracking data contain the additional frame data (not the frame id), delete it.
    if len(dat[0])%5 == 2:
        dat = np.delete(dat, 1, 1)

    # format of dat: frameID, fishID, x, y, deg, rad...


    # sort each row order fish_id
    (r, c) 		= dat.shape
    fish_num 	= int(c/5)

    X = np.zeros( shape=(r, 1+fish_num*4) )
    X[:,0] = dat[:,0]
    for i in range(r):
        fish_dict = {}
        row = dat[i,1:]
        for j in range(fish_num):
            begin = 5 * j
            # fish ids
            id = int(row[begin])
            # dat coordinate
            x = row[begin + 1]
            # y corrdinate
            y = row[begin + 2]
            # deg = row[begin+3]
            # orientation in radians
            rad = row[begin + 4]
            fish_dict[id] = [x, y, rad]

        l = []
        for k in range(len(fish_dict)):
            l = l + [k+1] + fish_dict[k+1]
        X[i,1:] = l


    return X

