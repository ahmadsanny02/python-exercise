saldo_awal = float(input("Masukkan saldo awal: "))
bunga = int(input("Masukkan jumlah bunga: "))
jangka_waktu = int(input("Masukkan jangka waktu: "))


for i in range(1, jangka_waktu + 1):
    saldo_awal = saldo_awal + ((bunga / 100) * saldo_awal)

    print(f"Saldo akhir bulan ke - {i}: Rp{saldo_awal:,.0f}")