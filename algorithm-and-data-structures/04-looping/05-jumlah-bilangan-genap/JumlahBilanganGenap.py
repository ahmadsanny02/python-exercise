batas_atas = int(input("Masukkan batas atas: "))
total = 0
deret = []

for i in range(1, batas_atas + 1):
    if i % 2 == 0:
        total += i
        deret.append(str(i))
        print(total)
print(f"Total jumlah bilangan genap dari 1 sampai {batas_atas} adalah {total}")
print(f"{" + ".join(deret)}")
