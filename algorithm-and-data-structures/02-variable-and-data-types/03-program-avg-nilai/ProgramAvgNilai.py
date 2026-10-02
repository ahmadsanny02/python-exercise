# --- Notasi Algoritma ---
# Algoritma HitungRataRataNilai

# Kamus / Deklarasi
# mapelMatematika, mapelFisika, mapelKimia: float
# rataRata: float

# Algoritma / Deskripsi
# mapelMatematika <- 75.80
# mapelFisika <- 80.50
# mapelKimia <- 70.25
# rataRata <- (mapelMatematika + mapelFisika + mapelKimia) / 3
# output(rataRata)

# --- Notasi Python ---
mapelMatematika = float(input("Masukkan nilai mata pelajaran matematika: "))
mapelFisika = float(input("Masukkan nilai mata pelajaran fisika: "))
mapelKimia = float(input("Masukkan nilai mata pelajaran kimia: "))

rataRata = (mapelMatematika + mapelFisika + mapelKimia) / 3

print(f"Nilai rata-rata Anda adalah: {rataRata:.2f}")

print("\n")

print("--- Created by: 10126905 - Ahmad Sani Jabarulloh ---")