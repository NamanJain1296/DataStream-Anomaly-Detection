import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import time

# Data Stream Simulation
"""Generates a continuous stream with seasonal patters, noise and occasional anomalies."""

def generate_data_stream(size=1000, anomaly_probability=0.05, noise_level=2, amplitude=10):
    t = np.linspace(0, 50, size)
    seas_pattern = np.sin(t)*amplitude # Sinusoidal pattern
    noise = np.random.normal(0, noise_level, size) # Random Noise
    data_stream = seas_pattern + noise

    #Inject Anomalies
    for i in range(size):
        if np.random.rand() < anomaly_probability:
            data_stream[i] += np.random.choice([20, -20]) # Large Deviations

    return data_stream

# Anomaly Detection with Z-Score
def detect_anomaly(data_pnt, window, threshold = 3):
    """Using Sliding window to detect anomaly"""
    if len(window) < 2:
        return False

    mean = np.mean(window)
    std_dev = np.std(window)
    if std_dev == 0:
        return False

    z_score = (data_pnt - mean)/std_dev
    return abs(z_score) > threshold

#Real Time Plotting
def real_time_plot(data_stream, window_size = 50):
    """Plot data stream in real time"""
    window = deque(maxlen=window_size)
    anomalies = []

    plt.ion()
    fig, ax = plt.subplots()
    line, = ax.plot([], [], label="Data Stream", color="blue")
    anomaly_scatter, = ax.plot([], [], 'ro', label="Anomalies")

    ax.legend()
    plt.title("Real-Time Data Stream Anomaly Detection")
    plt.xlabel("Time Step")
    plt.ylabel("Value")

    for i, data_point in enumerate(data_stream):
        window.append(data_point)

        # Detect Anomaly
        is_anomaly = detect_anomaly(data_point, window)
        if is_anomaly:
            anomalies.append((i, data_point))

        #Update Plot
        x_data = range(len(window))
        line.set_data(x_data, list(window))
        ax.set_xlim(0, max(len(window), 50))
        ax.set_ylim(min(window) - 5, max(window) + 5)

        # Update anomalies
        if anomalies:
            anomaly_x, anomaly_y = zip(*anomalies)
            anomaly_scatter.set_data(anomaly_x, anomaly_y)

        plt.pause(0.01)

    plt.ioff()
    plt.show()

# Main Function
if __name__ == "__main__":
    # Generate data stream
    stream = generate_data_stream(size=500, anomaly_probability=0.05)

    # Visualize and detect anomalies
    real_time_plot(stream)