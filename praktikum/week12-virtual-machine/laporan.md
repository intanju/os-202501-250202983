
# Laporan Praktikum Minggu 12
Topik: Virtualisasi Menggunakan Virtual Machine

---

## Identitas
- **Nama**  : 
  - Sukmani Intan Jumala (250202983)
  - Novia Safitri (250202923)
  - Putri Amaliya Ramadani (250202924)
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).
2. Membuat dan menjalankan sistem operasi guest di dalam VM.
3. Mengatur konfigurasi resource VM (CPU, RAM, storage).
4. Menjelaskan mekanisme proteksi OS melalui virtualisasi.
5. Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.

---

## Dasar Teori
1. Virtualisasi Sistem Operasi  
   Virtualisasi adalah teknologi yang memungkinkan satu komputer fisik menjalankan beberapa sistem operasi secara bersamaan dengan memanfaatkan pembagian sumber daya perangkat keras.  
2. Host OS dan Guest OS  
   Host OS dan Guest OS adalah dua jenis sistem operasi dalam virtualisasi, di mana host OS berfungsi mengelola perangkat keras secara langsung, sedangkan guest OS berjalan di dalam mesin virtual dan menggunakan resource dari host OS.  
3. Hypervisor  
   Hypervisor merupakan perangkat lunak yang berperan mengatur dan mengelola mesin virtual serta membagi sumber daya seperti CPU dan RAM agar setiap sistem dapat berjalan dengan aman dan stabil.  
4. Isolasi Sistem  
   Isolasi sistem adalah konsep dalam virtualisasi yang membuat setiap mesin virtual berjalan secara terpisah, sehingga gangguan atau masalah pada satu sistem tidak langsung memengaruhi sistem lainnya maupun sistem utama.

---

## Langkah Praktikum
1. **Instalasi Virtual Machine**
   - Instal VirtualBox atau VMware pada komputer host.  
   - Pastikan fitur virtualisasi (VT-x / AMD-V) aktif di BIOS.

2. **Pembuatan OS Guest**
   - Buat VM baru dan pilih OS guest (misal: Ubuntu Linux).  
   - Atur resource awal:
     - CPU: 1–2 core  
     - RAM: 2–4 GB  
     - Storage: ≥ 20 GB

3. **Instalasi Sistem Operasi**
   - Jalankan proses instalasi OS guest sampai selesai.  
   - Pastikan OS guest dapat login dan berjalan normal.

4. **Konfigurasi Resource**
   - Ubah konfigurasi CPU dan RAM.  
   - Amati perbedaan performa sebelum dan sesudah perubahan resource.

5. **Analisis Proteksi OS**
   - Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.  
   - Kaitkan dengan konsep *sandboxing* dan *hardening* OS.

6. **Dokumentasi**
   - Ambil screenshot setiap tahap penting.  
   - Simpan di folder `screenshots/`.

7. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 12 - Virtual Machine"
   git push origin main
   ```

---

## Hasil Eksekusi  
Dokumentasi Proses Instalasi Virtual Machine
![Screenshot hasil](screenshots/instalasi_vm.png)  

Dokumentasi Proses Konfigurasi Resource
![Screenshot hasil](screenshots/konfigurasi_resource.png)   

OS guest running  
![Screenshot hasil](screenshots/os_guest_running.png)  

Perbedaan performa sebelum dan sesudah perubahan resource
![Screenshot hasil](screenshots/perbedaan_performa.png)  

---

## Analisis  
- Bagaimana VM menyediakan isolasi antara host dan guest?
  
  Pada penggunaan Virtual Machine, sistem operasi guest dijalankan di lingkungan software yang terpisah dari sistem utama pada hardware komputer. Guest OS tidak berinteraksi langsung dengan hardware fisik karena seluruh akses resource seperti CPU, RAM, dan storage diatur oleh software virtualisasi. Dengan mekanisme ini, aktivitas yang terjadi di dalam guest OS tidak memengaruhi sistem utama. Jika terjadi kesalahan sistem atau crash pada guest OS, hardware dan sistem utama tetap berjalan normal dan aman.
- Kaitkan dengan konsep *sandboxing* dan *hardening* OS
  
  Isolasi pada Virtual Machine mencerminkan konsep *sandboxing*, yaitu menjalankan sistem atau proses dalam lingkungan terbatas. Guest OS berfungsi sebagai ruang uji coba. Jadi, pada saat error, crash, atau kesalahan saat instalasi, dampaknya hanya ada di Virtual Machine dan tidak berdampak pada sistem utama maupun hardware fisik.  
  Virtual Machine mendukung *hardening* OS karena guest OS dapat digunakan untuk mencoba pengaturan sistem (konfigurasi) dan keamanan terlebih dulu. Semua percobaan bisa dilakukan tanpa takut merusak sistem utama, sehingga sistem bisa dibuat lebih aman sebelum digunakan secara nyata.
- Perbedaan performa sebelum dan sesudah perubahan resource
  
  **Konfigurasi Awal**  
CPU: 1 core  
RAM: 2 GB  
Storage: 25 GB  
Dengan konfigurasi ini, pemakaian CPU cenderung tinggi walaupun hanya menjalankan proses dasar. Sistem terasa lambat, terutama saat membuka aplikasi dan berpindah menu. Penggunaan RAM juga cukup besar jika dibandingkan dengan kapasitas yang tersedia, sehingga kinerja sistem menjadi kurang optimal.  

  **Konfigurasi Setelah Diubah**  
CPU: 2 core   
RAM: 3 GB    
Storage: 30 GB  
Setelah resource ditambah, performa guest OS menjadi lebih baik. Beban CPU terbagi ke dua core sehingga sistem bekerja lebih stabil. Penambahan RAM membantu proses berjalan lebih lancar dan mengurangi jeda saat membuka aplikasi. Secara keseluruhan, sistem terasa lebih responsif dengan pemanfaatan resource yang lebih seimbang.  
 

---

## Kesimpulan
Pada praktikum Virtual Machine dapat kami simpulkan bahwa:   
1. Virtualisasi memungkinkan menjalankan sistem operasi guest di dalam satu komputer tanpa mengganggu sistem utama karena guest OS berjalan di lingkungan terpisah meskipun menggunakan hardware yang sama.
2. Pengaturan resource seperti CPU, RAM, dan storage sangat memengaruhi performa guest OS, di mana konfigurasi yang tepat membuat sistem lebih stabil dan responsif, serta membantu kami memahami manajemen resource pada VM.
3. Virtual Machine meningkatkan keamanan sistem melalui isolasi, sandboxing, dan hardening OS, sehingga guest OS dapat digunakan sebagai lingkungan uji coba tanpa merusak host OS.  

---

## Quiz
1. Apa perbedaan antara host OS dan guest OS?  
   Host OS adalah sistem operasi utama yang terpasang langsung pada komputer dan memiliki kontrol penuh terhadap perangkat keras. Sedangkan guest OS adalah sistem operasi yang dijalankan di dalam mesin virtual menggunakan software virtualisasi dan hanya menggunakan resource yang dialokasikan oleh host OS. Perbedaan utamanya, host OS mengelola hardware secara langsung, sementara guest OS berjalan secara terisolasi di atas host OS tanpa mengganggu sistem utama.  
2. Apa peran hypervisor dalam virtualisasi?  
   Hypervisor berperan sebagai pengelola utama dalam teknologi virtualisasi yang bertugas membuat, menjalankan, dan mengatur mesin virtual (Virtual Machine). Hypervisor membagi serta mengalokasikan sumber daya perangkat keras seperti CPU, RAM, dan storage kepada setiap VM agar dapat berjalan secara bersamaan tanpa saling mengganggu, sehingga sistem host tetap stabil dan aman.  
3. Mengapa virtualisasi meningkatkan keamanan sistem?  
   Virtualisasi dapat meningkatkan keamanan sistem karena setiap sistem operasi dijalankan dalam lingkungan yang terpisah. terjadi error, crash, atau serangan malware pada sistem operasi guest, dampaknya tidak langsung memengaruhi sistem utama (host). Dengan adanya isolasi ini, pengguna dapat melakukan pengujian atau menjalankan aplikasi berisiko dengan lebih aman tanpa mengganggu kestabilan dan keamanan sistem secara keseluruhan.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
