
# README: Enkripsi Kontak Rahasia dengan Segitiga

<!-- Anggota Tim -->
## Anggota Tim
| NPM           | Name                              |
| ------------- |-----------------------------------|
| 140810220069  | Rais Abiyyu Putra                 |
| 140810220083  | Novem Romadhofi kika              |

## Deskripsi Proyek
Proyek ini terdiri dari dua aplikasi yang saling terhubung untuk mengelola kontak rahasia menggunakan enkripsi. Enkripsi dilakukan dengan mengubah nomor telepon menjadi kode berbentuk segitiga. Berikut adalah alur kerja dua aplikasi yang digunakan:

1. **Aplikasi Input Kontak (`input_contact.cpp`)**
   - Bertugas untuk memasukkan nama dan nomor telepon.
   - Mengenkripsi nomor telepon dengan metode Shift Cipher berdasarkan nama kontak.
   - Menyimpan data nama, nomor asli, dan kode enkripsi berbentuk segitiga ke dalam file `encrypted_contacts.txt`.

2. **Aplikasi Pencarian Kontak (`decrypt_display.cpp`)**
   - Meminta input kode enkripsi dalam bentuk segitiga.
   - Mencari kecocokan kode enkripsi segitiga di file `encrypted_contacts.txt`.
   - Jika ditemukan, menampilkan nama dan nomor telepon asli.

---

## Alur Kerja Program

### **1. Input Kontak (`input_contact.cpp`):**
#### Langkah-langkah:
1. **Masukkan Nama dan Nomor Telepon:**
   - Pengguna diminta untuk memasukkan nama kontak dan nomor telepon.
2. **Proses Enkripsi:**
   - Nomor telepon dienkripsi menggunakan algoritma Shift Cipher dengan kunci yang dihitung dari nama kontak.
   - Hasil enkripsi ditampilkan dalam bentuk segitiga.
3. **Simpan Data:**
   - Data nama, nomor telepon asli, dan kode enkripsi segitiga disimpan ke file `encrypted_contacts.txt` dengan format berikut:
     ```
     Nama,Nomor Asli
     Enkripsi Baris 1
     Enkripsi Baris 2
     ...
     ---
     ```

### **2. Pencarian Kontak (`decrypt_display.cpp`):**
#### Langkah-langkah:
1. **Masukkan Kode Enkripsi Segitiga:**
   - Pengguna diminta memasukkan kode enkripsi dalam bentuk segitiga.
   - Untuk mengakhiri input segitiga, pengguna harus mengetikkan `---`.
2. **Cocokkan Data:**
   - Program membaca file `encrypted_contacts.txt` dan membandingkan input dengan kode enkripsi segitiga yang disimpan.
3. **Tampilkan Hasil:**
   - Jika ditemukan, nama dan nomor telepon asli ditampilkan.
   - Jika tidak ditemukan, program memberikan pesan bahwa kontak tidak ada.

---

## Catatan Penting
- **Format Input Segitiga:** Saat memasukkan kode enkripsi segitiga, pastikan formatnya benar dan akhiri dengan `---` untuk menandakan akhir input.
- **File Data:**
  - Pastikan file `encrypted_contacts.txt` berada di direktori yang sama dengan aplikasi.
  - Jangan menghapus atau mengubah isi file secara manual untuk menghindari kesalahan pencocokan data.

---

## Anggota
- Nama: Rais Abiyyu Putra  
  NPM: 140810220069
- Nama: Novem Romadhofi Kika  
  NPM: 140810220083

---

Dikembangkan untuk memenuhi tugas mata kuliah Kriptografi. Jika ada pertanyaan, hubungi pengembang. 😊

