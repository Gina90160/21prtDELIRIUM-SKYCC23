from rc import rc
import numpy as np
def calc_aoa_music(n_sources, n_rx, autocorr_mat, arr_resp_mat,
    arr_resp_mat_trans):
    eig_val, eig_vect = np.linalg.eig(autocorr_mat)
    U_N = eig_vect[:, n_sources:n_rx]
    U_N_sq = U_N @ U_N.conj().T
    pspec_out_vec = np.zeros(pspec_length, dtype=float)
    for ii in range(pspec_length):
        Q_temp = arr_resp_mat_trans[:, ii] @ U_N_sq @ arr_resp_mat[ii, :]
        pspec_out_vec[ii] = 1.0 / Q_temp.real
    pspec_out_vec = 10.0 * np.log10(pspec_out_vec / np.max(pspec_out_vec))
    return pspec_out_vec
