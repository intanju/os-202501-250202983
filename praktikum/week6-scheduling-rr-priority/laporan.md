
# Laporan Praktikum Minggu 6
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling 

---

## Identitas
- **Nama**  : Sukmani Intan Jumala 
- **NIM**   : 250202983  
- **Kelas** : 1 IKRA 

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung *waiting time* dan *turnaround time* pada algoritma RR dan Priority.  
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.  
3. Membandingkan performa algoritma RR dan Priority.  
4. Menjelaskan pengaruh *time quantum* dan prioritas terhadap keadilan eksekusi proses.  
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.  
---

## Dasar Teori
1. Penjadwalan CPU adalah mekanisme dalam sistem operasi yang menentukan proses mana yang akan mendapatkan akses ke CPU pada waktu tertentu. Tujuan utamanya adalah meningkatkan efisiensi, responsivitas, dan keadilan eksekusi proses  
2. Round Robin (RR) adalah algoritma preemptive yang memberikan setiap proses waktu CPU yang sama secara bergiliran, dikenal sebagai time quantum. Algoritma ini bisa dianggap sebagai pengembangan dari FCFS karena masih mengeksekusi proses sesuai urutan kedatangan, tetapi menambahkan preemption untuk meningkatkan keadilan dan responsivitas. Perbedaan ukuran time quantum memengaruhi performa, terlalu kecil meningkatkan overhead, terlalu besar membuat algoritma mirip FCFS
3. Priority Scheduling memberikan CPU kepada proses dengan prioritas tertinggi, baik secara preemptive maupun non-preemptive. Proses dengan prioritas rendah berisiko mengalami starvation. Algoritma ini memiliki kesamaan konsep dengan SJF, karena keduanya memilih proses berdasarkan kriteria tertentu.

---

## Langkah Praktikum
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
     ```
   - Catat sisa *burst time* tiap putaran.

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```

---

---

## Hasil Eksekusi

hasil tabel eksperimen 1, round robin dengan q = 3  
![Screenshot hasil](<screenshots/eksperimen1_q3.png>)  

hasil tabel sisa burst time tiap putaran  
![Screenshot hasil](<screenshots/eksperimen1_sisabt.png>)  

hasil tabel eksperimen 2, priority scheduling
urutan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi)   
![Screenshot hasil](<screenshots/eksperimen2.png>)  

hasil tabel eksperimen 3, round robin dengan q = 2 dan q = 5
![Screenshot hasil](<screenshots/eksperimen3_q2danq5.png>)  

---

## Analisis Hasil
**Eksperimen 1 – Round Robin (RR)**  
- Data proses  

| Proses | Burst Time | Arrival Time | Priority |
| :----: | :--------: | :----------: | :------: |
| P1 | 5 | 0 | 2 |
| P2 | 3 | 1 | 1 |
| P3 | 8 | 2 | 4 |
| P4 | 6 | 3 | 3 |

- *time quantum (q)* = 3  

| Proses | Burst Time | Arrival Time | Finish | Waiting Time (WT) | Turnaround Time (TAT) |
| :----: | :--------: | :----------: | :------------------: | :--------------------: | :--------------: |
| P1 | 5 | 0 | 14 | 9 | 14 |
| P2 | 3 | 1 | 6 | 2 | 5 |
| P3 | 8 | 2 | 22 | 12 | 20 |
| P4 | 6 | 3 | 20 | 11 | 17 |         

Rata-rata: 
Waiting Time (WT) = 8.5  
Turnaround Time (TAT) = 14.0  

- Gantt Chart  
```
| P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |  
 0    3    6    9   12   14   17   20   22
```
- Sisa burst time tiap putaran
  
| Putaran | Proses | Eksekusi | Sisa Burst Time |
| :-----: | :----: | :------: | :-------------: |
| 1 | P1 | 3 | 2 |
| 1 | P2 | 3 | 0 |
| 1 | P3 | 3 | 5 |
| 1 | P4 | 3 | 3 |
| 2 | P1 | 2 | 0 |
| 2 | P3 | 3 | 2 |
| 3 | P3 | 2 | 0 |

---

**Eksperimen 2 – Priority Scheduling (Non-Preemptive)**  
- Urutan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
- Perhitungan WT dan TAT
  
| Proses | Arrival | Burst | Priority | Start | Finish | Waiting Time (WT) | Turnaround Time (TAT) |
| :----: | :-----: | :---: | :------: | :---: | :------------------: | :-------------------: | :---------------: |
| P1 | 0 | 5 | 2 | 0 | 5 | 0 | 5 |
| P2 | 1 | 3 | 1 | 5 | 8 | 4 | 7 |
| P4 | 3 | 6 | 3 | 8 | 14 | 5 | 11 |
| P3 | 2 | 8 | 4| 14 | 22 | 12 | 20 |

Rata-rata :
Waiting Time (WT) = 5.25
Turnaround Time (TAT) = 10.75

