import cv2
import numpy as np

from gesture_control import get_gesture_data
from volume_control import setVolume, mute, unmute

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    length, fingers = get_gesture_data(frame)

    mode = "NONE"

    if fingers:

        # ✊ MUTE
        if fingers.count(1) == 0:
            mode = "MUTE"
            mute()

        # ✋ FREEZE VOLUME
        elif fingers.count(1) >= 4:
            mode = "FREEZE VOLUME"

        # 🤏 ADJUST
        elif fingers[0] == 1 and fingers[1] == 1 and fingers.count(1) <= 2:
            mode = "ADJUST"
            unmute()
            setVolume(length)

    # 🔥 UI: Show mode
    cv2.putText(frame, mode, (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255, 0, 0), 3)

    cv2.imshow("Gesture Volume Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()