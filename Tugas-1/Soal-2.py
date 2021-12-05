#menghitung luas lingkaran
#input user berupa r(jari-jari) lingkaran
#phi = konstanta 22/7

r           = int(input("masukkan jari-jari lingkaran: "))
phi         = 22/7
L_lingkaran = float(phi*r*r)

print("Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2".format(r,L_lingkaran))
