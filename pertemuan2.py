#user input

nama = input("masukan nama anda: ") # default string
umur = int(input("masukan umur: "))

print("nama saya adalah:" + nama)
print(type(umur))

#menghitung luas persegi panjang
p = int(input("masukan panjang:" ))
l = int(input("masukan lebar: "))
L = p*l 
k = 2*p + 2*l 
print("maka luas persegi panjang : {} cm^2 dan kelilingnya : {} cm".format(L,k))

x = "Indonesia"
y = "AI"
print(x + " " + y)

#string operations
a = "Halo, Dunia!"
print(a[0]) #karakter ke-0 adalah huruf H
print(a[2:8]) #mulai dari karakter ke-2 sd ke-7
print(len(a)) #menghitung panjang karakter
print(a[0] + " " + a[2]) #menampilkan huruf H dan l

#Quiz
x = "Indonesia AI"
print(x[2:4]) #karakter ke 2 sd 3
print(len(x))

#boolean
print(8 < 9)
print(8 > 9)

#condition
a = 200
b = 200
if b < a:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")
else:
    print("b is greater than a")

nilai = int(input("masukan nilai anda: "))
kkm = 70

if nilai < kkm:
    print("anda harus mengulang")
else:
    print("selamat anda lulus")
    print("anda akan diwisuda")

#list
y = [1, 2, 3, 4, 5]
print(y[3])
print(y[0]+y[1])


makanan = ["soto", "mi ayam", "sate"]
print(makanan[0])

#mau tambah makanan bakso
makanan.append("bakso")
print(makanan[3])

minuman = []
harga = []

minuman.append(input("masukan nama kontak: "))
minuman.append(input("masukan nama kontak: "))
minuman.append(input("masukan nama kontak: "))

harga.append(input("masukan harga: "))
harga.append(input("masukan harga: "))
harga.append(input("masukan harga: "))

print(minuman)
print(harga)

#mengganti minuman
minuman = ["es teh", "es jeruk", "syrup",]

minuman[0] = input("minuman pengganti: ")
print(minuman)

#Quiz
c = 3
a = c
b = c + 1
if b > a:
    print("b is greater than a")
elif c == b:
    print("c is same like b")
else :
    print("other")


    


