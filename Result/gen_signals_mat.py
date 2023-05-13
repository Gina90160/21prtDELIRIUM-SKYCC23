from rc import rc
import numpy as np
import matplotlib as mpl
def gen_signals_mat(n_rx, antenna_vec, n_sources, n_samples,
    source_theta_vec=None, source_power_vec=None, power_diff_vec=None,
    snr_db=float('inf'), print_params=False):
    if source_theta_vec is None:
        source_theta_vec = np.pi * np.random.rand(n_sources)
    if source_power_vec is None:
        source_power_vec = np.sqrt(1 / 2) * (np.random.randn(n_sources) + 
            np.random.randn(n_sources) * 1.0j)
    if power_diff_vec is None:
        power_diff_vec = np.ones(n_rx)
    if print_params == True:
        print('Sources theta: ', source_theta_vec)
        print('Sources power: ', abs(source_power_vec))
        print('RX node power diff coefficient: ', power_diff_vec)
    signals_mat = np.zeros((n_samples, n_rx), dtype=complex)
    for sample_idx in range(n_samples):
        array_sync_sample_vec = np.zeros(n_rx)
        for source_idx in range(n_sources):
            phase = np.exp(1.0j * 2 * np.pi * np.random.randn(1))
            array_sync_sample_vec = (array_sync_sample_vec + phase *
                source_power_vec[source_idx] * array_response_vector(
                antenna_vec, source_theta_vec[source_idx]))
        signals_mat[sample_idx, :] = array_sync_sample_vec
    for sample_vec_idx in range(signals_mat.shape[1]):
        signals_mat[:, sample_vec_idx] = add_awgn_vec(signals_mat[:,
            sample_vec_idx], snr_db)
    power_diff_vec = np.array(power_diff_vec)
    signals_mat = signals_mat * power_diff_vec.T
    return signals_mat, source_theta_vec
