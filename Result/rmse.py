import numpy as np
def rmse(predictions, target):
    return np.sqrt(((predictions - target) ** 2).mean())
