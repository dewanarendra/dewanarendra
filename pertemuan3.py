buah = ["apel", "jeruk", "semangka", "nanas"]

for x in buah:
    print(x)

# for in range
for x in range(5): #stop
    print(x)

for x in range(16, 24): #start dan stop
    print(x)

for x in range(3, 20, 3): #start stop dan step
    print(x)

for x in range(10):
    print("checkmate")

#menggabungkan for dengan input
nama = []
jumlah = int(input("Masukan jumlah yang diinginkan: "))

for x in range(jumlah):
    nama.append(input("Masukan nama ke {}:".format(x+1)))

for x in range(1, jumlah+1):
    print(nama[0:x])

#misal fungsi for dengan increment
i = 1             #start
while i < 6:      #stop
    print(i)
    i = i + 1     #step

#infinite loop
while True:
    print("road")

#break
for x in range(7):
    if x == 4:
        break
    print(x)

#continue
for x in range(7):
    if x == 4:
        continue
    print(x)

#nested loop ; loop di dalam loop
for i in range(2):
    for j in range(3):
        print("i: {}, j: {}".format(i,j), end=" ")
    print()

#mengambil import ascii lowercase 
from string import ascii_lowercase
for i in range(1,123):
    print(chr(i))

#Quiz
x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 5, 6]
z = 0

for i in x:
    for j in y:
        if i == j:
            z = z + 1
    print(z)




        










   
