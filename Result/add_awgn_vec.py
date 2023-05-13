import numpy as np
def add_awgn_vec(in_vec, snr_db):
    sig_pow = np.sum(np.square(np.abs(in_vec))) / len(in_vec)
    noise_pow = sig_pow / 10 ** (snr_db / 10)
    imp = 1
    noise_vec = np.sqrt(imp * noise_pow / 2) * (np.random.randn(len(in_vec)
        ) + 1.0j * np.random.randn(len(in_vec)))
    return in_vec + noise_vec
