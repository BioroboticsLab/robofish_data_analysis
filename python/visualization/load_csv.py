import numpy as np
import pandas as pd

#
# format: frameID, fishID, x, y, deg, rad ...
#
def load_csv(file_path):
    df = pd.read_csv(file_path, sep=',',delimiter=';',header=None)
    x = df.values
    if np.isnan(x.min()):
        (r,c) = x.shape
        x = x[~np.isnan(x)]
        x = np.reshape(x, (r, c - 1))
    if len(x[0])%5 == 2:
        x = np.delete(x, 1, 1)
    return x

