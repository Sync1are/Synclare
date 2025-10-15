# 🖱️ Hand Tracking Mouse Controller

**Control your computer mouse with just your hands!** This Python application uses computer vision and machine learning to turn your webcam into a gesture-controlled mouse interface.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-red.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-latest-orange.svg)

## ✨ Features

- 🎯 **Precise Hand Tracking**: Uses MediaPipe's robust hand detection for accurate finger positioning
- 🖱️ **Natural Mouse Movement**: Smooth cursor control with your index finger
- 👆 **Gesture Clicking**: Pinch your index and middle fingers together to click
- 🎥 **Real-time Feedback**: Live camera feed with hand landmark visualization
- ⚡ **Optimized Performance**: Lightweight and responsive with built-in smoothing
- 🔧 **Customizable Settings**: Easily adjust sensitivity, smoothing, and click thresholds

## 🚀 Demo

Simply point your index finger at the screen to move the cursor, and bring your index and middle fingers close together to click! The application provides real-time visual feedback showing your hand landmarks and click detection.

## 📋 Requirements

- Python 3.7+
- Webcam/Camera
- Windows/Mac/Linux

### Dependencies
```bash
opencv-python
mediapipe
pyautogui
```

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/hand-tracking-mouse.git
cd hand-tracking-mouse
```

2. **Install required packages**
```bash
pip install opencv-python mediapipe pyautogui
```

3. **Run the application**
```bash
python hand_mouse.py
```

## 🎮 Usage

1. **Launch the application** - A camera window will open showing your webcam feed
2. **Show your hand** - Hold your hand up in front of the camera with palm facing you
3. **Move the cursor** - Point with your index finger to control mouse movement
4. **Click** - Bring your index and middle fingertips close together (pinch gesture)
5. **Exit** - Press `ESC` key to quit the application

### 💡 Tips for Best Experience
- Ensure good lighting for better hand detection
- Keep your hand clearly visible in the camera frame
- Maintain a comfortable distance from the camera (1-2 feet)
- Use deliberate pinch gestures for reliable clicking

## ⚙️ How It Works

The application uses several key technologies:

1. **MediaPipe Hands**: Google's ML solution for real-time hand tracking
2. **OpenCV**: Computer vision library for camera capture and image processing
3. **PyAutoGUI**: Cross-platform mouse control automation

### Technical Flow:
```
Camera Feed → Hand Detection → Landmark Extraction → Coordinate Mapping → Mouse Control
```

- **Hand Detection**: MediaPipe identifies hand landmarks with 21 key points
- **Finger Tracking**: Focuses on index finger (landmark 8) for cursor position
- **Gesture Recognition**: Calculates distance between index (8) and middle (12) fingertips
- **Smoothing Algorithm**: Reduces jitter with exponential smoothing
- **Click Detection**: Triggers when finger distance falls below threshold

## 🔧 Customization

You can easily modify the behavior by adjusting these parameters in the code:

```python
SMOOTHING = 7                    # Higher = smoother but slower response
CLICK_DIST_THRESHOLD = 40        # Lower = easier clicking
CLICK_COOLDOWN = 0.35           # Minimum time between clicks (seconds)
min_detection_confidence = 0.6   # Hand detection sensitivity
min_tracking_confidence = 0.6    # Hand tracking sensitivity
```

## 🐛 Troubleshooting

**Camera not working?**
- Check if another application is using the camera
- Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` for external cameras

**Hand not detected?**
- Ensure good lighting conditions
- Keep your hand clearly visible and unobstructed
- Try adjusting the `min_detection_confidence` value

**Mouse too sensitive/slow?**
- Adjust the `SMOOTHING` parameter (higher = slower, lower = faster)
- Modify the coordinate mapping ratio if needed

**Accidental clicks?**
- Increase `CLICK_DIST_THRESHOLD` for stricter click detection
- Adjust `CLICK_COOLDOWN` to prevent rapid clicking

## 🤝 Contributing

Contributions are welcome! Here are some ideas for improvements:
- Add support for right-click gestures
- Implement scroll functionality
- Create a GUI for parameter adjustment
- Add gesture-based keyboard shortcuts
- Support for multiple hand tracking

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [MediaPipe](https://mediapipe.dev/) by Google for the hand tracking solution
- [OpenCV](https://opencv.org/) community for computer vision tools
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for cross-platform automation

## 📧 Contact

Feel free to reach out if you have questions or suggestions!

---

**⭐ Star this repository if you found it helpful!**
