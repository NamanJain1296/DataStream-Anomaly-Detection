# Efficient Data Stream Anomaly Detection

## Project Overview
This project implements a Python script to detect anomalies in a continuous data stream. The stream simulates real-time sequences of floating-point numbers representing metrics like financial transactions or system metrics. 

### Key Features
- **Data Stream Simulation**: Generates synthetic data with seasonal patterns, noise, and occasional anomalies.
- **Anomaly Detection**: Utilizes Z-Score-based detection with a sliding window.
- **Real-Time Visualization**: Displays the data stream and detected anomalies dynamically.

## Techniques Used
### Data Stream Simulation
- Simulates a sinusoidal seasonal pattern with added Gaussian noise to emulate real-world data behavior.
- Injects anomalies (large deviations) randomly to mimic unusual events.

### Anomaly Detection
- Employs the **Z-Score method** to identify outliers:
  - Calculates the deviation of each point from the mean.
  - Flags points with a Z-Score exceeding a threshold (default: 3).
- Benefits:
  - Simple and computationally efficient for streaming data.
  - Adapts dynamically to changes in the data stream (concept drift).
 
## Key Concepts and Insights
- **Z-Score Anomaly Detection**: 
  - Identifies outliers by measuring the number of standard deviations a data point is from the mean.
  - Effective for streaming data with a normal distribution.
- **Sliding Window Technique**: 
  - Maintains a fixed-size window of recent data points to dynamically adapt to concept drift.
- **Real-Time Visualization**:
  - Implements a live plot using `matplotlib` for immediate feedback on detected anomalies.

### Visualization
- Real-time plotting using `matplotlib`.
- Highlights anomalies with distinct markers for easy identification.

## Real-World Applications
- **Fraud Detection**: Identifying unusual transactions in financial data.
- **System Monitoring**: Detecting spikes or drops in system metrics like CPU usage or network traffic.
- **IoT Applications**: Monitoring sensor data for anomalies in smart devices.

## How to Run
1. Clone this repository.
2. Install dependencies using:
   ```bash
   pip install -r requirements.txt
