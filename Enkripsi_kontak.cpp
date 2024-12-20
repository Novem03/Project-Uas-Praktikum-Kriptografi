#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

// Fungsi untuk menghitung kunci berdasarkan nama kontak
int calculateKey(const string& name) {
    int key = 0;
    for (char c : name) {
        key += static_cast<int>(c); // Jumlahkan nilai ASCII setiap karakter
    }
    return key % 10; // Modulus 10 untuk menghasilkan kunci 0-9
}

// Fungsi untuk mengenkripsi nomor telepon
string encryptNumber(const string& number, int key) {
    string encryptedNumber = "";
    for (char c : number) {
        if (isdigit(c)) { // Hanya enkripsi digit
            char encryptedDigit = ((c - '0') + key) % 10 + '0'; // Shift digit
            encryptedNumber += encryptedDigit;
        } else {
            encryptedNumber += c; // Tambahkan karakter lain apa adanya
        }
    }
    return encryptedNumber;
}

// Fungsi untuk menghasilkan representasi segitiga
vector<string> generateTriangle(const string& encryptedNumber) {
    vector<string> triangle;
    for (size_t i = 1; i <= encryptedNumber.length(); ++i) {
        triangle.push_back(encryptedNumber.substr(0, i));
    }
    return triangle;
}

int main() {
    ofstream outFile("encrypted_contacts.txt", ios::app); // Buka file dalam mode append
    if (!outFile) {
        cerr << "Gagal membuka file untuk menyimpan data.\n";
        return 1;
    }

    string name, number;

    while (true) {
        cout << "\n=== Input Kontak ===\n";
        cout << "Masukkan Nama Kontak (atau ketik 'EXIT' untuk keluar): ";
        getline(cin, name);

        if (name == "EXIT") {
            cout << "Keluar dari aplikasi input.\n";
            break;
        }

        cout << "Masukkan Nomor Telepon: ";
        getline(cin, number);

        int key = calculateKey(name); // Hitung kunci berdasarkan nama
        string encryptedNumber = encryptNumber(number, key); // Enkripsi nomor

        // Hasilkan segitiga dari enkripsi
        vector<string> triangle = generateTriangle(encryptedNumber);

        // Tampilkan hasil segitiga
        cout << "\nHasil Enkripsi dalam Bentuk Segitiga:\n";
        for (const string& row : triangle) {
            cout << row << "\n";
        }

        // Simpan nama, nomor asli, dan segitiga enkripsi ke file
        outFile << name << "," << number << "\n";
        for (const string& row : triangle) {
            outFile << row << "\n";
        }
        outFile << "---\n"; // Separator antar kontak
        cout << "Data berhasil disimpan.\n";
    }

    outFile.close();
    return 0;
}
