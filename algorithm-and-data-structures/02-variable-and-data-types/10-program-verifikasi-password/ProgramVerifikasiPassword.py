# Notasi Algoritma
# Algoritma ProgramVerifikasiPassword

# Kamus / Deklarasi
# password : string

# Algoritma / Deskripsi
# input(password)
# jika panjang(password) kurang dari 8 maka
#     tampilkan "Password Anda lemah"
# jika tidak maka
#     tampilkan "Password Anda kuat"

# --- Notasi Python ---
password = str(input("Masukkan password: "))

if len(password) < 8:
    print("Password Anda lemah")
else:
    print("Password Anda kuat")

print("\n")

print("--- Created by: 10126905 - Ahmad Sani Jabarulloh ---")