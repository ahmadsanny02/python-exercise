# Notasi Algoritma
# Algoritma LuasSelimutDanVolumeBalok

# Kamus / Deklarasi
# panjang, lebar, tinggi : float
# luasSelimut, volumeBalok, dimensiBalok : float

# Algoritma / Deskripsi
# input(panjang)
# input(lebar)
# input(tinggi)

# luasSelimut <- (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)

# volumeBalok <- panjang * lebar * tinggi

# dimensiBalok <- panjang + " x " + lebar + " x " + tinggi

# output(luasSelimut)
# output(volumeBalok)
# output(dimensiBalok)

# Notasi Python
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
tinggi = float(input("Masukkan tinggi: "))

luasSelimut = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)

volumeBalok = panjang * lebar * tinggi

print("\n")

dimensiBalok = f"{panjang} x {lebar} x {tinggi}"

print(f"Luas Selimut Balok: {luasSelimut} \n")
print(f"Volume Balok: {volumeBalok} \n")
print(f"Dimensi Balok: {dimensiBalok}")

print("\n")

print("--- Created by: 10126905 - Ahmad Sani Jabarulloh ---")