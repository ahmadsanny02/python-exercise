# --- Notasi Algoritma ---
# Algortima HitungKomisiSalesman

# Kamus / Deklarasi
# namaSalesman : string
# nilaiPenjualan : float
# komisi : float

# Algoritma / Deskripsi
# namaSalesman ← "John Doe"
# nilaiPenjualan ← 5000000
# komisi ← nilaiPenjualan * 1.05
# output (namaSalesman)
# output (komisi)

# --- Notasi Python ---
namaSalesman = str(input("Masukkan nama Salesman: "))
nilaiPenjualan = float(input("Masukkan nilai penjualan: "))

komisi = nilaiPenjualan * 1.05

print(f"Nama Salesman: {namaSalesman}")
print(f"Komisi: Rp{komisi:.0f}")

print("\n")

print("--- Created by: 10126905 - Ahmad Sani Jabarulloh ---")