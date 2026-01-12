import time

data = []
i = 0

print("Program uji resource limit dimulai...")
print("Tekan Ctrl+C untuk menghentikan\n")

try:
    while True:
        total = 0
        for x in range(1_000_000):
            total += x * x

        data.append("X" * 5_000_000)

        i += 1
        print(f"Iterasi {i} | Total hitung: {total} | Perkiraan memori: {len(data)*5} MB")

        time.sleep(1)
except MemoryError:
    print("ERROR: Memori tidak cukup! Container terkena limit memori.")
except KeyboardInterrupt:
    print("\nProgram dihentikan manual.")
