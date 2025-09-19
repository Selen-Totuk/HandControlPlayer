# ------------------------------------------
# El Hareketiyle Bilgisayar Kontrolü
# - Avuç açık -> Müzik aç/kapat (sistem medya tuşu)
# - İşaret parmağı -> Ekran görüntüsü (Masaüstü)
# ------------------------------------------

import cv2
import mediapipe as mp
import pyautogui
import keyboard
import time
import os

# MediaPipe Hands başlat
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# Kamera başlat
cap = cv2.VideoCapture(0)

prev_action_time = 0
action_delay = 1  # saniye

# Masaüstü yolu
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

print("El kontrol sistemi başlatıldı. ESC ile çıkabilirsiniz.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera açılamadı.")
        break

    frame = cv2.flip(frame, 1)  # Ayna efekti
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            tips = [8, 12, 16, 20]  # İşaret, orta, yüzük, serçe parmak uçları
            fingers_up = []
            for tip in tips:
                if handLms.landmark[tip].y < handLms.landmark[tip - 2].y:
                    fingers_up.append(1)
                else:
                    fingers_up.append(0)

            current_time = time.time()
            if current_time - prev_action_time > action_delay:
                # Avuç açık -> Medya Play/Pause
                if fingers_up == [1, 1, 1, 1]:
                    keyboard.send("play/pause media")
                    prev_action_time = current_time
                    print("Müzik aç/kapat (sistem medya tuşu)")

                # Sadece işaret parmağı -> Ekran görüntüsü
                elif fingers_up == [1, 0, 0, 0]:
                    screenshot = pyautogui.screenshot()
                    save_path = os.path.join(desktop_path, "ekran.png")
                    screenshot.save(save_path)
                    prev_action_time = current_time
                    print(f"Ekran görüntüsü alındı: {save_path}")

    cv2.imshow("El Kontrol", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC ile çık
        break

cap.release()
cv2.destroyAllWindows()
print("El kontrol sistemi kapatıldı.")
