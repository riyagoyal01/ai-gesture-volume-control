# Gesture-Controlled Volume System 🎛️🤏✋✊

Control your **system volume in real-time** using just **hand gestures** with your webcam — no GUI needed.  
This is a **terminal-based ML application** demonstrating gesture recognition and system integration.

---

## Features
- 🖐 **Real-time hand gesture recognition** using MediaPipe  
- 🔊 **System volume control** with Pycaw  
- ✊ **Mute**, ✋ **Freeze Volume**, 🤏 **Adjust Volume** gestures  
- ✅ Modular code, easy to read and extend  
- 🎥 Demo video included in `assets/`  

---

## How It Works

### 1. Hand Detection
- Uses **MediaPipe Hands** to detect hand landmarks from your webcam feed.  
- Calculates distance between **thumb tip** and **index finger tip**.

### 2. Gesture Interpretation

| Gesture | Action | Finger Positions |
|---------|--------|----------------|
| ✊ Fist | Mute | 0 fingers up |
| ✋ Open Hand | Freeze Volume | 4+ fingers up |
| 🤏 Pinch | Adjust Volume | Thumb + index up, max 2 fingers |

### 3. Volume Control
- Maps finger distance to system volume using Pycaw.  
- Can mute, unmute, or adjust volume in real-time.

### 4. Terminal Display
- Shows current mode (`MUTE`, `FREEZE VOLUME`, `ADJUST`) in webcam feed.  
- Press `q` to quit the program.

---

## Getting Started

### Requirements
- Python 3.10+  
- Install dependencies:
```bash
pip install -r requirements.txt

## Run the Project

### 1. Connect your webcam.
### 2. Run the main program:
```bash
python app.py

### 3. Control your system volume using gestures.
### 4. Press q to exit.

---

## Folder Structure

Gesture-Control-Volume/
│
├─ app.py                 # Main program loop
├─ gesture_control.py     # Hand detection & finger tracking
├─ volume_control.py      # System volume control
├─ requirements.txt       # Python dependencies
├─ README.md              # Project documentation
├─ assets/                # Demo video or images
│   └─ demo_video.mp4
└─ .gitignore             # Ignore venv, __pycache__, etc.

---

### Demo
## 🎥 Watch how the gestures work:

- ✊ Make a fist → MUTE
- ✋ Open hand → FREEZE VOLUME
- 🤏 Pinch (thumb + index) → ADJUST VOLUME

Video is located in **assets/demo_video.mp4** showing live gesture control in action.