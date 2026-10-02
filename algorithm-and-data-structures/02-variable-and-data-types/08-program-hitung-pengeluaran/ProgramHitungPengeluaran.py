# --- Notasi Algoritma ---
# Algoritma HitungPersentasePengeluaran

# Kamus / Deklarasi
# makanan, transportasi, hiburan, pendidikan, total_pengeluaran, jumlah: float
# kategori: string
# persentase: float
# pengeluaran: dictionary

# Algoritma / Deskripsi
# input(makanan)
# input(transportasi)
# input(hiburan)
# input(pendidikan)
#
# pengeluaran <- {"Makanan": makanan, "Transportasi": transportasi, "Hiburan": hiburan, "Pendidikan": pendidikan}
#
# total_pengeluaran <- sum(pengeluaran.values)
#
# output("--- Rincian Pengeluaran ---")
# output("Total pengeluaran: Rp" + total_pengeluaran)
#
# Untuk setiap kategori, jumlah di dalam pengeluaran.items() lakukan:
#     persentase <- (jumlah / total_pengeluaran) * 100
#     output(kategori + ": Rp" + jumlah + " (" + persentase + "%)")


# --- Notasi Python ---
makanan = float(input("Masukkan pengeluaran untuk Makanan: "))
transportasi = float(input("Masukkan pengeluaran untuk Transportasi: "))
hiburan = float(input("Masukkan pengeluaran untuk Hiburan: "))
pendidikan = float(input("Masukkan pengeluaran untuk Pendidikan: "))

pengeluaran = {
    "Makanan": makanan,
    "Transportasi": transportasi,
    "Hiburan": hiburan,
    "Pendidikan": pendidikan,
}

total_pengeluaran = sum(pengeluaran.values())

print("\n--- Rincian Pengeluaran ---")

print(f"Total pengeluaran: Rp{total_pengeluaran:.0f}\n")

print("Persentase pengeluaran per kategori:")
for kategori, jumlah in pengeluaran.items():
    persentase = (jumlah / total_pengeluaran) * 100
    print(f"{kategori}: Rp{jumlah:.0f} ({persentase:.2f}%)")

print("\n")

print("--- Created by: 10126905 - Ahmad Sani Jabarulloh ---")