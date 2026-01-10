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

bisa_jalan = []

for i in range(len(process)):
    if request[i] not in allocation:
        bisa_jalan.append(process[i])

print("==Deadlock Detection==")
print()
print("Jumlah proses :", len(process))
print()
print("Status sistem :")

if len(bisa_jalan) == 0:
    print("Deadlock terdeteksi")
    print()
    print("Proses yang terlibat deadlock :")
    for p in process:
        print(p)
else:
    print("Tidak terjadi deadlock")
    print()
    print("Proses yang dapat berjalan :")
    for p in bisa_jalan:
        print(p)