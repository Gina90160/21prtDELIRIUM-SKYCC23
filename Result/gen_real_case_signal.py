import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
def gen_real_case_signal():
    sig_freq = 1000.0
    sampl_rate = 100000.0
    snap_size = 1024
    obs_time_len = snap_size / sampl_rate
    angle_vec = 2 * np.pi * sig_freq * np.linspace(0, obs_time_len, snap_size)
    time_vec = np.linspace(0, snap_size / sampl_rate, snap_size)
    n_rx = 2
    snap_size = 1024
    ampl_diff_vec = np.array([1, 1])
    phase_diff_vec = np.array([0, 0.7 * np.pi])
    add_noise_flag = True
    sig_mat = np.ndarray([snap_size, n_rx], dtype=complex)
    for idx in range(n_rx):
        cx_signal_vec = np.array(ampl_diff_vec[idx] * np.cos(angle_vec +
            phase_diff_vec[idx]) + 1.0j * ampl_diff_vec[idx] * np.sin(
            angle_vec + phase_diff_vec[idx]))
        if add_noise_flag:
            awgn = np.random.normal(0, 0.05, snap_size
                ) + 1.0j * np.random.normal(0, 0.05, snap_size)
            cx_signal_vec = cx_signal_vec + awgn
        sig_mat[:, idx] = cx_signal_vec
    """
    plt.figure(1)
    plt.xlabel("Time [s]")
    plt.subplot(211)
    plt.title("Signals in time")
    plt.plot(time_vec,np.real(sig_mat[:,0]),label = "Real")
    plt.plot(time_vec,np.imag(sig_mat[:,0]),label = "Imag")
    plt.legend()
    plt.subplot(212)
    plt.plot(time_vec,np.real(sig_mat[:,1]),label = "Real")
    plt.plot(time_vec,np.imag(sig_mat[:,1]),label = "Imag")
    plt.xlabel("Time [s]")
    plt.legend()
    plt.show()
    """
    return sig_mat
