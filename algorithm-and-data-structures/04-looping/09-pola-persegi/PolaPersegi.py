input_angka = int(input("Masukkan persegi: "))


persegi = [[0 for _ in range(input_angka)] for _ in range(input_angka)]

for i in range(len(persegi)):
    for j in range(len(persegi)):
        if persegi[i] == persegi[j]:
            persegi[i] = " X "
            print(persegi[i], end="")
        else:
            print(" 0 ", end="")
    print()