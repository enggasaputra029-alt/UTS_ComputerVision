# ============================================
# 🧠 UTS Computer Vision
# 👤 Nama: Engga Saputra
# 🆔 NIM: 43050230029
# ============================================

import cv2
import numpy as np
import os

# 🔹 Buat folder output jika belum ada
os.makedirs("output", exist_ok=True)

# ============================================
# 1️⃣ Membuat Karakter Buatan Sendiri (Orang Memancing)
# ============================================

# Buat kanvas (latar langit biru muda)
canvas = np.full((400, 600, 3), (180, 230, 255), dtype=np.uint8)

# Gambar air (bagian bawah)
cv2.rectangle(canvas, (0, 300), (600, 400), (200, 230, 255), -1)
cv2.rectangle(canvas, (0, 300), (600, 400), (100, 170, 250), 2)

# Gambar tepi tanah (brown)
cv2.rectangle(canvas, (0, 280), (600, 300), (80, 50, 20), -1)

# Tubuh pemancing (stickman)
# Kepala
cv2.circle(canvas, (150, 200), 20, (0, 0, 0), 2)
cv2.circle(canvas, (150, 200), 19, (230, 220, 200), -1)

# Badan
cv2.line(canvas, (150, 220), (150, 270), (0, 0, 0), 3)

# Tangan
cv2.line(canvas, (150, 230), (180, 250), (0, 0, 0), 3)

# Kaki
cv2.line(canvas, (150, 270), (140, 300), (0, 0, 0), 3)
cv2.line(canvas, (150, 270), (160, 300), (0, 0, 0), 3)

# Joran pancing
cv2.line(canvas, (180, 250), (300, 180), (60, 40, 10), 3)

# Tali pancing
cv2.line(canvas, (300, 180), (310, 290), (0, 0, 0), 1)

# Ikan (sederhana)
cv2.ellipse(canvas, (320, 310), (20, 10), 0, 0, 360, (0, 100, 255), -1)
cv2.circle(canvas, (330, 310), 3, (0, 0, 0), -1)

# Simpan karakter asli
cv2.imwrite("output/karakter.png", canvas)

# ============================================
# 2️⃣ Transformasi Citra
# ============================================

# Translasi
M_trans = np.float32([[1, 0, 30], [0, 1, -10]])
translate = cv2.warpAffine(canvas, M_trans, (600, 400))
cv2.imwrite("output/translate.png", translate)

# Rotasi
M_rot = cv2.getRotationMatrix2D((300, 200), 10, 1)
rotate = cv2.warpAffine(canvas, M_rot, (600, 400))
cv2.imwrite("output/rotate.png", rotate)

# Resize
resize = cv2.resize(canvas, (300, 200))
cv2.imwrite("output/resize.png", resize)

# Crop (area orang dan joran)
crop = canvas[150:310, 100:320]
cv2.imwrite("output/crop.png", crop)

# ============================================
# 3️⃣ Operasi Bitwise
# ============================================

# Buat background tambahan (warna senja)
bg = np.full((400, 600, 3), (255, 200, 150), dtype=np.uint8)

# Buat mask dari karakter
mask_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
_, mask_inv = cv2.threshold(mask_gray, 250, 255, cv2.THRESH_BINARY_INV)

# Operasi bitwise
bit_and = cv2.bitwise_and(bg, bg, mask=mask_inv)
bit_or = cv2.bitwise_or(canvas, bit_and)
cv2.imwrite("output/bitwise.png", bit_or)

# Gabungan akhir
final = cv2.addWeighted(rotate, 0.7, bit_or, 0.3, 0)
cv2.imwrite("output/final.png", final)

# ============================================
# 4️⃣ Tampilkan Hasil Akhir
# ============================================

cv2.imshow("Karakter Pemancing", canvas)
cv2.imshow("Transformasi: Rotasi", rotate)
cv2.imshow("Operasi Bitwise", bit_or)
cv2.imshow("Hasil Akhir", final)

print("✅ Semua gambar berhasil disimpan di folder 'output'")

cv2.waitKey(0)
cv2.destroyAllWindows()