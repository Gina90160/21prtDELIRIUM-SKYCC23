import numpy as np
import matplotlib as mpl
def gen_array_response_mat(pspec_length, n_rx, theta_vec, antenna_vec):
    vii_temp = np.zeros(n_rx)
    arr_resp_mat = np.ndarray([pspec_length, n_rx], dtype=complex)
    arr_resp_mat_trans = np.ndarray([n_rx, pspec_length], dtype=complex)
    for ii in range(pspec_length):
        vii_temp = np.exp(-1.0j * 2 * np.pi * np.cos(theta_vec[ii]) *
            antenna_vec)
        arr_resp_mat[ii, :] = vii_temp
    arr_resp_mat_trans = arr_resp_mat.conj().T
    return arr_resp_mat, arr_resp_mat_trans