Tabel Perbandingan RR dan Priority

| Algortima | Rata-rata WT | Rata-rata TAT | Kelebihan | Kekurangan |
|:---------:|:------------:|:-------------:|:----------|:-----------|
|Round Robin| 8.5 | 14.0 | Adil untuk semua proses | Bisa lambat jika quantum kurang tepat|
|Priority Scheduling| 5.25 | 10.75 | Efisien untuk proses penting | Proses prioritas rendah menunggu lama (starvation) |

**Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**  
*time quantum (q)* = 2  

| Proses |Burst Time | Arrival Time | Finish | Waiting Time (WT) | Turnaround Time (TAT) |
| :----: | :-------: | :----------: | :----: | :---------------: | :-------------------: |
| P1 | 5 | 0 | 14 | 9 | 14 |
| P2 | 3 | 1 | 6 | 2 | 5 | 
| P3 | 8 | 2 | 22 | 12 | 20 |
| P4 | 6 | 3 | 20 | 11 | 17 |

Rata-rata:
Waiting Time (WT) = 8.5  
Turnaround Time (TAT) = 14.0  

*time quantum (q)* = 5  

| Proses |Burst Time | Arrival Time | Finish | Waiting Time (WT) | Turnaround Time (TAT) |
| :----: | :-------: | :----------: | :----: | :---------------: | :-------------------: |
| P1 | 5 | 0 | 5 | 0 | 5 |
| P2 | 3 | 1 | 8 | 4 | 7 | 
| P3 | 8 | 2 | 22 | 12 | 20 |
| P4 | 6 | 3 | 19 | 10 | 16 |

Rata-rata:
Waiting Time (WT) = 6.5  
Turnaround Time (TAT) = 12.0

Tabel perbandingan efek *quantum*
| Quantum (q) | Rata-rata WT | Rata-rata TAT | Analisis Singkat |
| :---------: | :----------: | :-----------: | :--------------- |
| 2 | 8.5 | 14.0 | Proses sering bergantian, banyak context switching, respon cepat |
| 5 | 6.5 | 12.0 | Proses hampir selesai sekali jalan, mirip FCFS, WT lebih rendah |


## Kesimpulan
1. Dari Eksperimen 1 (RR quantum 3), terlihat kalau semua proses mendapat giliran CPU secara adil. Proses yang panjang tetap harus beberapa kali masuk CPU, jadi waiting time-nya lebih tinggi dibanding proses pendek  
2. Dari Eksperimen 2 (Priority Scheduling), proses dengan prioritas tinggi selesai lebih cepat, tapi proses prioritas rendah harus menunggu lebih lama. Jadi terlihat jelas trade-off, sistem responsif untuk proses penting, tetapi kurang adil dibanding Round Robin
3. Dari Eksperimen 3 (Variasi Quantum RR), nilai quantum memengaruhi performa:  
Quantum kecil → proses sering bergantian, respon cepat, tapi banyak context switching  
Quantum besar → proses jarang bergantian, waiting time rata-rata turun, perilaku RR mirip FCFS  
4. Secara umum, pemilihan algoritma dan quantum harus disesuaikan dengan karakteristik proses dan kebutuhan sistem, supaya keseimbangan antara fairness, responsivitas, dan efisiensi CPU tetap terjaga.

---

## Quiz  
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?
   **jawaban**: Perbedaan utamanya ada pada cara CPU membagi waktu eksekusi. Round Robin membagi CPU secara adil sesuai time quantum, sehingga semua proses mendapat giliran, sementara Priority Scheduling menjalankan proses berdasarkan prioritas, membuat proses penting cepat selesai tapi proses prioritas rendah menunggu lebih lama  
3. Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?
   **jawaban**: Time quantum yang kecil membuat proses sering bergantian, jadi sistem terasa lebih responsif, tapi context switching menjadi lebih banyak dan bisa menurunkan efisiensi CPU. Sebaliknya, time quantum yang besar membuat proses jarang bergantian, sehingga waiting time rata-rata bisa turun dan eksekusi lebih efisien, tapi sistem jadi kurang responsif dan perilakunya mulai mirip FCFS karena satu proses bisa memonopoli CPU lebih lama  
5. Mengapa algoritma Priority dapat menyebabkan *starvation*?
   **jawaban**: Karena algoritam tersebut menjalankan proses dengan mendahulukan proses yang memiliki prioritas tinggi terlebih dahulu, sehingga proses dengan prioritas rendah bisa menunggu lebih lama dan semakin lama, bahkan kadang bisa tidak pernah dieksekusi jika proses prioritas tinggi ada yang masuk terus menerus ke CPU
   
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  Bagian paling menantang dalam eksperimen kali ini adalah mengikuti urutan eksekusi proses di Round Robin yang bolak-balik beberapa putaran
- Bagaimana cara Anda mengatasinya?  
  Pahami langkah-langkah dan konsentrasi
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
