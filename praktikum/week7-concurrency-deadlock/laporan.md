
# Laporan Praktikum Minggu 7
Topik: Sinkronisasi Proses dan Masalah Deadlock

---

## Identitas Kelompok
- **Nama**  : Sukmani Intan Jumala (250202983)
- **Nama**  : Novia Safitri (250202923)
- **Nama**  : Ismatul Khoeriyah (250202912)

---

## Deskripsi Singkat
Pada praktikum minggu ini, mahasiswa akan mempelajari **mekanisme sinkronisasi proses dan penanganan deadlock** dalam sistem operasi.  
Tujuan utamanya adalah memahami bagaimana beberapa proses dapat berjalan secara bersamaan (concurrent) tanpa menyebabkan konflik data atau kebuntuan sumber daya (*deadlock*).

Mahasiswa akan melakukan studi kasus berbasis **Dining Philosophers Problem**, yaitu permasalahan klasik sinkronisasi yang menggambarkan bagaimana proses harus berbagi sumber daya terbatas (chopstick, mutex, semaphore) tanpa menimbulkan deadlock.  

Eksperimen ini dilakukan secara berkelompok, difokuskan pada:
- Analisis kondisi terjadinya deadlock.
- Implementasi solusi sinkronisasi menggunakan *semaphore* atau *monitor*.
- Dokumentasi perbandingan versi deadlock dan versi fixed.

--- 

## Tujuan
1. Mahasiswa mampu mengidentifikasi empat kondisi penyebab deadlock (mutual exclusion, hold and wait, no preemption, circular wait).  
2. Mahasiswa mampu menjelaskan mekanisme sinkronisasi menggunakan semaphore atau monitor.  
3. Mahasiswa mampu menganalisis dan memberikan solusi untuk kasus deadlock.  
4. Mahasiswa mampu berkolaborasi dalam tim untuk menyusun laporan analisis.  
5. Mahasiswa mampu menyajikan hasil studi kasus secara sistematis.
   
---

## Dasar Teori
Sinkronisasi proses adalah cara untuk mengatur sebagian proses yang berjalan bersamaan (concurrent) agar tidak terjadi bentrokan saat mengakses data yang sama. Tujuan supaya data tetap konsisten proses berjalan dengan teratur tanpa saling menganggu. Metode seperti semaphore dan mutex membantu untuk memastikan hanya satu proses yang masuk ke bagian sistem pada satu waktu, sehingga data tetap aman dan hasil kerja tidak berantakan.
Deadlock terjadi ketika beberapa proses berhenti total karena saling menunggu sumber daya yang sedang digunakan di proses lain, sehingga tidak ada yang bisa maju atau selesai. Deadlock biasanya muncul jika 4 kondisi ini terpenuhi:
- Mutual Exclusion: satu sumber daya hanya bisa dipakai oleh satu proses.
- Hold and Wait: proses menahan satu sumber daya sambil menunggu yang lain.
- No Preemption: sumber daya tidak bisa diambil paksa dari proses lain.
- Circular Wait: terbentuk lingkaran menunggu, sehingga semua proses berhenti.

Pencegahan Deadlock dapat dilakukan dengan semaphore, monitor, atau mengatur urutan pengambilan sumber daya agar proses tidak saling menunggu dalam lingkaran (circular wait). Dengan mekanisme tersebut, proses dapat berjalan lancar dan risiko deadlock dapat diminimalkan.

---

## Langkah Pengerjaan
1. **Persiapan Tim**
   - Bentuk kelompok beranggotakan 3–4 orang.  
   - Tentukan ketua dan pembagian tugas (analisis, implementasi, dokumentasi).

2. **Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**
   - Implementasikan versi sederhana dari masalah *Dining Philosophers* tanpa mekanisme pencegahan deadlock.  
   - Contoh pseudocode:
     ```text
     while true:
       think()
       pick_left_fork()
       pick_right_fork()
       eat()
       put_left_fork()
       put_right_fork()
     ```
   - Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).  
   - Identifikasi kapan dan mengapa deadlock terjadi.

3. **Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)**
   - Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:
     - Menggunakan *semaphore (mutex)* untuk mengontrol akses.
     - Membatasi jumlah filosof yang dapat makan bersamaan (max 4).  
     - Mengatur urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).  
   - Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.

