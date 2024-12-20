
# README: Enkripsi Kontak Rahasia dengan Segitiga

<!-- Anggota Tim -->
## Anggota Tim
| NPM           | Name                              |
| ------------- |-----------------------------------|
| 140810220069  | Rais Abiyyu Putra                 |
| 140810220083  | Novem Romadhofi kika              |
| 140810220062  | Drias Ameliano Kevin David        |

## Deskripsi Proyek

Aplikasi ini adalah sistem pengelolaan kontak rahasia berbasis web menggunakan Streamlit. Dengan aplikasi ini, Anda dapat menyimpan, mencari, dan menghapus kontak dengan metode enkripsi khusus untuk menjaga kerahasiaan data.

---

## Fitur Utama

1. **Tambah Kontak**:
   - Menyimpan nama dan nomor telepon dengan enkripsi berbasis shift cipher.
   - Data enkripsi ditampilkan dalam format segitiga untuk keamanan tambahan.
2. **Cari Kontak**:
   - Memungkinkan pencarian kontak berdasarkan kode enkripsi segitiga.
   - Menampilkan nama dan nomor telepon jika data cocok.
3. **Hapus Kontak**:
   - Menghapus kontak yang dipilih berdasarkan nama dari penyimpanan sistem.

---

## Cara Kerja

### 1. **Enkripsi Kontak**
- Nomor telepon dienkripsi dengan metode **shift cipher**, di mana setiap digit angka digeser berdasarkan nilai alfabet dari nama kontak.
- Hasil enkripsi disusun dalam format segitiga. Contoh:
  ```
  1
  12
  123
  1234
  12345
  ```
  Format ini menambahkan lapisan keamanan karena mempersulit interpretasi data langsung.

### 2. **Tambah Kontak**
- Pengguna memasukkan nama dan nomor telepon melalui antarmuka aplikasi.
- Sistem:
  1. Mengenkripsi nomor telepon.
  2. Menyimpan data ke file `encrypted_contacts.txt` dalam format:
     ```
     Nama,Nomor
     Kode Segitiga
     ---
     ```
  3. Membuat file `encrypted_triangle_<Nama>.txt` sebagai berkas unduhan untuk setiap kontak.

### 3. **Cari Kontak**
- Pengguna memasukkan kode segitiga hasil enkripsi.
- Sistem membaca file `encrypted_contacts.txt` dan mencocokkan kode segitiga dengan data yang tersimpan.
- Jika ditemukan, sistem menampilkan nama dan nomor telepon kontak tersebut.

### 4. **Hapus Kontak**
- Pengguna memasukkan nama kontak yang ingin dihapus.
- Sistem:
  1. Membaca file `encrypted_contacts.txt`.
  2. Mencari nama yang cocok dan menghapus data terkait.
  3. Menyimpan kembali data yang tersisa ke file.

---

## Menjalankan Aplikasi

1. **Persiapan Lingkungan**:
   - Pastikan Python telah terinstal di sistem Anda.
   - Instal Streamlit dengan perintah:
     ```bash
     pip install streamlit
     ```

2. **Menjalankan Aplikasi**:
   - Gunakan perintah berikut untuk menjalankan aplikasi:
     ```bash
     streamlit run app.py
     ```
   - Akses aplikasi melalui browser pada alamat yang ditampilkan (biasanya `http://localhost:8501`).

3. **Penggunaan Aplikasi**:
   - Navigasi melalui menu di sidebar untuk memilih fitur Tambah Kontak, Cari Kontak, atau Hapus Kontak.
   - Ikuti petunjuk di layar untuk setiap fitur.

---


