# Notasi Algoritma
# Algoritma RincianUangKembalian

# Kamus / Deklarasi
# besarBayar, totalBayar, kembalian: float
# lembarUang: dictionary
# jumlahLembar: integer

# Algoritma / Deskripsi
# input(besarBayar)
# input(totalBayar)

# kembalian <- besarBayar - totalBayar

# untuk setiap nominal, keterangan dalam lembarUang:
#     jumlahLembar <- kembalian // nominal
#     jika jumlahLembar lebih dari atau sama dengan 0:
#         kembalian <- kembalian - (jumlahLembar * nominal)
#         output(keterangan, jumlahLembar)

# Notasi Python
besarBayar = float(input("Masukkan besar uang yang dibayarkan: "))
totalBayar = float(input("Masukkan total yang harus dibayar: "))

kembalian = besarBayar - totalBayar

print(f"\nKembalian: Rp. {kembalian:.0f}\n")

print("Rincian uang kembalian:")

lembarUang = {
    50000: "Lembar Rp. 50.000",
    20000: "Lembar Rp. 20.000",
    10000: "Lembar Rp. 10.000",
    5000: "Lembar Rp. 5.000",
    2000: "Lembar Rp. 2.000",
    1000: "Lembar Rp. 1.000",
}

for nominal, keterangan in lembarUang.items():
    jumlahLembar = int(kembalian // nominal)
    if jumlahLembar >= 0:
        kembalian -= jumlahLembar * nominal
        print(f"{keterangan}: {jumlahLembar} lembar")

print("\n")

print("--- Created by: 10126905 - Ahmad Sani Jabarulloh ---")