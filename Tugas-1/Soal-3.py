# Menentukan siswa lulus ujian atau tidak
# siswa lulus jika nilai teori dan nilai praktek >= 70
# input user berupa nilai ujian teori dan nilai ujian praktek

teori    = int(input("Masukkan nilai ujian teori: "))
praktek  = int(input("Masukkan nilai ujian praktek: "))

nilai_teori   = 70
nilai_praktek = 70

if teori >= nilai_teori and praktek >= nilai_praktek :
    print("Selamat, anda lulus")
elif teori >= nilai_teori and praktek < nilai_praktek :
    print("Anda harus mengulang ujian praktek")
elif teori < nilai_teori and praktek >= nilai_praktek :
    print("Anda harus mengulang ujian teori")
else :
    print("Anda harus mengulang ujian teori dan praktek")


