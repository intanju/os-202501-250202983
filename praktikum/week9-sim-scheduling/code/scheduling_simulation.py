import csv
import os

# BACA DATASET
file_data = os.path.join(os.path.dirname(__file__), "dataset.csv")
processes = []

with open(file_data, "r") as file:
    reader = csv.reader(file)
    next(reader) # lewati header

    for row in reader:
        processes.append({
            "name": row[0],
            "arrival": int(row[1]),
            "burst": int(row[2])
        })

# urutkan berdasarkan arrival time (FCFS)
processes.sort(key=lambda x: x["arrival"])

# SIMULASI FCFS
time = 0
total_waiting = 0
total_turnaround = 0

for p in processes:
    if time < p["arrival"]:
        time = p["arrival"]

    p["waiting"] = time - p["arrival"]
    p["turnaround"] = p["waiting"] + p["burst"]

    time += p["burst"]

    total_waiting += p["waiting"]
    total_turnaround += p["turnaround"]

# OUTPUT TABEL
print("\nHasil Simulasi Penjadwalan FCFS")
print("Proses | Arrival | Burst | Waiting | Turnaround")
print("-" * 50)

for p in processes:
    print(f"{p['name']:6} | {p['arrival']:7} | {p['burst']:5} | "
          f"{p['waiting']:7} | {p['turnaround']:10}")

print("-" * 50)
print("Rata-rata Waiting Time   :", total_waiting / len(processes))
print("Rata-rata Turnaround Time:", total_turnaround / len(processes))