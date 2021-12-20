#dictionary
mydict = {
    "brand": "ford",       #brand = keys ; ford = values
    "model": "Mustang",
    "year": 1964
}
print(mydict)

#access value
print(mydict["model"])     #yg dipanggil keys nya

#change value
mydict["brand"] = "Ferrari"

print(mydict)

#Quiz
mydict = {
    'Name': 'Zara',
    'Age' : 7,
    'Class': 'First'
}
mydict['Age'] = 8;
mydict['School'] = 'DPS School'

print("dict['Age']: ",mydict['Age'])
print("dict['School']", mydict['School'])

#function without parameter
def myFunction():
    print("hello from a function")

myFunction() #manggil function yang dibuat

#function with parameter
def myFunction(nama):
    print("halo nama saya: " + nama)

myFunction("dewa")
myFunction("darren")

#contoh lain dg parameter
def fungsiLuasPersegi(p,l):
   print (p*l)

fungsiLuasPersegi(2,3)
fungsiLuasPersegi(100,200)

#function keyword parameter
def myfunction(child3, child2, child1):
    print("the youngest child is " + child3)

myfunction(child1 = "Emil", Child2 = "Tobi", child3 = "Enzo")

#function with return value
def myfunction(x):
    y = x**2 + 2*x + 3
    return y

print(myfunction(3))
print(myfunction(5))
print(myfunction(8))

#Quiz
def myfunction():
    x = 10
    print("value inside function: ", x)

x = 20
myfunction()
print("value outside function: ", x)

#contoh fungsi luas dengan input
def LuasPersegi(p,l):
    L = p*l
    return L      #manggil hasil L

p = int(input("masukkan panjang: "))
l = int(input("Masukkan lebar: "))
print("Luas persegi panjang: {} cm^2".format(LuasPersegi(p,l)))

#Contoh program
def fungsiLuas(p, l):
   L = p * l
   return L

def fungsiKeliling(p, l):
   K = 2 * (p + l)
   return K

while True:
   print('''
   -- Selamat Datang --
   1. Menghitung Luas
   2. Menghitung Keliling
   3. Keluar
   ''')
   pilihan = int(input("Masukan pilihan Anda: "))
   
   if pilihan == 1:
      p = int(input("Masukan panjang: "))
      l = int(input("Masukan lebar: "))
      print("Luas persegi panjang adalah: {}".format(fungsiLuas(p, l)))

   elif pilihan == 2:
      p = int(input("Masukan panjang: "))
      l = int(input("Masukan lebar: "))
      print("Keliling persegi panjang adalah: {}".format(fungsiKeliling(p, l)))

   elif pilihan == 3:
      break

   else :
      print("Masukan pilihan dengan benar!")
