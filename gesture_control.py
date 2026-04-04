import cv2
import mediapipe as mp
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

def get_fingers_up(hand_landmarks):
    fingers = []
    tips = [4, 8, 12, 16, 20]

    # Thumb
    if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for tip in tips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers


def get_gesture_data(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            h, w, _ = frame.shape

            x1 = int(hand_landmarks.landmark[4].x * w)
            y1 = int(hand_landmarks.landmark[4].y * h)

            x2 = int(hand_landmarks.landmark[8].x * w)
            y2 = int(hand_landmarks.landmark[8].y * h)

            length = math.hypot(x2 - x1, y2 - y1)

            fingers = get_fingers_up(hand_landmarks)

            return length, fingers

    return None, None