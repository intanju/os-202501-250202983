import os

nama_file = "reference_string.txt"
jumlah_frame = 3

def cetak_header(judul):
    print("\n" + judul)
    print("-" * len (judul))
    print("page\tF1\tF2\tF3\tStatus")
    print("-" * 45)

def cetak_baris(page,frame_list, status):
    tampilan = frame_list + ['-'] * (jumlah_frame - len(frame_list))
    print(f"{page}\t{tampilan[0]}\t{tampilan[1]}\t{tampilan[2]}\t{status}")

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, nama_file)

try:
    with open(file_path, "r") as f:
        isi = f.read().strip()
        pages = [int(x) for x in isi.split(",")]
except FileNotFoundError:
    print("File reference_string.txt tidak ditemukan!")
    exit()

print("Dataset Loaded:", pages)
print("Jumlah Frame :", jumlah_frame)

cetak_header("FIFO Page Replacement")

fifo_frames = []
fifo_fault = 0
posisi = 0  

for page in pages:
    if page in fifo_frames:
        status = "HIT"
    else:
        status = "FAULT"
        fifo_fault += 1

        if len(fifo_frames) < jumlah_frame:
            fifo_frames.append(page)
        else:
            fifo_frames[posisi] = page
            posisi = (posisi + 1) % jumlah_frame

    cetak_baris(page, fifo_frames, status)

print("\nTotal Page Fault FIFO:", fifo_fault)

cetak_header("LRU Page Replacement")

lru_frames = []
urutan_pakai = []   
lru_fault = 0

for page in pages:
    if page in lru_frames:
        status = "HIT"
        urutan_pakai.remove(page)
    else:
        status = "FAULT"
        lru_fault += 1

        if len(lru_frames) < jumlah_frame:
            lru_frames.append(page)
        else:
            lama = urutan_pakai.pop(0)
            lru_frames.remove(lama)
            lru_frames.append(page)

    urutan_pakai.append(page)
    cetak_baris(page, lru_frames, status)

print("\nTotal Page Fault LRU:", lru_fault)

print("\nPERBANDINGAN")
print("-" * 25)
print("FIFO Page Fault:", fifo_fault)
print("LRU  Page Fault:", lru_fault)

if lru_fault < fifo_fault:
    print(">> Algoritma LRU lebih efisien pada dataset ini.")
elif fifo_fault < lru_fault:
    print(">> Algoritma FIFO lebih efisien pada dataset ini.")
else:
    print(">> Kedua algoritma memiliki performa yang sama.")