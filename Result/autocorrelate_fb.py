import numpy as np
def autocorrelate_fb(signals_mat, snap_size):
    d_J = np.eye(signals_mat.shape[1], signals_mat.shape[1])
    d_J = np.fliplr(d_J)
    out_matrix = 1.0 / snap_size * np.transpose(signals_mat) @ np.conjugate(
        signals_mat)
    return 0.5 * out_matrix + 0.5 / snap_size * d_J @ np.conjugate(out_matrix
        ) @ d_J
