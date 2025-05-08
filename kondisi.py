# Kondisi if 

nilai = 5

if(nilai > 3):
  print("Nilai Lebih Besar Dari Angka Tiga") 

if(nilai > 10):
  print("Nilai Lebih Besar Dari Angka Sepuluh")

 
# Kondisi if-else

nilai = 6

if nilai >= 7:
    print("Lulus")
else:
    print("Tidak Lulus")

# Kondisi if-elif-else

nilai = 85

if nilai >= 90:
    print("Grade A")
elif nilai >= 80:
    print("Grade B")
elif nilai >= 70:
    print("Grade C")
else:
    print("Grade D")

#PENGULANGAN

# While loop

nilai = 1

while nilai <= 3: 
    print("Nilai =", nilai)
    nilai += 1  

# For loop

for i in range(1, 3):  
    print("Angka:", i)

# For loop

for i in range(1, 3):  
    print("Angka:", i)

# Fungsi abs() untuk nilai absolute

x, y = -15, 7
print('Nilai absolute dari', x, 'adalah =', abs(x))
print('Nilai absolute dari', y, 'adalah =', abs(y))
print()

x, y, z = -4, -11, 6
print('x =', x, 'y =', y, 'z =', z)
print('Nilai Tertinggi dari ketiga variabel di atas adalah =', max(x, y, z))
print('Nilai Terendah dari ketiga variabel di atas adalah =', min(x, y, z))
print()

# Fungsi max() dan min() untuk list

data = [12, 5, 18, 7]
print('data =', data)
print('Nilai Tertinggi dari list di atas adalah =', max(data))
print('Nilai Terendah dari list di atas adalah =', min(data))
print()

# Fungsi max() dan min() dengan string dalam list

kata = ['apel', 'jeruk', 'mangga', 'pisang']
print('kata =', kata)
print('String dengan urutan alfabet tertinggi di list di atas adalah =', max(kata))
print('String dengan urutan alfabet terendah di list di atas adalah =', min(kata))

#STRING

name = 'Resya Nur Aisah'
message = "Resya Nur Aisah sedang belajar pemrograman di Belajarpython"
print("name[0]: ", name[0])  
print("message[0:5]: ", message[0:5])  

print("name[5]: ", name[5]) 
print("message[6:10]: ", message[6:10]) 

nama = 'Resya Nur'
print('sebelum =', nama)
nama_lengkap = nama[:5] + ' Aisah ' + nama[5:]
print('sesudah =', nama_lengkap)
x = nama[6:] + " " + nama[:5]
print(x)
