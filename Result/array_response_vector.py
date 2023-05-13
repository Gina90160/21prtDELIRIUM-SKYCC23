import numpy as np
def array_response_vector(antena_vec, theta):
    return np.exp(-1.0j * 2 * np.pi * antena_vec * np.cos(theta))
