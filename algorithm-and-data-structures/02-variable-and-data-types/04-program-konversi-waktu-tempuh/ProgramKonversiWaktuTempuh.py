# --- Notasi Algoritma ---
# Algoritma KonversiWaktuTempuh

# Kamus / Deklarasi
# jamTempuh, menitTempuh, detikTempuh: integer
# totalDetik: integer

# Algoritma / Deskripsi
# jamTempuh <-- 2
# menitTempuh <-- 10
# detikTempuh <-- 50
# totalDetik <-- (jamTempuh * 3600) + (menitTempuh * 60) + detikTempuh
# output(totalDetik)

# --- Notasi Python ---
jamTempuh = int(input("Masukkan waktu tempuh (dalam jam): "))
menitTempuh = int(input("Masukkan waktu tempuh (dalam menit): "))
detikTempuh = int(input("Masukkan waktu tempuh (dalam detik): "))

totalDetik = (jamTempuh * 3600) + (menitTempuh * 60) + detikTempuh
print(f"Total waktu tempuh dalam detik adalah: {totalDetik} detik")

print("\n")

print("--- Created by: 10126905 - Ahmad Sani Jabarulloh ---")