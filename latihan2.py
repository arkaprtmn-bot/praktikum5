# Inisialisasi Dictionary global
data_mahasiswa = {}

def hitung_nilai_akhir(tugas, uts, uas):
    """Menghitung Nilai Akhir: Tugas(30%), UTS(35%), UAS(35%)"""
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

def tambah_data():
    print("\n--- Tambah Data Mahasiswa ---")
    nama = input("Masukkan Nama Mahasiswa: ").strip()
    if nama in data_mahasiswa:
        print(f"ERROR: Data untuk '{nama}' sudah ada!")
        return
    
    try:
        tugas = float(input("Nilai Tugas (0-100): "))
        uts = float(input("Nilai UTS (0-100): "))
        uas = float(input("Nilai UAS (0-100): "))
    except ValueError:
        print("ERROR: Input nilai harus berupa angka.")
        return

    na = hitung_nilai_akhir(tugas, uts, uas)
    
    data_mahasiswa[nama] = {
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": round(na, 2)
    }
    print(f"SUKSES: Data '{nama}' berhasil ditambahkan.")

def ubah_data():
    print("\n--- Ubah Data Mahasiswa ---")
    nama = input("Masukkan Nama Mahasiswa yang akan diubah: ").strip()
    
    if nama not in data_mahasiswa:
        print(f"ERROR: Data untuk '{nama}' tidak ditemukan.")
        return
        
    print(f"Data saat ini untuk {nama}: {data_mahasiswa[nama]}")
    
    try:
        tugas = float(input("Masukkan Nilai Tugas baru (kosongkan jika tidak diubah): ") or data_mahasiswa[nama]['tugas'])
        uts = float(input("Masukkan Nilai UTS baru (kosongkan jika tidak diubah): ") or data_mahasiswa[nama]['uts'])
        uas = float(input("Masukkan Nilai UAS baru (kosongkan jika tidak diubah): ") or data_mahasiswa[nama]['uas'])
    except ValueError:
        print("ERROR: Input nilai harus berupa angka.")
        return

    na = hitung_nilai_akhir(tugas, uts, uas)
    
    # Update Dictionary
    data_mahasiswa[nama]['tugas'] = tugas
    data_mahasiswa[nama]['uts'] = uts
    data_mahasiswa[nama]['uas'] = uas
    data_mahasiswa[nama]['nilai_akhir'] = round(na, 2)
    
    print(f"SUKSES: Data '{nama}' berhasil diubah. Nilai Akhir baru: {data_mahasiswa[nama]['nilai_akhir']}")


def hapus_data():
    print("\n--- Hapus Data Mahasiswa ---")
    nama = input("Masukkan Nama Mahasiswa yang akan dihapus: ").strip()
    
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"SUKSES: Data '{nama}' berhasil dihapus.")
    else:
        print(f"ERROR: Data untuk '{nama}' tidak ditemukan.")

def tampilkan_data():
    print("\n--- Daftar Nilai Mahasiswa ---")
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
        return

    # Header Tabel
    print("-" * 55)
    print(f"| {'NAMA':<15} | {'TUGAS':<6} | {'UTS':<5} | {'UAS':<5} | {'N. AKHIR':<8} |")
    print("-" * 55)
    
    for nama, nilai in data_mahasiswa.items():
        print(f"| {nama:<15} | {nilai['tugas']:<6.0f} | {nilai['uts']:<5.0f} | {nilai['uas']:<5.0f} | {nilai['nilai_akhir']:<8.2f} |")
    
    print("-" * 55)

def cari_data():
    print("\n--- Cari Data Mahasiswa ---")
    nama = input("Masukkan Nama Mahasiswa yang dicari: ").strip()
    
    if nama in data_mahasiswa:
        data = data_mahasiswa[nama]
        print(f"\nData Ditemukan untuk {nama}:")
        print(f"  - Tugas: {data['tugas']}")
        print(f"  - UTS: {data['uts']}")
        print(f"  - UAS: {data['uas']}")
        print(f"  - Nilai Akhir: {data['nilai_akhir']}")
    else:
        print(f"ERROR: Data untuk '{nama}' tidak ditemukan.")

def tampilkan_menu():
    """Menampilkan menu utama program."""
    print("\n==============================")
    print(" PROGRAM PENGOLAH NILAI MAHASISWA")
    print("==============================")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data (Semua)")
    print("5. Cari Data")
    print("6. Keluar")
    print("------------------------------")
    pilihan = input("Pilih menu (1-6): ")
    return pilihan

# Main Loop Program
def main():
    while True:
        pilihan = tampilkan_menu()
        
        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            ubah_data()
        elif pilihan == '3':
            hapus_data()
        elif pilihan == '4':
            tampilkan_data()
        elif pilihan == '5':
            cari_data()
        elif pilihan == '6':
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()