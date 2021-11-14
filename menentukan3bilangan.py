#Menentukan Bilangan Terbesar Dari Tiga Buah Bilangan
#Meminta user memasukan angka
a = int (input("masukan bilangan a = "))
b = int (input("masukan bilangan b = "))
c = int (input("masukan bilangan c = "))

maks = 0

print (a, b, c)
if a > b:
    maks = a
else:
    maks = b

if c > maks:
    maks = c
    
    print("terbesar: ",maks)
