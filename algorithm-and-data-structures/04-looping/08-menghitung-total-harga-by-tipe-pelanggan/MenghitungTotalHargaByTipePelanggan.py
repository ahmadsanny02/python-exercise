jenis_pelanggan = str(input("Jenis Pelanggan (Umum / Member / VIP Member): "))
total_belanja = float(input("Masukkan total belanja (Rp): "))

if jenis_pelanggan == "Umum":
    if total_belanja >= 500000 and total_belanja < 1000000:
        print(f"\nTotal harga awal Rp{total_belanja:,.0f}".replace(",", "."))

        besaranDiskon = 10
        print(f"Diskon sebesar: {besaranDiskon}%")

        diskon = total_belanja * (besaranDiskon / 100)
        total_belanja = total_belanja - diskon
        print(f"Total setelah diskon Rp{total_belanja:,.0f}".replace(",", "."))
    elif total_belanja >= 1000000:
        print(f"\nTotal harga awal Rp{total_belanja:,.0f}".replace(",", "."))

        besaranDiskon = 15
        print(f"Diskon sebesar: {besaranDiskon}%")

        diskon = total_belanja * (besaranDiskon / 100)
        total_belanja = total_belanja - diskon
        print(f"Total setelah diskon Rp{total_belanja:,.0f}".replace(",", "."))
    else:
        print(f"\nTotal harga awal Rp{total_belanja:,.0f}".replace(",", "."))

        besaranDiskon = 0
        print(f"Diskon sebesar: {besaranDiskon}%")

        diskon = total_belanja * (besaranDiskon / 100)
        total_belanja = total_belanja - diskon
        print(f"Total setelah diskon Rp{total_belanja:,.0f}".replace(",", "."))
elif jenis_pelanggan == "Member":
    if total_belanja >= 300000 and total_belanja < 700000:
        print(f"\nTotal harga awal Rp{total_belanja:,.0f}".replace(",", "."))

        besaranDiskon = 10
        print(f"Diskon sebesar: {besaranDiskon}%")

        diskon = total_belanja * (besaranDiskon / 100)
        total_belanja = total_belanja - diskon
        print(f"Total setelah diskon Rp{total_belanja:,.0f}".replace(",", "."))
    elif total_belanja >= 700000 and total_belanja < 1000000:
        print(f"\nTotal harga awal Rp{total_belanja:,.0f}".replace(",", "."))

        besaranDiskon = 20
        print(f"Diskon sebesar: {besaranDiskon}%")

        diskon = total_belanja * (besaranDiskon / 100)
        total_belanja = total_belanja - diskon
        print(f"Total setelah diskon Rp{total_belanja:,.0f}".replace(",", "."))
    elif total_belanja >= 1000000:
        print(f"\nTotal harga awal Rp{total_belanja:,.0f}".replace(",", "."))

        besaranDiskon = 30
        print(f"Diskon sebesar: {besaranDiskon}%")

        diskon = total_belanja * (besaranDiskon / 100)
        total_belanja = total_belanja - diskon
        print(f"Total setelah diskon Rp{total_belanja:,.0f}".replace(",", "."))
    else:
        print(f"\nTotal harga awal Rp{total_belanja:,.0f}".replace(",", "."))

        besaranDiskon = 0
        print(f"Diskon sebesar: {besaranDiskon}%")

        diskon = total_belanja * (besaranDiskon / 100)
        total_belanja = total_belanja - diskon
        print(f"Total setelah diskon Rp{total_belanja:,.0f}".replace(",", "."))
elif jenis_pelanggan == "VIP Member":
    if total_belanja >= 300000 and total_belanja < 500000:
        print(f"\nTotal harga awal Rp{total_belanja:,.0f}".replace(",", "."))

        besaranDiskon = 15
        print(f"Diskon sebesar: {besaranDiskon}%")

        diskon = total_belanja * (besaranDiskon / 100)
        total_belanja = total_belanja - diskon
        print(f"Total setelah diskon Rp{total_belanja:,.0f}".replace(",", "."))
    elif total_belanja >= 500000 and total_belanja < 1000000:
        print(f"\nTotal harga awal Rp{total_belanja:,.0f}".replace(",", "."))

        besaranDiskon = 25
        print(f"Diskon sebesar: {besaranDiskon}%")

        diskon = total_belanja * (besaranDiskon / 100)
        total_belanja = total_belanja - diskon
        print(f"Total setelah diskon Rp{total_belanja:,.0f}".replace(",", "."))
    elif total_belanja >= 1000000:
        print(f"\nTotal harga awal Rp{total_belanja:,.0f}".replace(",", "."))

        besaranDiskon = 35
        print(f"Diskon sebesar: {besaranDiskon}%")

        diskon = total_belanja * (besaranDiskon / 100)
        total_belanja = total_belanja - diskon
        print(f"Total setelah diskon Rp{total_belanja:,.0f}".replace(",", "."))
    else:
        print(f"\nTotal harga awal Rp{total_belanja:,.0f}".replace(",", "."))

        besaranDiskon = 0
        print(f"Diskon sebesar: {besaranDiskon}%")

        diskon = total_belanja * (besaranDiskon / 100)
        total_belanja = total_belanja - diskon
        print(f"Total setelah diskon Rp{total_belanja:,.0f}".replace(",", "."))
else:
    print("Jenis pelanggan tidak valid!")