4. **Eksperimen 3 – Analisis Deadlock**
   - Jelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut dipecahkan pada versi fixed.  
   - Sajikan hasil analisis dalam tabel seperti contoh berikut:

     | Kondisi Deadlock | Terjadi di Versi Deadlock | Solusi di Versi Fixed |
     |------------------|---------------------------|------------------------|
     | Mutual Exclusion | Ya (satu garpu hanya satu proses) | Gunakan semaphore untuk kontrol akses |
     | Hold and Wait | Ya | Hindari proses menahan lebih dari satu sumber daya |
     | No Preemption | Ya | Tidak ada mekanisme pelepasan paksa |
     | Circular Wait | Ya | Ubah urutan pengambilan sumber daya |

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua diagram, screenshot simulasi, dan hasil diskusi di:
     ```
     praktikum/week7-concurrency-deadlock/screenshots/
     ```
   - Tuliskan laporan kelompok di `laporan.md` (format IMRaD singkat: *Pendahuluan, Metode, Hasil, Analisis, Diskusi*).

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 7 - Sinkronisasi Proses & Deadlock"
   git push origin main
   ```

---

## Analisis Hasil
**Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**  
- Implementasikan versi sederhana dari masalah *Dining Philosophers* tanpa mekanisme pencegahan deadlock  
```text
Semua filosof mulai: think()

Langkah 1:
F0 mengambil garpu kiri (G0)
F1 mengambil garpu kiri (G1)
F2 mengambil garpu kiri (G2)
F3 mengambil garpu kiri (G3)
F4 mengambil garpu kiri (G4)

Semua garpu kiri sekarang terpakai.

Langkah 2:
F0 mencoba mengambil garpu kanan (G1) -> tidak bisa karena dipakai F1
F1 mencoba mengambil garpu kanan (G2) -> tidak bisa karena dipakai F2
F2 mencoba mengambil garpu kanan (G3) -> tidak bisa karena dipakai F3
F3 mencoba mengambil garpu kanan (G4) -> tidak bisa karena dipakai F4
F4 mencoba mengambil garpu kanan (G0) -> tidak bisa karena dipakai F0

Setiap filosof menunggu garpu kanan yang sedang dipegang filosof sebelahnya

Lingkaran Tunggu (Circular Wait)
F0 -> F1 -> F2 -> F3 -> F4 -> kembali ke F0
Tidak ada yang bisa lanjut

HASIL:
Tidak ada filosof yang dapat makan
Tidak ada filosof yang melepaskan garpu

```
- Identifikasi kapan dan mengapa deadlock terjadi.  

Deadlock terjadi pada saat semua filosof sudah memegang garpu kiri, kemudian mencoba mengambil garpu kanan secara bersamaan (bisa dilihat pada langkah 2 simulasi).
  Karena setiap filosof membutuhkan dua garpu, sementara tidak ada satu pun garpu kanan yang tersedia dan masing-masing sedang dipegang oleh filosof sebelahnya, akibatnya semua filosof berhenti dan saling menunggu satu sama lain, sehingga terjadilah deadlock.

**Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)**  
- Modifikasi pseudocode agar deadlock tidak terjadi.  

Pada versi ini digunakan mekanisme semaphore melalui aturan waiter, yaitu hanya 4 filosof yang diizinkan mulai mengambil garpu pada satu waktu. Mekanisme ini mencegah terbentuknya circular wait, sehingga deadlock tidak muncul  

```text
Semua filosof mulai: think()

Waiter Rule: 
Hanya 4 filosof yang boleh mengambil garpu dalam satu waktu
F0, F1, F2, F3 -> diizinkan oleh waiter
F4 -> belum diizinkan (menunggu)

Langkah 1:
F0 mengambil garpu kiri (G0)
F1 mengambil garpu kiri (G1)
F2 mengambil garpu kiri (G2)
F3 mengambil garpu kiri (G3)

Karena F4 belum boleh ambil garpu, masih ada satu garpu yang bebas (G4)

Langkah 2:
F0 mencoba ambil garpu kanan (G1) -> masih dipakai F1 -> menunggu
F1 mencoba ambil garpu kanan (G2) -> masih dipakai F2 -> menunggu
F2 mencoba ambil garpu kanan (G3) -> masih dipakai F3 -> menunggu
F3 mencoba ambil garpu kanan (G4) -> berhasil (G4 masih bebas)

F3 bisa makan

Langkah 3:
F3 selesai -> meletakkan garpu kiri dan kanan -> izin dikembalikan ke waiter
Waiter mengizinkan F4

F4 ambil garpu kiri (G4)
F4 ambil garpu kanan (G0) -> berhasil

F4 bisa makan

Setelah itu, proses berjalan bergantian
Tidak ada lingkaran tunggu (circular wait)
Tidak ada filosof yang saling menunggu terus-menerus

HASIL:
Tidak terjadi deadlock
Filosof bisa makan secara bergantian

