
# Laporan Praktikum Minggu 9
Topik: Simulasi Algoritma Penjadwalan CPU  

---

## Identitas
- **Nama**  : Sukmani Intan Jumala
- **NIM**   : 250202983
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.  
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.  
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.  
4. Menjelaskan hasil simulasi secara tertulis.  
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
- Penjadwalan CPU adalah proses pengaturan urutan eksekusi proses di sistem operasi agar penggunaan CPU optimal serta waktu tunggu dan penyelesaian proses dapat diminimalkan (Silberschatz et al., 2018).
- FCFS (First-Come First-Served) menjalankan proses berdasarkan urutan kedatangan secara non-preemptive, mudah diimplementasikan namun dapat menyebabkan proses pendek menunggu lama di belakang proses panjang (convoy effect) (Tanenbaum & Bos, 2014).
- SJF (Shortest Job First) memilih proses dengan burst time terpendek terlebih dahulu sehingga rata-rata waktu tunggu rendah, namun dapat menyebabkan proses panjang tertunda atau starvation (Arpaci-Dusseau & Arpaci-Dusseau, 2019).
- Waiting time dan turnaround time digunakan untuk mengevaluasi performa algoritma, simulasi membantu menghitung kedua metrik tersebut secara otomatis sehingga lebih akurat untuk dataset yang lebih besar.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**
   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**
   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```
   
---

## Kode / Perintah
```bash
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
```

---

## Hasil Eksekusi
![Screenshot hasil](screenshots/hasil_simulasi.png)

---

# Analisis  
- Alur Program  
  Dalam praktikum ini, saya memutuskan untuk menggunakan algoritma FCFS. Pilihan ini bukan berarti saya menolak atau tidak ingin mempelajari lebih dalam tentang algoritma SJF. Tapi saya memilih algoritma FCFS karena saya sudah cukup memahami logikanya dan lebih mudah untuk saya analisis dan jelaskan. Berdasarkan program yang saya jalankan sebelumnya, berikut analisis alur nya:
   - Program dimulai dengan membaca dataset `dataset.csv`, Pada kode berikut:  
  ```bash
  with open(file_data, "r") as file:
    reader = csv.reader(file)
    next(reader) # lewati header

    for row in reader:
        processes.append({
            "name": row[0],
            "arrival": int(row[1]),
            "burst": int(row[2])
        })
  ```
  dapat dilihat bahwa setiap baris data diubah menjadi dictionary berisi name, arrival, dan burst. Dari kode ini, terlihat bahwa program menyiapkan struktur data yang memudahkan proses selanjutnya, terutama untuk pengurutan dan perhitungan waktu
   - Langkah berikutnya adalah mengurutkan proses berdasarkan arrival time:  
  ```bash
  processes.sort(key=lambda x: x["arrival"])
  ```
  Kode ini menunjukkan inti FCFS: proses dieksekusi sesuai urutan kedatangan. Dari sini, kita bisa melihat bahwa urutan proses sudah siap untuk simulasi.

   - Simulasi eksekusi dilakukan dengan blok berikut:
  ```bash
  for p in processes:
    if time < p["arrival"]:
        time = p["arrival"]

    p["waiting"] = time - p["arrival"]
    p["turnaround"] = p["waiting"] + p["burst"]

    time += p["burst"]
  ```
  Dari kode ini, terlihat logika penghitungan waiting time dan turnaround time. Jika CPU sedang idle ketika proses tiba, nilai time disesuaikan sehingga proses dapat langsung dieksekusi. Kemudian, waktu tunggu dan turnaround dihitung secara otomatis, dan total waktunya diakumulasi untuk menghitung rata-rata.
   - Hasil simulasi ditampilkan dalam bentuk tabel menggunakan kode:
  ```bash
  for p in processes:
    print(f"{p['name']:6} | {p['arrival']:7} | {p['burst']:5} | "
          f"{p['waiting']:7} | {p['turnaround']:10}")
  ```
  Dari sini, dapat dilihat semua informasi proses, mulai dari arrival dan burst, hingga waiting time dan turnaround time. Dengan cara ini, pembaca bisa langsung memahami urutan eksekusi setiap proses dan efektivitas algoritma FCFS.

- Bandingkan hasil simulasi dengan perhitungan manual  
  Dari hasil program, diperoleh tabel simulasi sebagai berikut:
  
  |Proses|AT|BT|WT|TAT|
  |:---:|:--:|:--:|:--:|:--:|
  |P1|0|6|0|6|
  |P2|1|8|5|13|
  |P3|2|7|12|19|
  |P4|3|3|18|21|

  Dari hasil simulasi program FCFS diatas, diperoleh rata-rata Waiting Time 8.75 dan rata-rata Turnaround Time 14.75. Jika dibandingkan dengan perhitungan manual yang dilakukan pada praktikum minggu sebelumnya(tepatnya minggu ke-5), hasilnya sama.
  Secara prinsip, hasil simulasi dan perhitungan manual memberikan nilai waiting time dan turnaround time yang sama karena menggunakan rumus dan logika algoritma yang sama. Perbedaannya adalah pada proses pengerjaan, yang mana perhitungan manual membutuhkan langkah-langkah hitungan satu per satu sehingga lebih lama dan rawan salah, sedangkan simulasi menghitung secara otomatis sehingga lebih cepat, konsisten, dan praktis terutama ketika jumlah proses semakin banyak
       
- Kelebihan dan keterbatasan simulasi  
  **Kelebihan:**
   - Penghitungan waktu tunggu dan turnaround dilakukan secara cepat dan akurat dari kode simulasi.
   - Struktur data dan logika program memudahkan analisis untuk dataset lebih besar
     
  **Keterbatasan:**
   - Bergantung pada akurasi dataset input.
   - Tidak memperhitungkan overhead context switching atau interupsi nyata pada OS  

---

## Kesimpulan  
Dari praktikum ini, tujuan utama yaitu mampu membuat program simulasi penjadwalan CPU telah tercapai. Dengan menjalankan program, saya belajar langsung bagaimana membaca dataset, mengurutkan proses, menghitung waiting time dan turnaround time, serta menampilkan hasilnya secara otomatis dalam bentuk tabel.

Pengalaman membuat program ini membuat saya lebih memahami bagaimana logika penjadwalan bekerja secara nyata, termasuk bagaimana proses menunggu dan dieksekusi. Praktikum ini juga memperlihatkan keterbatasan simulasi, seperti proses yang harus menunggu lama karena urutan eksekusi, sehingga saya menyadari fenomena Convoy Effect secara langsung.

Secara keseluruhan, praktikum ini membantu saya memahami logika penjadwalan CPU sekaligus praktik membuat simulasi program Python dengan lebih mudah dan nyata


---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?  
   Simulasi diperlukan karena memungkinkan algoritma untuk diuji dalam berbagai situasi tanpa perlu menjalankan proses sebenarnya. Dengan simulasi, perhitungan waiting time, turnaround time, dan performa algoritma bisa diobservasi secara otomatis, lebih cepat, dan konsisten, terutama ketika jumlah proses yang dihadapi besar.
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?  
   Dalam dataset yang besar, perhitungan secara manual berisiko keliru dan memerlukan waktu, sedangkan simulasi memberikan hasil yang setara secara prinsip namun lebih tepat dan efisien karena perhitungan dilakukan oleh program. Simulasi juga memungkinkan pengujian kembali dengan dataset yang berbeda tanpa perlu melakukan pekerjaan besar ulang.
3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.  
   FCFS lebih gampang diterapkan karena hanya memerlukan pengurutan berdasarkan waktu kedatangan dan eksekusi berurutan dari antrian, tanpa perlu membandingkan burst time atau menjadwalkan ulang proses. SJF membutuhkan pemilihan proses terpendek setiap kali CPU siap, sehingga lebih kompleks terutama dalam memastikan pemilihan proses secara dinamis.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  Bagian tersulit adalah membuat program simulasi karena saya belum terlalu terbiasa dan belum hafal sintaks bahasa pemrograman
- Bagaimana cara Anda mengatasinya?
  Saya belajar dan mencoba contoh kode sederhana kemudian berlatih menjalankan program sedikit demi sedikit sampai mulai paham alurnya. Pastinya juga meminta bantuan dengan teman serta ai saat mengalami kesulitan

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
