# Bus Entry and Exit Monitoring System using Facial Recognition

This project employs Python, 'face_recognition', and 'OpenCV' libraries to create a system that monitors bus entry and exit events via facial recognition.

## Key Features

- **Facial Recognition:** Utilizes facial recognition to identify individuals entering and exiting a bus.
- **Multi-Camera Support:** Enables multiple camera inputs for capturing events from various angles.
- **Timestamp Logging:** Tracks and logs timestamps when individuals are recognized entering and leaving the bus.
- **Dynamic Face Encoding:** Periodically updates face encodings to ensure accurate recognition.

## Usage

1. **Data Input:** Configure the code with video sources for bus entry and exit cameras.
2. **Execution:** Run the code to initiate the monitoring system.

## How it Works

The program continuously processes video frames, encoding faces and their respective timestamps upon entry and exit. By utilizing a set threshold for facial similarity, it identifies and logs the time when recognized faces enter and exit the bus.

## Future Improvements

- Enhancing facial recognition accuracy.
- Real-time visual monitoring interface.
- Integration with a database for log storage.
