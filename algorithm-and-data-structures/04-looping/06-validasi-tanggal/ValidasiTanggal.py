tanggal = int(input("Masukkan tanggal: "))
bulan = int(input("Masukkan bulan: "))
tahun = int(input("Masukkan tahun: "))
bulan_panjang = [1, 3, 5, 7, 8, 10, 12]
bulan_pendek = [2, 4, 6, 9, 11]
jumlah_hari = 0
validitas = True

if bulan in bulan_panjang:
    jumlah_hari = 31
    print(f"Jumlah hari = {jumlah_hari}")
elif bulan in bulan_pendek and bulan != 2:
    jumlah_hari = 30
    print(f"Jumlah hari = {jumlah_hari}")
elif bulan == 2:
    if tahun % 4 == 0 and tahun % 100 != 0 or tahun % 400 == 0:
        jumlah_hari = 29
        print(f"Jumlah hari = {jumlah_hari}")
    else:
        jumlah_hari = 28
        print(f"Jumlah hari = {jumlah_hari}")
else:
    validitas = False
    
if tanggal >= 1 and tanggal <= jumlah_hari and bulan >= 1 and bulan <= 12:
    validitas = True
else:
    validitas = False
    
if validitas:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah tanggal valid")
else:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah bukan tanggal valid")
