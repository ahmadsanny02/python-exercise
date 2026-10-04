totalDetik = int(input("Masukkan total detik: "))

hari = totalDetik // 86400
sisaHari = totalDetik % 86400

jam = sisaHari // 3600
sisaJam = sisaHari % 3600

menit = sisaJam // 60
detik = sisaJam % 60

print(f"{hari} hari, {jam} jam, {menit} menit, {detik} detik")

print("\n")

print("--- Created by: 10126905 - Ahmad Sani Jabarulloh ---")