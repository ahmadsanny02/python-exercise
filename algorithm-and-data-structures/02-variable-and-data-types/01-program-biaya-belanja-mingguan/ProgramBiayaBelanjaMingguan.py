# --- Notasi Algoritma ---
# Algoritma hitung_biaya_belanja_mingguan

# Kamus / Deklarasi
# hargaBarangSatu, hargaBarangDua, hargaBarangTiga: float
# jumlahBarangSatu, jumlahBarangDua, jumlahBarangTiga: int
# totalBiayaBelanjaMingguan: float

# Algoritma / Deskripsi
# hargaBarangSatu ← 15000
# jumlahBarangSatu ← 2
# hargaBarangDua ← 20000
# jumlahBarangDua ← 1
# hargaBarangTiga ← 10000
# jumlahBarangTiga ← 3
# output (totalBiayaBelanjaMingguan ← (hargaBarangSatu * jumlahBarangSatu) + (hargaBarangDua * jumlahBarangDua) + (hargaBarangTiga * jumlahBarangTiga))

# --- Notasi Python ---
hargaBarangSatu = float(input("Masukkan harga barang pertama: "))
jumlahBarangSatu = int(input("Masukkan jumlah barang pertama: "))

hargaBarangDua = float(input("Masukkan harga barang kedua: "))
jumlahBarangDua = int(input("Masukkan jumlah barang kedua: "))

hargaBarangTiga = float(input("Masukkan harga barang ketiga: "))
jumlahBarangTiga = int(input("Masukkan jumlah barang ketiga: "))

totalBiayaBelanjaMingguan = (hargaBarangSatu * jumlahBarangSatu) + (hargaBarangDua * jumlahBarangDua) + (hargaBarangTiga * jumlahBarangTiga)

print(f"Total biaya belanja mingguan adalah: Rp{totalBiayaBelanjaMingguan:.0f}")

print("\n")

print("--- Created by: 10126905 - Ahmad Sani Jabarulloh ---")