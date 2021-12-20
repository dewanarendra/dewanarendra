"""
Program menyimpan kontak dan menampilkan kontak
Kontak terdiri dari nama dan nomor telepon
Ketika program running, akan menampilkan pesan sambutan dan menu
Program secara otomatis kembali ke menu apabila user telah selesai melihat atau menambah kontak
"""

#daftar kontak
daftarkontak = []
daftarkontak.append({
   "Nama" : "Farhan",
   "Telepon" : "08123456789"
})
daftarkontak.append({
    "Nama" : "Joko",
    "Telepon" : "08987654321"
})

def list_kontak(daftarkontak):
    for kontak in daftarkontak:
        print("-------------------------")
        print(f"Nama : {kontak['Nama']}")                    #kontak [keys]
        print(f"No Telp : {kontak['Telepon']}")               #kontak [keys]
        print("-------------------------")

def tambah_kontak():
    Nama = input("Masukkan Nama : ")
    NoTelp = input("Masukkan Telepon : ")
    kontak = {
        "Nama" :  Nama,
        "Telepon" : NoTelp
    }
    return kontak
        

#main program
while True:
    print("Selamat Datang!")
    print('''
    === Menu ===
    1. Daftar Kontak
    2. Tambah Kontak
    3. Keluar
    ''')
    
    menu = int(input("Pilih Menu: "))

    if menu == 3:
        break
    elif menu == 1:
        list_kontak(daftarkontak)
       
    elif menu == 2:
        daftarkontak.append(tambah_kontak())
        print("Kontak berhasil ditambahkan")
          
    else:
        print("Menu tidak tersedia")

print("Program selesai, sampai jumpa!")
    



   