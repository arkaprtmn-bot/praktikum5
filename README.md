# praktikum5
# Program Pengolah Nilai Mahasiswa

## Tujuan
Program ini dibuat untuk mengelola daftar nilai mahasiswa menggunakan struktur data **Dictionary** dalam bahasa pemrograman Python. Program ini mengimplementasikan fungsi dasar Create, Read, Update, Delete (CRUD) melalui menu interaktif.

## Ketentuan Utama
1.  **Struktur Data:** Menggunakan **Dictionary** di mana **Nama Mahasiswa** adalah **kunci (key)** dan **nilai-nilai komponen** (Tugas, UTS, UAS, Nilai Akhir) disimpan sebagai **nilai (value)** dalam bentuk dictionary bertingkat.
2.  **Menu Pilihan:** Program menyediakan menu untuk:
    * Tambah Data
    * Ubah Data
    * Hapus Data
    * Tampilkan Data
    * Cari Data
3.  **Perhitungan Nilai Akhir (NA):**
    Nilai Akhir dihitung berdasarkan bobot:
    $$\text{NA} = (\text{Tugas} \times 30\%) + (\text{UTS} \times 35\%) + (\text{UAS} \times 35\%)$$

## Flowchart Program

**Penjelasan Flowchart:**
1.  **Start:** Program dimulai.
2.  **Inisialisasi Dictionary:** Membuat Dictionary kosong (`data_mahasiswa`) untuk menyimpan data.
3.  **Tampilkan Menu:** Menampilkan opsi menu (Tambah, Ubah, Hapus, Tampilkan, Cari, Keluar).
4.  **Input Pilihan:** Meminta input dari pengguna.
5.  **Proses (Decision):** Program mengeksekusi fungsi yang sesuai berdasarkan pilihan:
    * **Tambah Data:** Mengambil input nama dan nilai, menghitung NA, dan menambahkannya ke dictionary.
    * **Ubah Data:** Mencari data, mengambil input nilai baru, menghitung ulang NA, dan memperbarui dictionary.
    * **Hapus Data:** Mencari data, dan menghapusnya dari dictionary.
    * **Tampilkan/Cari Data:** Menampilkan semua data atau data spesifik.
6.  **Loop:** Setelah selesai, program kembali menampilkan menu (kecuali jika memilih **Keluar**).
7.  **End:** Program berhenti.
