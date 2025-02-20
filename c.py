import cv2
import pyautogui
import time
import numpy as np

def color_distance(color1, color2):
    return np.linalg.norm(np.array(color1) - np.array(color2))

# Target warna (B, G, R) buat on dan off
on_target = (160, 119, 76)
off_target = (131, 128, 128)

def is_on_color(b, g, r, tolerance=30):
    dist = color_distance((b, g, r), on_target)
    return dist < tolerance

def is_off_color(b, g, r, tolerance=30):
    dist = color_distance((b, g, r), off_target)
    return dist < tolerance

while True:
    # Ambil screenshot
    ss = pyautogui.screenshot()
    frame = np.array(ss)
    # Convert dari RGB (PIL) ke BGR (OpenCV)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Koordinat tombol yang udah lo tentuin
    x, y, w, h = 519, 635, 172, 105
    button_region = frame[y:y+h, x:x+w]

    # Hitung rata-rata warna di region itu
    avg_color = button_region.mean(axis=0).mean(axis=0)
    b, g, r = int(avg_color[0]), int(avg_color[1]), int(avg_color[2])
    print(f"Rata-rata warna di region: B={b}, G={g}, R={r}")

    if is_off_color(b, g, r):
        pyautogui.click(x + w//2, y + h//2)
        print("Tombol OFF, gue klik biar ON")
    elif is_on_color(b, g, r):
        print("Tombol udah ON, chill aja bro")
    else:
        print("Warnanya nggak ketebak, mungkin lo perlu atur threshold lagi")

    time.sleep(5)  # Cek tiap 5 detik, lo bisa adjust sesuai kebutuhan