```
- Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.

Pada simulasi hasil modifikasi diatas, deadlock tidak terjadi karena waiter membatasi maksimal 4 filosof yang boleh mengambil garpu secara bersamaa/dalam satu waktu. Pada awal simulasi, F0 sampai F3 langsung mendapat izin dan mengambil garpu kiri (G0–G3), sementara F4 menunggu, sehingga garpu G4 tetap bebas.

F0, F1, dan F2 menunggu garpu kanan karena masih dipakai filosof sampingnya, tetapi F3 berhasil mengambil garpu kanan (G4). Setelah F3 selesai, garpu dilepas dan izin diberikan ke F4, yang kemudian bisa mengambil garpu kiri (G4) dan kanan (G0). Filosof lain mendapat giliran setelah garpu dilepas.  

Dengan adanya garpu yang selalu bebas dan pengaturan izin waiter, tidak pernah muncul lingkaran tunggu, sehingga deadlock berhasil dihindari. Semua filosof bisa makan bergantian tanpa saling menunggu, membuktikan bahwa mekanisme semaphore (waiter) efektif untuk mencegah deadlock.

**Eksperimen 3 – Analisis Deadlock**

|Kondisi Deadlock|Terjadi di Versi Deadlock|Solusi di Versi Fixed|
|:---------------|:------------------------|:--------------------|
|Mutual Exclusion|Ya – setiap garpu hanya bisa dipegang satu filsuf pada satu waktu|Tetap menggunakan semaphore/lock untuk kontrol akses garpu agar eksklusif tetap terjaga|
|Hold and Wait|Ya – filsuf memegang garpu kiri sambil menunggu garpu kanan|Waiter/semaphore membatasi jumlah filsuf yang boleh mengambil garpu, sehingga tidak ada yang menahan lebih dari kapasitas|
|No Preemption|Ya – garpu tidak bisa diambil paksa dari filsuf lain|Tetap tidak ada preemption, tetapi deadlock dihindari karena waiter membatasi dan urutan pengambilan garpu|
|Circular Wait|Ya – F0 menunggu garpu F1, F1 menunggu F2, ..., F4 menunggu F0|Filsuf terakhir mengambil garpu secara terbalik, dan waiter membatasi filsuf makan → circular wait hilang|


---

## Kesimpulan

---

## Tugas
1. Analisis versi *Dining Philosophers* yang menyebabkan deadlock dan versi fixed yang bebas deadlock.  
2. Dokumentasikan hasil diskusi kelompok ke dalam `laporan.md`.  
3. Sertakan diagram atau screenshot hasil simulasi/pseudocode.  
4. Laporkan temuan penyebab deadlock dan solusi pencegahannya. 

## Quiz
1. Sebutkan empat kondisi utama penyebab deadlock.
   Empat kondisi utama penyebab deadlock:
   - Mutual Exclusion yaitu situsi dimana kapasitas hanya digunakan oleh satu sistem pada suatu waktu,sehingga tidak bisa dibagi bersama.
   - Hold and Wait yaitu situasi dimana sistem memegang satu kapasitas sambil menunggu kapasitas lain yang sedang dipegang oleh sistem lain.
   - NO Preemption yaitu situasi dimana kapaitas tidak dapat diambil paksa dari sistem yang sedang memakainya sampai proses tersebut selesai.
   - Circular Wait yaitu situasi dimana terdapat putaran sistem yang saling menunggu kapasitas yang dimiliki oleh sistem lain,membentuk lingkaran ketergantungan.  
2. Mengapa sinkronisasi diperlukan dalam sistem operasi?
   Sinkronisasi diperlukan dalam sistem operasi karena untuk mengatur berlangsungnya sebagian sistem yang berlangsung bersamaan dan bisa mengakses data secara bersamaan,jika tidak diatur dengan baik data bisa tidak konsisten atau malah bisa rusak.Sinkronisasi juga membantu menghindari dari masalah seperti deadlock dan starvation,sehingga semua proses bisa berlangsung lancar sesuai urutan yang benar  
3. Jelaskan perbedaan antara semaphore dan monitor.
   |Aspek|Semaphore|Monitor|
   |:----|:--------|:------|
   |Pengertian|Komponen yang digunakan untuk mengatur akses ke kapasitas bersama dengan angka(counting)|Struktur yang menggabungkan komponen, proses, dan pengendali akses agar aman digunakan bersama|
   |Cara kerja|Proses menggunakan wait() dan signal()|Akses dilakukan dengan prosedur dan monitor,manajemen antrian tunggu diatur dengan otomatis oleh sistem|
   |Jenis sinkronisasi|Sinkronisasi tingkat rendah|Sinkronisasi tingakt tinggi dengan penyederhanaan|
   |Kesulitan|Lebih rumit dan rawan kesalahan|Lebih dan aman|

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
