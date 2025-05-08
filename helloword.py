#print helloword
print("hello word")

#komentar
#nama saya
print ("Resya nur aisah ibrahim")
#kelas
print ("X PPLG 1")

#Tipe data
print(("1,2,3,4,5"))
print({"siapa nama kamu?"})

#Variabel pyhton
Kiri = "Kamu"
Kanan = "Aku"
Kata = Kanan + " " + Kiri
print("Siapa:\n",Kata, "\n")

#Operator aritmatika

#TAMBAH
kue = 10
bery = 5
Total = kue + bery 
print(Total)

#KURANG
kue = 10
bery = 5
Total = kue - bery 
print(Total)

#PERKALIAN
kue = 10
bery = 5
Total = kue * bery 
print("Total kue yg di dapat",Total)

#OPERATOR PERBANDINGAN

# Sama dengan (==)
print('Operator sama dengan')
print('10 == 10 bernilai', 10 == 10)
print('7 == 8 bernilai', 7 == 8)
print()

# Lebih kecil dari atau sama dengan (<=)
print('Operator lebih kecil dari atau sama dengan')
print('2 <= 1 bernilai', 2 <= 1)
print('2 <= 2 bernilai', 2 <= 2)
print('2 <= 5 bernilai', 2 <= 5)
print()

# Operator Penugasan

print('Operator tambah sama dengan')
x = 3
print(x)
x += 4
print(x)
print()

# Pembagian bulat sama dengan (//=)
print('Operator pembagian bulat sama dengan')
x = 20
print(x)
x //= 6
print(x)
print()

#Operator Logical

print('8 > 6 dan 8 > 4 bernilai', 8 > 6 and 8 > 4)
print('8 > 6 dan 8 > 12 bernilai', 8 > 6 and 8 > 12)
print('6 > 2 atau 6 > 3 bernilai', 6 > 2 or 6 > 3)
print('6 > 2 atau 6 > 9 bernilai', 6 > 2 or 6 > 9)
print()
print('not 6 > 3 bernilai', not 6 > 3)

# Operator Bitwise

x = 22  # dalam biner: 0001 0110
y = 10  # dalam biner: 0000 1010
z = x & y  # hasil:      0000 0010 (2)
print(z)
print()

# Operator Keanggotaan

angka = [7, 8, 9, 10, 11]
print('angka =', angka)
print('9 not in angka bernilai', 9 not in angka)
print('3 not in angka bernilai', 3 not in angka)

# Operator Identitas

x, y, z, w = 30, 30, 25, x
print('x =', x)
print('y =', y)
print('z =', z)
print('w =', w)
print('x is y bernilai', x is y)
print('x is z bernilai', x is z)
print('x is w bernilai', x is w)
print('y is w bernilai', y is w)
print()