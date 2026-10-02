# --- Notasi Algoritma ---
# Algoritma ProgramGajiBersihKaryawan

# Kamus / Deklarasi
# namaKaryawan: string
# gajiPokok: float
# tunjangan: float
# pajak: float
# gajiBersih: float

# Algoritma / Deskripsi
# namaKaryawan <- "John Doe"
# gajiPokok <- 5000000.0
# tunjangan <- 20/100 * gajiPokok
# pajak <- 15/100 * (gajiPokok + tunjangan)
# gajiBersih <- (gajiPokok + tunjangan) - pajak
# output("--- Informasi Gaji Karyawan ---")
# output(namaKaryawan)
# output(gajiBersih)

# --- Notasi Python ---
namaKaryawan = str(input("Masukkan nama karyawan: "))
gajiPokok = float(input("Masukkan gaji pokok: "))

tunjangan = 20/100 * gajiPokok
pajak = 15/100 * (gajiPokok + tunjangan)

gajiBersih = (gajiPokok + tunjangan) - pajak

print(f"\n--- Informasi Gaji Karyawan ---")
print(f"Nama Karyawan: {namaKaryawan}")
print(f"Gaji Bersih: {gajiBersih}")

print("\n")

print("--- Created by: 10126905 - Ahmad Sani Jabarulloh ---")