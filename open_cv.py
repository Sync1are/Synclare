import cv2
import mediapipe as mp
import pyautogui
import time
import math

# Setup
pyautogui.FAILSAFE = False
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.6, min_tracking_confidence=0.6)

# Screen size
screen_w, screen_h = pyautogui.size()

# Smoothing and click
SMOOTHING = 7
CLICK_DIST_THRESHOLD = 40
CLICK_COOLDOWN = 0.35
prev_x, prev_y = 0, 0
last_click = 0

def distance(p1, p2):
    return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip horizontally so it feels natural
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    h, w, _ = frame.shape

    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Get index and middle fingertips
        lm_list = []
        for id, lm in enumerate(hand_landmarks.landmark):
            lm_list.append((int(lm.x * w), int(lm.y * h)))

        index_finger = lm_list[8]
        middle_finger = lm_list[12]

        # Map to screen
        screen_x = index_finger[0] * screen_w / w
        screen_y = index_finger[1] * screen_h / h

        # Smooth movement
        smooth_x = prev_x + (screen_x - prev_x) / SMOOTHING
        smooth_y = prev_y + (screen_y - prev_y) / SMOOTHING
        prev_x, prev_y = smooth_x, smooth_y

        pyautogui.moveTo(smooth_x, smooth_y)

        # Click detection
        dist = distance(index_finger, middle_finger)
        now = time.time()
        if dist < CLICK_DIST_THRESHOLD and now - last_click > CLICK_COOLDOWN:
            pyautogui.click()
            last_click = now
            cv2.putText(frame, "CLICK", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

    cv2.putText(frame, "Press ESC to exit", (10, h-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200,200,200), 1)
    cv2.imshow("Finger Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
