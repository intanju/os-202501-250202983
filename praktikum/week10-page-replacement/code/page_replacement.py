# Simulasi Page Replacement
# FIFO dan LRU
# Praktikum Sistem Operasi

import os

# ===============================
# BACA FILE (AMAN)
# ===============================
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "reference_string.txt")

with open(file_path, "r") as file:
    data = file.read()

# Bersihkan data (hindari error)
pages = []
for p in data.replace("\n", "").split(","):
    if p.strip() != "":
        pages.append(int(p.strip()))

jumlah_frame = 3


# ===============================
# FIFO
# ===============================
frames_fifo = []
fifo_faults = 0
pointer = 0

print("=== SIMULASI FIFO ===")
print("Page | Frame | Status")
print("----------------------")

for page in pages:
    if page in frames_fifo:
        status = "HIT"
    else:
        status = "FAULT"
        fifo_faults += 1

        if len(frames_fifo) < jumlah_frame:
            frames_fifo.append(page)
        else:
            frames_fifo[pointer] = page
            pointer = (pointer + 1) % jumlah_frame

    print(f"{page}    | {frames_fifo} | {status}")

print("Total Page Fault FIFO:", fifo_faults)
print()


# ===============================
# LRU
# ===============================
frames_lru = []
lru_faults = 0

print("=== SIMULASI LRU ===")
print("Page | Frame | Status")
print("----------------------")

for page in pages:
    if page in frames_lru:
        status = "HIT"
        frames_lru.remove(page)
        frames_lru.append(page)
    else:
        status = "FAULT"
        lru_faults += 1

        if len(frames_lru) < jumlah_frame:
            frames_lru.append(page)
        else:
            frames_lru.pop(0)
            frames_lru.append(page)

    print(f"{page}    | {frames_lru} | {status}")

print("Total Page Fault LRU:", lru_faults)


# ===============================
# PERBANDINGAN
# ===============================
print("\n=== PERBANDINGAN ===")
print("FIFO Page Fault :", fifo_faults)
print("LRU Page Fault  :", lru_faults)
