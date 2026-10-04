totalHari = int(input("Masukkan total hari: "))

tahun = totalHari // 365
sisaTahun = totalHari % 365

bulan = sisaTahun // 30
hari = sisaTahun % 30

print(f"{tahun} tahun, {bulan} bulan, {hari} hari")

print("\n")

print("--- Created by: 10126905 - Ahmad Sani Jabarulloh ---")