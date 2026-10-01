# Program Hitung Jumlah Huruf Vokal

kata = str(input("Masukkan kata: "))
vokal = "aiueo"

hitungVokal = len([huruf for huruf in kata.lower() if huruf in vokal])

print(f"Jumlah huruf vokal dalam {kata} adalah {hitungVokal}")

print("\n")

print("--- Created by: 10126905 - Ahmad Sani Jabarulloh ---")
