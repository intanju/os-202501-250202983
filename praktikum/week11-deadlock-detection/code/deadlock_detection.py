import csv

processes = []

with open("dataset_deadlock.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        processes.append(row)
deadlock_process = []

for p in processes:
    for other in processes:
        if p["Request"] == other["Allocation"]:
            deadlock_process.append(p["Process"])
deadlock_process = list(set(deadlock_process))

print("=" * 36)
print("deadlock detection")
print("=" * 36)
print(f"\njumlah proses yang diuji : {len(processes)}\n")

if len(deadlock_process) == len(processes):
    print("hasil analisis sistem :")
    print(">> status : deadlock terdeteksi\n")
    print("daftar proses yang terlibat deadlock :")
    for p in deadlock_process:
        print(f"- {p}")

    print("\nkesimpulan :")
    print("semua proses saling menunggu resource")
    print("sehingga tidak ada proses yang dapat berjalan.")
else:
    print("Hasil Analisis Sistem :")
    print(">> status : tidak terjadi deadlock")

print("=" * 36)
