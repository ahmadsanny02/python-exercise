from datetime import date

# Program Hitung Usia dari Tahun Lahir

currentYear = date.today().year

tahunLahir = int(input("Masukkan tahun lahir Anda: "))

usia = currentYear - tahunLahir

print(f"Usia Anda adalah {usia} tahun")

print("\n")

print("--- Created by: 10126905 - Ahmad Sani Jabarulloh ---")
