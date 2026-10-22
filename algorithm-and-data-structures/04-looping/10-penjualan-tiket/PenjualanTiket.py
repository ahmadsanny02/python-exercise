print("""=== Menu ===
1. Pesan Tiket
2. Keluar
""")

denah = [[0 for _ in range(20)] for _ in range(10)]

pendapatan = 0
pesan_tiket = True

print(f"Pendapatan awal: Rp{pendapatan:,}")

while pesan_tiket:
    pilih_menu = int(input("\nPilih menu (1 / 2): "))

    if pilih_menu == 1:
        input_baris = int(input("\nNomor baris (1 - 10): "))
        input_kursi = int(input("Nomor kursi (1 - 20): "))

        if input_baris < 1 or input_baris > 10 or input_kursi < 1 or input_kursi > 20:
            print("Pilih antara baris 1 - 10 dan kursi antara 1 - 20")
            continue

        nomor_baris = input_baris - 1
        nomor_kursi = input_kursi - 1

        print("\n")

        if denah[nomor_baris][nomor_kursi] == "X":
            print(f"Kursi nomor {nomor_kursi} pada baris {nomor_baris} sudah di isi!")
        else:
            if 1 <= input_baris <= 5:
                harga_tiket = 50000
            else:
                harga_tiket = 40000

            pendapatan += harga_tiket

            denah[nomor_baris][nomor_kursi] = "X"
            print(f"Tiket berhasil dipesan. Harga Rp{harga_tiket:,}")

            print("\nSusunan:")

            for i in range(10):
                for j in range(20):
                    if denah[i][j] == "X":
                        print(" X ", end="")
                    else:
                        print(" 0 ", end="")
                print()

            print(f"\nTotal pendapatan: Rp{pendapatan:,}")
    elif pilih_menu == 2:
        pesan_tiket = False
        print("\nTerima kasih telah menggunakan sistem")
    else:
        print("Pilih 1 atau 2")