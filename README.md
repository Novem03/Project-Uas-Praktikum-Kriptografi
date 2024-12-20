
# README: Enkripsi Kontak Rahasia dengan Segitiga

<!-- Anggota Tim -->
## Anggota Tim
| NPM           | Name                              |
| ------------- |-----------------------------------|
| 140810220069  | Rais Abiyyu Putra                 |
| 140810220083  | Novem Romadhofi kika              |

## Deskripsi Proyek

Aplikasi ini adalah sistem pengelolaan kontak rahasia berbasis web menggunakan Streamlit. Aplikasi ini memungkinkan Anda menyimpan, mencari, dan menghapus kontak dengan enkripsi berbentuk segitiga.

---

## Fitur Utama

1. **Tambah Kontak**: Menyimpan nama dan nomor telepon yang dienkripsi dengan metode shift cipher.
2. **Cari Kontak**: Mencari kontak berdasarkan kode enkripsi berbentuk segitiga.
3. **Hapus Kontak**: Menghapus kontak berdasarkan nama yang diberikan.

---

## Cara Kerja

1. **Enkripsi Kontak**:
   - Setiap nomor telepon dienkripsi menggunakan shift cipher berdasarkan urutan alfabet dari nama kontak.
   - Hasil enkripsi ditampilkan dalam format segitiga, misalnya:
     ```
     1
     12
     123
     1234
     12345
     ```

2. **Tambah Kontak**:
   - Input nama dan nomor telepon.
   - Data disimpan ke file `encrypted_contacts.txt` dalam format:
     ```
     Nama,Nomor
     Kode Segitiga
     ---
     ```
   - File tambahan `encrypted_triangle_<Nama>.txt` dibuat untuk unduhan.

3. **Cari Kontak**:
   - Masukkan kode enkripsi berbentuk segitiga.
   - Sistem mencocokkan dengan data di file `encrypted_contacts.txt` dan menampilkan hasilnya jika ditemukan.

4. **Hapus Kontak**:
   - Masukkan nama kontak.
   - Kontak dihapus dari file `encrypted_contacts.txt` jika ditemukan.

---

## Menjalankan Aplikasi

1. Instal Streamlit jika belum terinstal:
   ```bash
   pip install streamlit
   ```
2. Jalankan aplikasi dengan perintah:
   ```bash
   streamlit run app.py
   ```
3. Akses aplikasi melalui browser di alamat yang ditampilkan (biasanya `http://localhost:8501`).

