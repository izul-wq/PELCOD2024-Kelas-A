namas = "Adimas Mochammad Alfan"
nim = 240441100120
ipk = 4.00
mahasiswa = True

# ini adakah format natural (tipe data sama)
print("Nama saya adalah =", namas)
print("Nim saya adalah =", nim)
print("impian ipk =", ipk)
print("mahasiswa =",  mahasiswa)


# ini adalah format string (tipe data diubah menjadi string)
print(f"nama saya adalah {namas}")
print(f"nim saya adalah {nim}")
print(f"ipk saya adalah {ipk}")
print(f"mahasiswa saya adalah {mahasiswa}")


# program dinamis string
nama_panjang = str(input("nama saya adalah = "))

# program dinamis integer
nilai_matematika =int(input("nilai saya adalah = "))

nilai_matematika = 89 
nilai_biologi = 75 
nilai_kimia = 90 
nilai_fisika = 82 

penjumlahan = nilai_matematika + nilai_kimia
perkalian = nilai_fisika * nilai_biologi
pengurangan = nilai_biologi - nilai_kimia
pembagian = nilai_matematika / nilai_fisika

print(f"hasil penjumlahan dari matematika dan kimia adalah =  {penjumlahan}")
print(f"hasil perkalian dari fisika dan biologi adalah =  {perkalian}")
print(f"hasil pengurangan dari biologi dan kimia adalah =  {pengurangan}")
print(f"hasil pembagian dari matematika dan fisika adalah =  {pembagian}")

usia_masuk_kuliah = int(input("berapa usia anda saat masuk kuliah ? "))
lama_kuliah = int(input("lama kuliah anda ? "))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah
tahun_lulus = 2024  + lama_kuliah

print(f"saya ini, bernama {namas} berusia {usia_saat_ini} ")
print(f"saya {namas} akan lulus pada tahun {tahun_lulus} ")

