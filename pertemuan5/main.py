# spill assignment 2
nama = []
nomor = []

def tampilkan_kontak():
   for x in range(len(nama)):
      print("Nama ke {}: {}, Nomor: {}".format(x+1, nama[x], nomor[x]))

def tambah_kontak():
   for x in range(jmlh):
      nama.append(str(input("Masukan Nama ke {}: ".format(x+1))))
      nomor.append(int(input("Masukan Nama ke {}: ".format(x+1))))

while True:
   print("""
   -- Program Kontak --
   1. Tampilkan Kontak
   2. Tambah Kontak
   3. Keluar
   """)
   pilihan = int(input("Masukan Pilihan Anda: "))

   if pilihan == 1:
      tampilkan_kontak()
   elif pilihan == 2:
      jmlh = int(input("Masukan jumlah yg ingin ditambah: "))
      tambah_kontak()
   elif pilihan == 3:
      break
   else:
      print("Pilihan tidak tersedia")


# modul manual
import mymodules
mymodules.greeting("adit")

# modul built in
import math
phi = math.pi
print(phi)

print(math.sqrt(256))

import datetime
print(datetime.datetime.now())

# modul download firt (using pip install sympy on terminal)
import sympy
print(sympy.isprime(5))
print(list(sympy.primerange(0, 100)))

# File handling

# append or write
f = open("file.txt", "w")
f.write("baris pertama")
f.close()

# read
f = open("file.txt", "r")
print(f.read())

f = open("file.txt", "r")
print(f.readline())

import os
os.remove("file.txt")

# Quiz
import matematika

print("PI: ", matematika.pi)
print(matematika.luas_persegi(sisi=12))