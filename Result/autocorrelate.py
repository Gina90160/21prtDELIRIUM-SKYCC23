import numpy as np
def autocorrelate(signals_mat, snap_size):
    return 1.0 / snap_size * np.transpose(signals_mat) @ np.conjugate(
        signals_mat)
