import numpy as np
from scipy.stats import skew, kurtosis


def extract_signal_features(signal_values):
    signal = np.array(signal_values, dtype=float)

    rms = np.sqrt(np.mean(signal ** 2))
    mean_value = np.mean(signal)
    peak_value = np.max(np.abs(signal))
    std_value = np.std(signal)
    skewness_value = skew(signal)
    kurtosis_value = kurtosis(signal)

    fft_values = np.fft.fft(signal)
    fft_magnitude = np.abs(fft_values)

    spectral_energy = np.sum(fft_magnitude ** 2)

    return {
        "signal_rms": round(float(rms), 6),
        "signal_mean": round(float(mean_value), 6),
        "signal_peak": round(float(peak_value), 6),
        "signal_std": round(float(std_value), 6),
        "signal_skewness": round(float(skewness_value), 6),
        "signal_kurtosis": round(float(kurtosis_value), 6),
        "spectral_energy": round(float(spectral_energy), 6)
    }