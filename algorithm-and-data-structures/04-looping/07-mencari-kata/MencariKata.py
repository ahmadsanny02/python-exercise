teks_buku = [
    "Python adalah bahasa pemrograman yang sangat populer.",
    "Banyak orang menggunakan Python untuk data science.",
    "Python juga digunakan untuk pengembangan web dan otomatisasi.",
    "Pemrograman dengan Python memungkinkan pembuatan aplikasi dengan cepat."]

masukan_kata = str(input("Masukkan kata: "))

gabungan_kata = " ".join(teks_buku).lower().replace(".", "").split()

result = gabungan_kata.count(masukan_kata.lower())
print(result)
