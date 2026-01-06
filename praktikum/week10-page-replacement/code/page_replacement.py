import os

file_name = "reference_string.txt"
frame_count = 3

def print_header(title):
    print(f"\n{title}")
    print("-" * len(title))
    print("Page\tFrame1\tFrame2\tFrame3\tStatus")
    print("-" * 45)

def print_row(page, frames, status):
    display = frames + ['-'] * (frame_count - len(frames))
    print(f"{page}\t{display[0]}\t{display[1]}\t{display[2]}\t{status}")

base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, file_name)

try:
    with open(path, "r") as f:
        content = f.read().strip()
        reference_pages = [int(x) for x in content.split(",")]
except FileNotFoundError:
    print(f"File {file_name} tidak ditemukan!")
    exit()

print("Dataset Loaded:", reference_pages)
print("Jumlah Frame :", frame_count)

print_header("FIFO Page Replacement")

fifo_mem = []
fifo_index = 0
fifo_faults = 0

for page in reference_pages:
    if page in fifo_mem:
        status = "HIT"
    else:
        status = "FAULT"
        fifo_faults += 1

        if len(fifo_mem) < frame_count:
            fifo_mem.append(page)
        else:
            fifo_mem[fifo_index] = page
            fifo_index = (fifo_index + 1) % frame_count

    print_row(page, fifo_mem, status)

print("\nTotal Page Fault FIFO:", fifo_faults)

print_header("LRU Page Replacement")

lru_mem = []
recent_order = []  
lru_faults = 0

for page in reference_pages:
    if page in lru_mem:
        status = "HIT"
        recent_order.remove(page)
    else:
        status = "FAULT"
        lru_faults += 1

        if len(lru_mem) < frame_count:
            lru_mem.append(page)
        else:
            oldest = recent_order.pop(0)
            lru_mem[lru_mem.index(oldest)] = page

    recent_order.append(page)
    print_row(page, lru_mem, status)

print("\nTotal Page Fault LRU:", lru_faults)