import streamlit as st
import os

# Fungsi Enkripsi shift cipher
def shift_cipher_encrypt(name, number):
    key = sum((ord(c.upper()) - ord('A')) for c in name if c.isalpha()) % 26
    encrypted = ''.join(chr((ord(ch) - ord('0') + key) % 10 + ord('0')) for ch in number)
    triangle = "\n".join([encrypted[:i] for i in range(1, len(encrypted) + 1)])
    return triangle

# Fungsi untuk Menambahkan Kontak
def add_contact(name, number):
    encrypted = shift_cipher_encrypt(name, number)
    with open("encrypted_contacts.txt", "a") as file:
        file.write(f"{name},{number}\n{encrypted}\n---\n")
    file_name = f"encrypted_triangle_{name}.txt"
    with open(file_name, "w") as file:
        file.write(f"Kode Enkripsi untuk {name}:\n\n{encrypted}")
    return file_name

# Fungsi untuk Menghapus Kontak
def delete_contact(name):
    if not os.path.exists("encrypted_contacts.txt"):
        return False
    deleted = False
    new_data = []
    with open("encrypted_contacts.txt", "r") as file:
        entries = file.read().split("---\n")
        for entry in entries:
            if entry.strip():
                current_name = entry.split("\n")[0].split(",")[0]
                if current_name != name:
                    new_data.append(entry.strip())
                else:
                    deleted = True
    if deleted:
        with open("encrypted_contacts.txt", "w") as file:
            file.write("\n---\n".join(new_data) + "\n---\n")
    return deleted

# Fungsi untuk Mencari Kontak
def search_contact(input_triangle):
    if not os.path.exists("encrypted_contacts.txt"):
        return None
    with open("encrypted_contacts.txt", "r") as file:
        entries = file.read().split("---\n")
        for entry in entries:
            if entry.strip():
                name, number = entry.split("\n")[0].split(",")
                encrypted_triangle = "\n".join(entry.split("\n")[1:])
                if input_triangle == encrypted_triangle.strip():
                    return name, number
    return None

# -------------------------
# Gaya Tampilan (CSS)
# -------------------------
st.markdown("""
    <style>
    body {
        background-color: #f8f9fa;
        color: #212529;
        font-family: 'Arial', sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #f1f3f5;
    }
    .stButton>button {
        background-color: #6c757d;
        color: white;
        border-radius: 8px;
        padding: 8px 16px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #495057;
        color: white;
    }
    .stTextInput>div>input {
        border-radius: 8px;
        border: 1px solid #ced4da;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------
# Aplikasi Streamlit
# -------------------------
st.title("📒 Enkripsi Kontak Rahasia")
st.write("""
**Sistem Pengelolaan Kontak Rahasia**  
Amankan kontak Anda dengan metode enkripsi berbentuk segitiga!  
""")

menu = st.sidebar.radio("Navigasi Menu", ["Tambah Kontak", "Cari Kontak", "Hapus Kontak"], index=0)

if menu == "Tambah Kontak":
    st.header("➕ Tambah Kontak Baru")
    name = st.text_input("Nama Kontak", placeholder="Masukkan nama kontak")
    number = st.text_input("Nomor Telepon", max_chars=15, placeholder="Masukkan nomor telepon")
    if st.button("Simpan Kontak"):
        if name and number.isdigit():
            file_name = add_contact(name, number)
            st.success("✅ Kontak berhasil disimpan!")
            with open(file_name, "rb") as f:
                st.download_button("📥 Unduh Kode Enkripsi", data=f, file_name=file_name, mime="text/plain")
        else:
            st.error("⚠️ Harap masukkan nama dan nomor telepon yang valid.")

elif menu == "Cari Kontak":
    st.header("🔍 Cari Kontak")
    input_triangle = st.text_area("Masukkan Kode Enkripsi (Segitiga)", placeholder="Input kode enkripsi")
    if st.button("Cari"):
        result = search_contact(input_triangle.strip())
        if result:
            name, number = result
            st.success(f"✅ Kontak ditemukan: **{name}** - **{number}**")
        else:
            st.error("❌ Kontak tidak ditemukan.")

elif menu == "Hapus Kontak":
    st.header("🗑️ Hapus Kontak")
    name = st.text_input("Nama Kontak yang Ingin Dihapus", placeholder="Masukkan nama kontak")
    if st.button("Hapus Kontak"):
        if delete_contact(name):
            st.success("✅ Kontak berhasil dihapus!")
        else:
            st.error("❌ Gagal menghapus kontak. Pastikan nama kontak benar.")
