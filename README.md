# Parking-Slot-openCV

## Team Members
   Febin Anto,
   Enostar
  
# 🚗 Smart Parking Space Monitoring System using OpenCV + Web Application

This project is a Smart Parking Space Monitoring System that uses **OpenCV** to analyze a video feed from a car park and determine the availability of parking spaces in real-time. Additionally, it includes a **web application** to monitor the parking slots remotely and suggests the **easiest available slot to park** based on proximity and space clarity.

## 💡 Features

- Real-time parking space detection using video processing
- Web interface to monitor parking slots remotely via the internet
- Suggests the best (easiest) parking slot based on availability
- Dynamic visual feedback (rectangles: green for free, red for occupied)
- Easy-to-customize with any car parking video or CCTV feed

---

## 🛠 Requirements

To run this project, you’ll need the following software and Python libraries:

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Pickle
- CVZone
- Flask (for the web application)

### ✅ Installation

Clone the project:

```bash
git clone https://github.com/FEBINANTOKK/Parking-Slot-openCV.git
```

### ✅ Install the required libraries:

```bash
pip install opencv-python numpy pickle-mixin cvzone flask
```

### 🚀 Running the Project

Ensure the carPark.mp4 and CarParkPos files are placed correctly in the project directory.

## Start the local OpenCV monitoring system:

```bash
python main.py
```

## To start the web application:

```bash
python app.py
```

## Open your browser and navigate to:

```bash
http://localhost:5000
```

You will see a live view of the parking lot with real-time status of each slot.

### 🌐 Web Application Features

Displays real-time video feed with slot status
Shows total and available parking slots
Highlights and recommends the easiest slot to park (based on:
Distance from entry
Width of slot
Low traffic area)

### ⚙️ How it Works

Slot Detection: Predefined parking slot positions are stored using pickle in the CarParkPos file.

Frame Processing:
Convert color frame to grayscale.
Apply Gaussian Blur to reduce noise.
Use Adaptive Thresholding to highlight slots.
Perform Median Blur and Dilation to refine results.

Slot Status:
Count white (non-zero) pixels for each slot.
If pixel count is below a threshold → free slot.
Display slot status with bounding boxes.

Slot Suggestion:
Analyze all free slots.
Use heuristics like proximity and clarity.
Recommend the most accessible slot.

### 📸 Output Preview

Green Rectangle → Free slot

Red Rectangle → Occupied slot

Recommended Slot → Highlighted or shown separately on the web interface

## References

OpenCV: https://opencv.org/
NumPy: https://numpy.org/
Pickle: https://docs.python.org/3/library/pickle.html
CVZone: https://github.com/cvzone/cvzone
Note: The CarParkPos file should contain the serialized list of parking space positions (x, y coordinates) that are relevant to the provided car park video. This file is crucial for the correct functioning of the system, and its format should be compatible with the pickle.load() function. Make sure to provide the correct file with the accurate parking space positions to get accurate results.

Additionally, this project assumes the video file is present in the specified path (./media/carPark.mp4). If the video is not available or the path is incorrect, the system may not work as expected. Please ensure that the video is accessible before running the script.
