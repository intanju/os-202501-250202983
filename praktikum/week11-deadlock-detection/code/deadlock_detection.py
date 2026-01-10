import csv
import os

process = []
allocation = []
request = []

file_path = os.path.join(os.path.dirname(__file__), "dataset_deadlock.csv")

with open(file_path, "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        process.append(row[0])
        allocation.append(row[1])
        request.append(row[2])

finish = [False] * len(process)
progress = True

while progress:
    progress = False
    for i in range(len(process)):
        if not finish[i]:
            # jika resource yang diminta tidak dipegang proses lain
            if request[i] not in allocation:
                finish[i] = True
                allocation[i] = "-"   # resource dilepas
                progress = True

print("== Deadlock Detection ==")
print()

deadlock_process = []

for i in range(len(process)):
    if not finish[i]:
        deadlock_process.append(process[i])

if deadlock_process:
    print("Deadlock terdeteksi")
    print("Proses yang terlibat deadlock:")
    for p in deadlock_process:
        print(p)
else:
    print("Tidak terjadi deadlock")
