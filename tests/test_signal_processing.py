from features.signal_processing import extract_signal_features


def test_extract_signal_features_returns_required_keys():
    signal = [0.1, 0.2, 0.3, 0.4, 0.5]

    features = extract_signal_features(signal)

    assert "signal_rms" in features
    assert "signal_mean" in features
    assert "signal_peak" in features
    assert "signal_std" in features
    assert "signal_skewness" in features
    assert "signal_kurtosis" in features
    assert "spectral_energy" in features


def test_extract_signal_features_values():
    signal = [1, 2, 3, 4, 5]

    features = extract_signal_features(signal)

    assert features["signal_peak"] == 5.0
    assert features["signal_mean"] == 3.0
    assert features["signal_rms"] > 0
    assert features["spectral_energy"] > 0