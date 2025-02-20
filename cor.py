import pyautogui

print("Geser mouse lu ke pojok kiri-atas area tombol, terus pencet Enter...")
input()  # Tunggu lu pencet Enter
x1, y1 = pyautogui.position()
print(f"Koordinat kiri-atas: ({x1}, {y1})")

print("Sekarang geser mouse lu ke pojok kanan-bawah area tombol, terus pencet Enter...")
input()  # Tunggu lu pencet Enter
x2, y2 = pyautogui.position()
print(f"Koordinat kanan-bawah: ({x2}, {y2})")

# Hitung width & height
w = x2 - x1
h = y2 - y1

print(f"x = {x1}, y = {y1}, w = {w}, h = {h}")

