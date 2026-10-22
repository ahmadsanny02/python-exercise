print("""Menu
0. Setor tunai
1. Tarik tunai
2. Keluar
""")

SALDO_MINIMUM = 10000
saldo = 100000
proses = True

print(f"\nSaldo saat ini: Rp{saldo:,.0f}")

while proses:

    kode = int(input("\nPilih menu (0 / 1 / 2): "))

    if kode >= 0 and kode <= 1:
        jumlah_uang = float(input("Masukkan jumlah uang: "))

        while jumlah_uang <= 0:
            print("\nSetor / tarik tunai harus lebih dari 0 rupiah")
            jumlah_uang = float(input("Masukkan jumlah uang: "))


        if kode == 0:
            saldo += jumlah_uang

            print(f"\nSetor tunai sebesar Rp{jumlah_uang} berhasil dilakukan.")

            print(f"Total saldo: Rp{saldo:,.0f}")
        elif kode == 1:
            if saldo <= SALDO_MINIMUM or jumlah_uang >= saldo:
                print("Tarik tunai gagal dilakukan. Saldo tidak mencukupi!")
            else:
                saldo -= jumlah_uang

                print(f"\nTarik tunai sebesar Rp{jumlah_uang:,.0f} berhasil dilakukan.")

                print(f"Total saldo: Rp{saldo:,.0f}")
    elif kode == 2:
        proses = False

        print("Terima kasih")
    else:
        print("Menu tidak valid!")