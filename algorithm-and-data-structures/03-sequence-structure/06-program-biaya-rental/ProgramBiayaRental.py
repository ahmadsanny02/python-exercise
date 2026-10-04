# Notasi ALgoritma
# Algoritma BiayaRental

# Kamus / Deklarasi
# jamMasuk, menitMasuk, jamKeluar, menitKeluar : integer
# waktuMasuk, waktuKeluar, waktuRental : integer
# jam, menit : integer
# biayaRental : integer

# Algoritma / Deskripsi
# input(jhamMasuk)
# input(menitMasuk)
# input(jamKeluar)
# input(menitKeluar)

# waktuMasuk <- (jamMasuk * 60) + menitMasuk
# waktuKeluar <- (jamKeluar * 60) + menitKeluar

# waktuRental <- waktuKeluar - waktuMasuk

# jam <- waktuRental // 60
# menit <- waktuRental % 60

# biayaRental <- jam * 5000

# output("Lama rental: ", waktuRental, " menit (", jam, " jam ", menit, " menit)")
# output("Biaya rental: Rp. ", biayaRental)

# Notasi Python
jamMasuk = int(input("Masukkan jam masuk: "))
menitMasuk = int(input("Masukkan menit masuk: "))

jamKeluar = int(input("Masukkan jam keluar: "))
menitKeluar = int(input("Masukkan menit keluar: "))

waktuMasuk = (jamMasuk * 60) + menitMasuk
waktuKeluar = (jamKeluar * 60) + menitKeluar

waktuRental = waktuKeluar - waktuMasuk

jam = waktuRental // 60
menit = waktuRental % 60

biayaRental = jam * 5000

print("\n")

print(f"Lama rental: {waktuRental} menit ({jam} jam {menit} menit)")
print(f"Biaya rental: Rp. {biayaRental}")

print("\n")

print("--- Created by: 10126905 - Ahmad Sani Jabarulloh ---")