#Minta pengguna untuk memasukkan dua bilangan
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))

# Inisialisasi variabel untuk bilangan terbesar
bilangan_terbesar = bilangan1

# Periksa apakah bilangan kedua lebih besar dari bilangan_terbesar
if bilangan2 > bilangan_terbesar:
    bilangan_terbesar = bilangan2

# Tampilkan bilangan terbesar
print("Bilangan terbesar adalah:", bilangan_terbesar)