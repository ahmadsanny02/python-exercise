total = 0

lagi = "Y"

while lagi == "Y":
    input_angka = int(input("Masukkan angka: "))

    total += input_angka
    print(f"Total sekarang: {total}")

    lagi = str(input("\nLagi? "))