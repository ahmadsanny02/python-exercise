# --- Notasi Algoritma ---
# Algoritma ProgramDurasiTayangan

# Kamus / Deklarasi
# durasiFilmSatu, durasiFilmDua, durasiFilmTiga: float
# totalDurasi: float
# jam, menit: float

# Algoritma / Deskripsi
# input(durasiFilmSatu)
# input(durasiFilmDua)
# input(durasiFilmTiga)

# totalDurasi <- durasiFilmSatu + durasiFilmDua + durasiFilmTiga

# jam <- totalDurasi di bagi 60
# menit <- totalDurasi di mod 60

# output("Total durasi tayangan film adalah: ", jam, " jam ", menit, " menit")

# --- Notasi Python ---
durasiFilmSatu = float(input("Masukkan durasi film pertama (dalam menit): "))
durasiFilmDua = float(input("Masukkan durasi film kedua (dalam menit): "))
durasiFilmTiga = float(input("Masukkan durasi film ketiga (dalam menit): "))

totalDurasi = durasiFilmSatu + durasiFilmDua + durasiFilmTiga

jam = totalDurasi // 60
menit = totalDurasi % 60

print(f"Total durasi tayangan film adalah: {jam:.0f} jam {menit:.0f} menit")

print("\n")

print("--- Created by: 10126905 - Ahmad Sani Jabarulloh ---")