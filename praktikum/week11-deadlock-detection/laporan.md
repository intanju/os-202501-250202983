
# Laporan Praktikum Minggu 11
Topik: Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Sukmani Intan Jumala
- **NIM**   : 250202983
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program sederhana untuk mendeteksi deadlock.  
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.  
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.  
4. Memberikan interpretasi hasil uji secara logis dan sistematis.  
5. Menyusun laporan praktikum sesuai format yang ditentukan.

---

## Dasar Teori
1. Pengertian Deadlock
Deadlock merupakan kondisi di mana dua atau lebih proses saling menunggu resource yang sedang digunakan oleh proses lain, sehingga tidak ada proses yang dapat melanjutkan eksekusi dan sistem berhenti.
(Silberschatz et al., 2018; Tanenbaum, 2015)  
2. Empat Kondisi Deadlock  
Deadlock dapat terjadi jika empat kondisi terpenuhi secara bersamaan, yaitu mutual exclusion, hold and wait, no preemption, dan circular wait. Jika salah satu kondisi tidak terpenuhi, maka deadlock tidak akan terjadi.
(Silberschatz et al., 2018)
3.  Deteksi Deadlock
Deteksi deadlock dilakukan dengan membiarkan sistem berjalan normal, kemudian secara berkala memeriksa hubungan antara proses dan resource untuk mengetahui apakah terjadi deadlock, misalnya dengan mendeteksi adanya siklus pada graf alokasi resource.
(OSTEP – Deadlock Detection)

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```

---

## Kode / Perintah
```bash
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
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/hasil_deteksi.png)

---

## Analisis
- Tabel Hasil Deteksi
  
  | Proses | Status |
  |:---:|:---:|
  | P1 | deadlock | 
  | P2 | deadlock |
  | P3 | deadlock |
- Validasi Manual
  - P1 menunggu R2 yang dipegang P2
  - P2 menunggu R3 yang dipegang P3
  - P3 menunggu R1 yang dipegang P1  
Maka terjadi circular wait. Tidak ada proses yang bisa lanjut sehingga hasil program sudah sesuai dengan analisis manual.
- Berdasarkan hasil deteksi dengan program yang telah dibuat, semua proses yang diuji berada dalam keadaan deadlock. Hal itu terpantau dari hasil program yang menunjukkan bahwa tidak ada proses yang dapat diselesaikan. Deadlock muncul ketika setiap proses memegang satu resource sambil meminta resource lain yang sedang dipakai oleh proses yang berbeda. Situasi ini mengakibatkan semua proses terhambat saling menunggu dan tidak ada yang dapat melanjutkan eksekusi.  
Jika dikaitkan dengan teori deadlock, kondisi ini memenuhi empat syarat terjadinya deadlock, yaitu:  
   - Mutual Exclusion, resource hanya dapat digunakan oleh satu proses dalam satu waktu.  
   - Hold and Wait, proses menahan resource sambil menunggu resource lain.  
   - No Preemption, resource tidak dapat diambil secara paksa dari proses lain.  
   - Circular Wait, terdapat siklus saling menunggu antar proses (P1 -> P2 -> P3 -> P1)  
Karena keempat kondisi tersebut terpenuhi, sistem berada dalam kondisi deadlock.  
---

## Kesimpulan
- Deadlock dapat dideteksi dengan menganalisis hubungan antara proses dan resource melalui program simulasi yang dibuat.  
- Hasil simulasi menunjukkan bahwa data proses yang digunakan menyebabkan sistem berada dalam kondisi deadlock, karena setiap proses memegang satu resource dan menunggu resource lain yang sedang digunakan oleh proses lain. Akibatnya, tidak ada proses yang dapat berjalan.  
- Kondisi deadlock yang terdeteksi sesuai dengan teori deadlock, di mana empat syarat deadlock (mutual exclusion, hold and wait, no preemption, dan circular wait) terpenuhi.

---

## Quiz
1. Apa perbedaan antara *deadlock prevention*, *avoidance*, dan *detection*?
   - Prevention: mencegah agar deadlock tidak mungkin terjadi.  
   - Avoidance: menghindari kondisi yang berpotensi menyebabkan deadlock.
   - Detection: membiarkan deadlock terjadi lalu mendeteksinya.
2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?
Karena tidak semua deadlock bisa dicegah atau dihindari sejak awal. Pada sistem yang kompleks, deadlock bisa saja terjadi. Dengan deteksi deadlock, sistem operasi bisa mengetahui adanya deadlock dan melakukan tindakan pemulihan.
3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?

   Kelebihan:  
   - Pemanfaatan resource lebih efisien karena sistem tidak membatasi alokasi sejak awal seperti pada metode pencegahan.  
   - Tidak memerlukan prediksi kebutuhan resource maksimum proses di awal, sehingga lebih fleksibel.  
   - Deadlock yang terjadi dapat dideteksi dan ditangani melalui mekanisme pemulihan.  
   - Memberikan gambaran perilaku sistem dan hubungan antar proses yang berguna untuk evaluasi desain sistem.

   Kekurangan:  
   - Memiliki overhead kinerja karena sistem harus melakukan pengecekan deadlock secara berkala.  
   - Proses pemulihan cukup kompleks dan dapat menyebabkan penghentian proses serta kehilangan data.  
   - Deteksi deadlock tidak selalu akurat dan berpotensi menghasilkan kesalahan deteksi.  
   - Penghentian proses untuk memutus deadlock dapat menghilangkan kemajuan proses yang sudah berjalan.

---

## Refleksi diri  
1. Apa bagian yang paling menantang minggu ini?
   Memahami konsep deadlock dan alur saling menunggu antar proses, lalu mengubahnya menjadi logika program yang benar
2. Bagaimana cara anda mengatasinya?
   Saya buka beberapa materi dan contoh dari internet, lalu coba pahami pakai cara sendiri. Setelah itu saya tes berulang-ulang sampai hasilnya sesuai.
   

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
