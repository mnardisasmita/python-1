a,b,c = 1,5,"Hello Dunia awal"
print(a)
print(c)

print ("Hello Dunia")
print ("Selamat Datang di pemograman Python")
print ("Saya belajar Pyrhin dengan PyCharm")
print ("Salam , MNA")

nama = "Mulya N Ardisasmita"
NAMA = "MNA saja "
print(NAMA+nama+" Nama saya")


nama = "Hartono"
alamat = 'Mataram'
umur = 19
tinggi = 170.5
menikah = True
# mencetak isi variabel
print ("Nama : ", nama)
print ("Alamat : ", alamat)
print ("Umur : ", umur)
print ("Tinggi : ", tinggi)
if(menikah):
    print ("Status: menikah")
else:
    print ("Status: belum menikah")

a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", c)

#modifikasi dari yang diatas

angka = int(input("Masukan Nilai : "))
bangka = 10
cangka = 0

cangka = angka + bangka
print ("Line 1 - Value of cangka is ", cangka)


# Ambil input untuk mengisi nilai
a = int(input("Inputkan nilai a: "))
b = int(input("Inputkan nilai b: "))

# Menggunakan operator penjumlahan
c = a + b
print ("Hasil %d + %d = %d" % (a,b,c))

# Operator Pengurangan
c = a - b
print ("Hasil %d - %d = %d" % (a,b,c))

# Operator Perkalian
c = a * b
print ("Hasil %d * %d = %d" % (a,b,c))

# Operator Pembagian
c = a / b
print ("Hasil %d / %d = %d" % (a,b,c))

# Operator Sisa Bagi
c = a % b
print ("Hasil %d %% %d = %d" % (a,b,c))

# Operator Pangkat
c = a ** b
print ("Hasil %d ** %d = %d" % (a,b,c))

#Latihan Input
angka_satu = int(input("Angka ke satu: "))
angka_dua = int(input("Angka ke dua: "))
hasil_angka = angka_satu + angka_dua

print ("{} dengan {} sepertinya angka yang berdekatan :)".format(angka_dua, angka_satu))
print(hasil_angka)


print ("{} dengan {} sepertinya benda yang berdekatan :)".format("laptop", "mouse"))

# Ambil input untuk mengisi nilai
a = int(input("Inputkan nilai a: "))

# tambahkan dengan 2
a += 2
# kurangi 3
a -= 3
# kali 10
a *= 10
# bagi dengan 4
a /= 4
# pangkat 10
a **= 10

# Berapakah nilai a sekarang?
print ("Nilai a adalah %d" % a)




# file: operator_pembanding.py
a = int(input("Inputkan nilai a: "))
b = int(input("Inputkan nilai b: "))

# apakah a sama dengan b?
c = a == b
print ("Apakah %d == %d: %r" % (a,b,c))

# apakah a < b?
c = a < b
print ("Apakah %d < %d: %r" % (a,b,c))

# apakah a > b?
c = a > b
print ("Apakah %d > %d: %r" % (a,b,c))

# apakah a <= b?
c = a <= b
print ("Apakah %d <= %d: %r" % (a,b,c))

# apakah a >= b?
c = a >= b
print ("Apakah %d >= %d: %r" % (a,b,c))

# apakah a != b?
c = a != b
print ("Apakah %d != %d: %r" % (a,b,c))