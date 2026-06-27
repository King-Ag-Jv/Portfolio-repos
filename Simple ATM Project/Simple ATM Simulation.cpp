#include <iostream>
using namespace std;

int main() {
    
    // Buat variabel:
    // Saldo Awal
    string mataUang = "Rp.";
    int saldo = 15000000;
    double tarikSaldo_Mentah, setorSaldo_Mentah = 0; 
    int tarikSaldo, setorSaldo = 0;
    
    // Riwayat Transaksi:
    int Riwayat1, Riwayat2, Riwayat3, Riwayat4, Riwayat5 = 0;
    int perubahanSaldo1, perubahanSaldo2, perubahanSaldo3, perubahanSaldo4, perubahanSaldo5 = 0;
    
    //menu
    double pilihanMenuMentah = 0;
    int pilihanMenu, pilihanMenuSebelumnya = 0;
    int i = 0;
    int keluaranRiwayat;
    
    // Untuk variabel LoopCount
    int loopCount = 0;
    
    bool mulaiProgram = true;
    while (mulaiProgram){
        
        keluaranRiwayat = i % 6;
        if (pilihanMenu == 4 && i > 0){
            pilihanMenu = pilihanMenuSebelumnya; // Buat nilai sistemnya biar ga jadi 4, pasti ngertilah 😅
        }
        else {
            if (i >= 0 && i <= 5){
                if (keluaranRiwayat == 1){
                Riwayat1 = pilihanMenu;
                perubahanSaldo1 = saldo;
            }
            else if (keluaranRiwayat == 2){
                Riwayat2 = pilihanMenu;
                perubahanSaldo2 = saldo;
            }
            else if (keluaranRiwayat == 3){
                Riwayat3 = pilihanMenu;
                perubahanSaldo3 = saldo;
            }
            else if (keluaranRiwayat == 4){
                Riwayat4 = pilihanMenu;
                perubahanSaldo4 = saldo;
            }
            else {
                    Riwayat5 = pilihanMenu;
                    perubahanSaldo5 = saldo;
            }
            }
            else {
                    Riwayat1 = Riwayat2;
                    Riwayat2 = Riwayat3;
                    Riwayat3 = Riwayat4;
                    Riwayat4 = Riwayat5;
                    perubahanSaldo1 = perubahanSaldo2;
                    perubahanSaldo2 = perubahanSaldo3;
                    perubahanSaldo3 = perubahanSaldo4;
                    perubahanSaldo4 = perubahanSaldo5;
                    
                    Riwayat5 = pilihanMenu;
                    perubahanSaldo5 = saldo;
            }
        }
        
        // Menu ATM
        if (i == 0){
            cout << "=== MENU ATM ==="
                << "\n1. Cek Saldo"
                << "\n2. Tarik Saldo"
                << "\n3. Setor Saldo"
                << "\n4. Keluar"
                << "\nPilih Menu: ";
        }
        else {
            cout << "=== MENU ATM ==="
             << "\n1. Cek Saldo"
             << "\n2. Tarik Saldo"
             << "\n3. Setor Saldo"
             << "\n4. Lihat Riwayat"
             << "\n5. Keluar"
             << "\nPilih Menu: ";
        }
        
        cin >> pilihanMenuMentah;
        pilihanMenu = (int)pilihanMenuMentah;
        
        if (pilihanMenuMentah - pilihanMenu > 0 && pilihanMenuMentah - pilihanMenu < 1) {
            cout << "\nMasukan Menu Tidak Diperbolehkan Menggunakan Nilai Desimal!\n\n";
            pilihanMenu = 0;
            pilihanMenuMentah = 0;
        }
        else{
            
        
            if (pilihanMenu == 1){
                cout << "Saldo Anda Saat Ini Adalah: Rp."
                     << saldo
                     << "\n\n";
                pilihanMenuSebelumnya = pilihanMenu;
                i++;
                loopCount++;
            }
            else if (pilihanMenu == 2){
                
                if (saldo == 0) {
                    cout << "Mohon Maaf, Saldo Anda Telah Habis!"
                         << "\nProses Penarikan Saldo Tidak Berhasil."
                         << endl;
                } 
                else {
                    cout << "Masukkan Jumlah Saldo Yang Ingin Anda Tarik\n(Jika Tidak Ingin Tarik Ketik '0'):\n";
                    while (true)
                    {
                        cout << ">>> ";
                        cin >> tarikSaldo_Mentah;
                        tarikSaldo = (int)tarikSaldo_Mentah;
                        
                        if (tarikSaldo == 0){
                            break;
                        }
                        else if (tarikSaldo > 0 && tarikSaldo <= saldo) {
                            if (tarikSaldo_Mentah - tarikSaldo > 0 && tarikSaldo_Mentah - tarikSaldo < 1) {
                                cout << "Nilai Tarik Saldo Harus Asli Dan Tidak Menyertai Nilai Desimal!" << endl;
                            }
                            else {
                                if (tarikSaldo % 100 == 0){
                                    saldo = saldo - tarikSaldo;
                                cout << "Saldo Anda Saat Ini Adalah: "
                                << mataUang
                                << saldo
                                << endl;
                                i++;
                                pilihanMenuSebelumnya = pilihanMenu;
                                break;
                                }
                                else {
                                    cout << "Proses Penarikan Saldo Dibatalkan. Mohon Masukkan Nilai Tarik Saldo Dengan Kelipatan 100!"
                                        << "\nContoh:"
                                        << "\nBenar: 1100, 50300"
                                        << "\nSalah: 400020, 6009"
                                        << endl;
                                }
                            }
                        }
                        else {
                            cout << "Masukan Penarikan Saldo Anda Tidak Valid. Mohon Untuk Mengecek Saldo Anda Terlebih Dahulu!"
                                << endl;
                        }
                    }
                }
                cout << endl;
                loopCount++;
            }
            else if (pilihanMenu == 3) {
                cout << "Masukkan Jumlah Saldo Yang Ingin Anda Setorkan\n(Ketik '0' Jika Tidak Ingin Menyetor):\n";
                while (true) {
                    cout << ">>> ";
                    cin >> setorSaldo_Mentah;
                    setorSaldo = (int)setorSaldo_Mentah;
                    if (setorSaldo < 0) {
                        cout << "Nilai Setor Tidak Valid, Mohon Ulangi Lagi!" << endl;
                    }
                    else if (setorSaldo == 0){
                        break;
                    }
                    else {
                        if (setorSaldo_Mentah - setorSaldo > 0 && setorSaldo_Mentah - setorSaldo < 1) {
                            cout << "Nilai Setor Saldo Harus Real Dan Tidak Menerima Nilai Desimal!" << endl;
                        }
                        else {
                            
                        
                            if (setorSaldo % 100 == 0) {
                                saldo = saldo + setorSaldo;
                                cout << "Saldo Anda Saat Ini Adalah: "
                                    << mataUang
                                    << saldo
                                    << endl;
                                pilihanMenuSebelumnya = pilihanMenu;
                                i++;
                                break;
                            }
                            else {
                                cout << "Proses Penyetoran Saldo Dibatalkan. Mohon Masukkan Nilai Setor Saldo Dengan Kelipatan 100!"
                                        << "\nContoh:"
                                        << "\nBenar: 1100, 50300"
                                        << "\nSalah: 400020, 6009"
                                        << endl;
                            }
                        }
                    }
                }
                cout << endl;
                loopCount++;
            }
            else if (pilihanMenu == 4 && i > 0){
                cout << "\nRiwayat Anda:" << endl;
                for (int j = 1; j <= i; j++){
                    cout << j << ". ";
                    if (j == 1){
                        if (Riwayat1 == 1){
                            cout << "Cek Saldo";
                        }
                        else if (Riwayat1 == 2) {
                            cout << "Tarik Saldo";
                        }
                        else {
                            cout << "Setor Saldo";
                        }
                        cout << " : " << mataUang << perubahanSaldo1 << endl;
                    }
                    else if (j == 2){
                        if (Riwayat2 == 1){
                            cout << "Cek Saldo";
                        }
                        else if (Riwayat2 == 2) {
                            cout << "Tarik Saldo";
                        }
                        else {
                            cout << "Setor Saldo";
                        }
                        cout << " : " << mataUang << perubahanSaldo2 << endl;
                    }
                    else if (j == 3) {
                        if (Riwayat3 == 1){
                            cout << "Cek Saldo";
                        }
                        else if (Riwayat3 == 2) {
                            cout << "Tarik Saldo";
                        }
                        else {
                            cout << "Setor Saldo";
                        }
                        cout << " : " << mataUang << perubahanSaldo3 << endl;
                    }
                    else if (j == 4) {
                        if (Riwayat4 == 1){
                            cout << "Cek Saldo";
                        }
                        else if (Riwayat4 == 2) {
                            cout << "Tarik Saldo";
                        }
                        else {
                            cout << "Setor Saldo";
                        }
                        cout << " : " << mataUang << perubahanSaldo4 << endl;
                    }
                    else if (j == 5) {
                        if (Riwayat5 == 1){
                            cout << "Cek Saldo";
                        }
                        else if (Riwayat5 == 2) {
                            cout << "Tarik Saldo";
                        }
                        else {
                            cout << "Setor Saldo";
                        }
                        cout << " : " << mataUang << perubahanSaldo5 << endl;
                        break;
                    }
                }
                cout << endl;
                loopCount++;
            }
            else if ((pilihanMenu == 4) || (pilihanMenu == 5 && i > 0)) {
                cout << "\nTerima Kasih Telah Mengunjungi Bank ATM Kami!" << endl;
                if (i == 0){
                    cout << "Tidak Ada Riwayat Tercatat." << endl;
                }
                else {
                    cout << "\nRiwayat Anda:";
                for (int j = 1; j <= i; j++){
                    cout << "\n" << j << ". ";
                    if (j == 1){
                        if (Riwayat1 == 1){
                            cout << "Cek Saldo";
                        }
                        else if (Riwayat1 == 2) {
                            cout << "Tarik Saldo";
                        }
                        else {
                            cout << "Setor Saldo";
                        }
                        cout << " : " << mataUang << perubahanSaldo1;
                    }
                    else if (j == 2){
                        if (Riwayat2 == 1){
                            cout << "Cek Saldo";
                        }
                        else if (Riwayat2 == 2) {
                            cout << "Tarik Saldo";
                        }
                        else {
                            cout << "Setor Saldo";
                        }
                        cout << " : "<< mataUang << perubahanSaldo2;
                    }
                    else if (j == 3) {
                        if (Riwayat3 == 1){
                            cout << "Cek Saldo";
                        }
                        else if (Riwayat3 == 2) {
                            cout << "Tarik Saldo";
                        }
                        else {
                            cout << "Setor Saldo";
                        }
                        cout << " : "<< mataUang << perubahanSaldo3;
                    }
                    else if (j == 4) {
                        if (Riwayat4 == 1){
                            cout << "Cek Saldo";
                        }
                        else if (Riwayat4 == 2) {
                            cout << "Tarik Saldo";
                        }
                        else {
                            cout << "Setor Saldo";
                        }
                        cout << " : " << mataUang << perubahanSaldo4;
                    }
                    else if (j == 5) {
                        if (Riwayat5 == 1){
                            cout << "Cek Saldo";
                        }
                        else if (Riwayat5 == 2) {
                            cout << "Tarik Saldo";
                        }
                        else {
                            cout << "Setor Saldo";
                        }
                        cout << " : " << mataUang << perubahanSaldo5;
                        break;
                    }
                }
                cout << endl;
                }
                
                cout << "\nTotal Transaksi: " << i << endl;
                cout << "Kode Transaksi: ";
                if (i == 0){
                    string PK_ = "TRX000";
                    cout << PK_
                         << endl;
                }
                else {
                    if (loopCount > 0 && loopCount < 10) {
                        string PK1 = "TRX00";
                        cout << PK1 << loopCount;
                    } else if (loopCount >= 10 && loopCount < 100) {
                        string PK2 = "TRX0";
                        cout << PK2 << loopCount;
                    } else if (loopCount >= 100 && loopCount < 1000) {
                        string PK3 = "TRX";
                        cout << PK3 << loopCount;
                }
                cout << endl;
                }
                
                cout << "Tanggal Melakukan Transaksi: ";
                cout << __DATE__;
                mulaiProgram = false;
            }
            else {
                cout << "\nMohon Masukkan Menu Dengan Angka Pada Daftar Menu Diatas!\n\n";
            }
        }
    }
}
