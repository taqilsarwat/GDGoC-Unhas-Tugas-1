nama = "Taqil"
isStudent = True
nilai_angka = 90

if isStudent == True:
    if nilai_angka < 0 or nilai_angka > 100:
        nilai_huruf = "Nilai: Tidak Valid"
    elif nilai_angka >= 90:
        nilai_huruf = "Nilai: A"
    elif nilai_angka >= 80:
        nilai_huruf = "Nilai: B"
    elif nilai_angka >= 70:
        nilai_huruf = "Nilai: C"
    elif nilai_angka >= 60:
        nilai_huruf = "Nilai: D"
    else:
        nilai_huruf = "Nilai: Error"
    print(f"Nilai Mahasiswa adalah {nilai_angka}")
else:
    print("Anda Bukan Siswa!!")
