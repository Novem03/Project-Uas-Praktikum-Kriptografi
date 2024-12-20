#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

// Fungsi untuk membaca segitiga enkripsi dari input
vector<string> readTriangleInput() {
    vector<string> triangle;
    cout << "Masukkan Enkripsi Segitiga (Ketik '---' untuk selesai):\n";
    string line;
    while (true) {
        getline(cin, line);
        if (line == "---") break;
        triangle.push_back(line);
    }
    return triangle;
}

// Fungsi untuk membaca kontak dari file
bool findContactByTriangle(const vector<string>& inputTriangle) {
    ifstream inFile("encrypted_contacts.txt");
    if (!inFile) {
        cerr << "Gagal membuka file untuk membaca data.\n";
        return false;
    }

    string line;
    while (getline(inFile, line)) {
        string name = line.substr(0, line.find(',')); // Ambil nama
        string number = line.substr(line.find(',') + 1); // Ambil nomor telepon

        // Baca segitiga enkripsi dari file
        vector<string> fileTriangle;
        while (getline(inFile, line) && line != "---") {
            fileTriangle.push_back(line);
        }

        // Cocokkan segitiga input dengan segitiga dari file
        if (fileTriangle == inputTriangle) {
            cout << "\nKontak Ditemukan!\n";
            cout << "Nama: " << name << "\n";
            cout << "Nomor Telepon: " << number << "\n";
            inFile.close();
            return true;
        }
    }

    inFile.close();
    return false;
}

int main() {
    while (true) {
        cout << "\n=== Cari Kontak Berdasarkan Enkripsi Segitiga ===\n";
        vector<string> inputTriangle = readTriangleInput();

        if (inputTriangle.empty()) {
            cout << "Input segitiga kosong. Keluar dari aplikasi.\n";
            break;
        }

        if (!findContactByTriangle(inputTriangle)) {
            cout << "Tidak ada kontak dengan kode enkripsi segitiga tersebut.\n";
        }
    }

    return 0;
}
