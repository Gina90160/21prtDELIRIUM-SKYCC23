import numpy as np
def gen_antenna_vec(lambda_separation, n_rx):
    return np.linspace(-(n_rx - 1) * lambda_separation / 2, (n_rx - 1) *
        lambda_separation / 2, n_rx)
