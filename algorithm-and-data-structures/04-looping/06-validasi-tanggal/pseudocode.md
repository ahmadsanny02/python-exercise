# Algoritma dan Pseudocode - Program Validasi Tanggal Kalender

## 1. Deskripsi Program
Program ini memvalidasi keabsahan kombinasi tanggal, bulan, dan tahun. Program menentukan batas hari maksimum untuk bulan bersangkutan (31 untuk bulan ganjil/panjang, 30 untuk bulan pendek, dan 28/29 untuk Februari tergantung status tahun kabisat), lalu mengecek apakah tanggal berada dalam batas yang valid.

- **File Program**: [`ValidasiTanggal.py`](./ValidasiTanggal.py)
- **Direktori**: `06-validasi-tanggal`

---

## 2. Analisis Masalah
- **Input**:
  - Menggunakan nilai awal/parameter yang didefinisikan dalam kode.
- **Proses**:
  - Validasi kondisi perulangan dan percabangan logika sesuai spesifikasi program.
  - Perhitungan matematika / manipulasi data / akumulasi nilai.
- **Output**:
  - Menampilkan hasil pengolahan, status operasi, rincian iterasi, atau representasi visual.

---

## 3. Kamus Data / Deklarasi Variabel
| Nama Variabel | Tipe Data | Keterangan |
| :--- | :--- | :--- |
| `tanggal` | integer | Nilai tanggal yang divalidasi |
| `bulan` | integer | Nilai bulan yang divalidasi (1 - 12) |
| `tahun` | integer | Nilai tahun yang divalidasi |
| `bulan_panjang` | array of integer | Daftar bulan dengan 31 hari [1, 3, 5, 7, 8, 10, 12] |
| `bulan_pendek` | array of integer | Daftar bulan dengan 30 hari [2, 4, 6, 9, 11] |
| `jumlah_hari` | integer | Maksimum hari pada bulan tertentu |
| `validitas` | boolean | Status keabsahan tanggal (True jika valid, False jika tidak valid) |

---

## 4. Algoritma (Pseudocode)

```pseudocode
ALGORITMA ValidasiTanggal
DEKLARASI:
    tanggal, bulan, tahun : integer
    bulan_panjang, bulan_pendek : array of integer
    jumlah_hari : integer
    validitas : boolean

DESKRIPSI:
    bulan <- 2
    tahun <- 2000
    tanggal <- 30
    bulan_panjang <- [1, 3, 5, 7, 8, 10, 12]
    bulan_pendek <- [2, 4, 6, 9, 11]
    jumlah_hari <- 0
    validitas <- TRUE

    IF bulan IN bulan_panjang THEN
        jumlah_hari <- 31
        OUTPUT "Jumlah hari = ", jumlah_hari
    ELSE IF bulan IN bulan_pendek AND bulan != 2 THEN
        jumlah_hari <- 30
        OUTPUT "Jumlah hari = ", jumlah_hari
    ELSE IF bulan == 2 THEN
        IF (tahun MOD 4 == 0 AND tahun MOD 100 != 0) OR (tahun MOD 400 == 0) THEN
            jumlah_hari <- 29
            OUTPUT "Jumlah hari = ", jumlah_hari
        ELSE
            jumlah_hari <- 28
            OUTPUT "Jumlah hari = ", jumlah_hari
        ENDIF
    ELSE
        validitas <- FALSE
    ENDIF

    IF (tanggal >= 1 AND tanggal <= jumlah_hari) AND (bulan >= 1 AND bulan <= 12) THEN
        validitas <- TRUE
    ELSE
        validitas <- FALSE
    ENDIF

    IF validitas == TRUE THEN
        OUTPUT "Tanggal ", tanggal, "/", bulan, "/", tahun, " adalah tanggal valid"
    ELSE
        OUTPUT "Tanggal ", tanggal, "/", bulan, "/", tahun, " adalah bukan tanggal valid"
    ENDIF

    SELESAI
```

---

## 5. Flowchart

Berikut adalah diagram alir (*flowchart*) dari algoritma di atas:

![Flowchart](flowchart.png)

> File diagram tersedia dalam format **PNG** ([`flowchart.png`](./flowchart.png)) dan **JPG** ([`flowchart.jpg`](./flowchart.jpg)).

---

## 6. Penjelasan Alur Eksekusi (Traceability)
1. Program dimulai (Start) dan menginisialisasi parameter tanggal (tanggal=30, bulan=2, tahun=2000) beserta daftar kategori bulan.
2. Pengecekan penentuan batas `jumlah_hari`:
3. - Jika `bulan in bulan_panjang`: `jumlah_hari = 31`.
4. - Jika `bulan in bulan_pendek` dan `bulan != 2`: `jumlah_hari = 30`.
5. - Jika `bulan == 2`: cek aturan tahun kabisat. Jika kabisat `jumlah_hari = 29`, jika bukan `jumlah_hari = 28`.
6. - Jika di luar bulan 1-12: `validitas = False`.
7. Validasi rentang nilai: periksa apakah `1 <= tanggal <= jumlah_hari` dan `1 <= bulan <= 12`. Jika ya `validitas = True`, jika tidak `validitas = False`.
8. Pemeriksaan hasil: jika `validitas` bernilai True, cetak tanggal valid; jika False cetak bukan tanggal valid.
9. Program selesai (End).
