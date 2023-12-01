# Bus Entry and Exit Monitoring System using Facial Recognition
This project utilizes Python along with the 'face_recognition' and 'OpenCV' libraries to create a system for monitoring entry and exit events on a bus through facial recognition.

# Key Features:
#Facial Recognition: The code implements facial recognition to identify individuals entering and exiting a bus.
#Multiple Camera Support: It supports multiple camera inputs for capturing entry and exit events from different angles.
#Timestamp Logging: Tracks and logs timestamps when individuals are recognized entering and leaving the bus.
#Dynamic Face Encoding: Periodically updates face encodings to maintain accuracy in recognition.
# Usage:
#Data Input: Configure the code with video sources for bus entry and exit cameras.
#Execution: Run the code to initiate the monitoring system.
# How it Works:
The program continuously processes video frames, encoding faces and their respective timestamps upon entry and exit. Using a set threshold for facial similarity, it identifies and logs the time when recognized faces enter and exit the bus.

# Future Improvements:
#Enhancing facial recognition accuracy.
#Real-time visual monitoring interface.
#Integration with database for log storage.
