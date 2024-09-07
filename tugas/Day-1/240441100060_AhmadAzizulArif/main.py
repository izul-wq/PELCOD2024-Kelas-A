# referensi https://revou.co/panduan-teknis

welcome = "SELAMAT DATANG"
aritmatika = "penjumlahan, pengurangan, perkalian, pembagian"

# Selamat datang
print("************************************")
print(f"********** {welcome} **********")
print("************************************")

# Data diri
nama_user = input("Nama : ")
nim_user = input("Nim : ")
print("************************************")

# Judul
print('''
OPERASI ARITMATIKA
''')

# Aritmatika
print("Silahkan Pilih Proses Aritmatika Di Bawah Ini")
operator = input("penjumlahan, pengurangan, perkalian, pembagian : ")
print("")

# Masukkan angka
angka1 = int(input("Masukkan Angka Pertama : "))
angka2 = int(input("Masukkan Angka Kedua : "))
print("")

# Rumus
if operator == "penjumlahan":
    total = angka1 + angka2
elif operator == "pengurangan":
    total = angka1 - angka2
elif operator == "perkalian":
    total = angka1 * angka2
elif operator == "pembagian":
    total = angka1 / angka2
    
# Hasil
print(f"{aritmatika} dari {angka1} dan {angka2} adalah {total}")