# NOTE - first function
print("Ini fungsi pertama:")
# first function
def hello_world():
    print("Hello! world!")
    print("welcome to the function")
    
# pemanggilan func()
hello_world()
hello_world()

print("=======================")

# NOTE - parameter(param)
print("Ini fungsi kedua tentang parameter dan argumen")
# second func - parameter
def sapa_teman(nama_orang):
    print(f"halo, udah lama gak ketemu nih {nama_orang}")
 
 # panggil teman menggunakan argumen: "Joko"
sapa_teman("Joko")

print("=========================")

# NOTE - return func()
print("Ini berfungsi untuk mengembalikan/menyimpan fungsi ke nilai sehingga nantinya bisa dipanggil lagi.")

# wrong func
print("1. cara yang salah")
def tambah_salah(a,b):
    hasil = a + b
    print(hasil)
    
total = tambah_salah(3,5)
print(total)
# jika di print maka tidak ada hasil apa-apa karena tidak menyimpan dan mengembalikan nilai
print(total)

# right func
print("2. cara yang benar")
def tambah_benar(a,b):
    return a + b

totalBenar = tambah_benar(3,5)
print(totalBenar)
print("=============================")

# NOTE - variabel lokal
print("Belajar variable lokal")
# print("\n")
def fungsi_rahasia():
    x = 100 # Ini variabel lokal (hanya hidup di dalam sini)
    print(x) # Ini berhasil

fungsi_rahasia()
print(x)

# print(x) # INI AKAN ERROR! 
# Python akan bilang: "Siapa itu x? Saya tidak kenal."
# Kenapa begitu? Supaya aman. Bayangkan kalau kamu punya program besar dengan 100 function, dan semua pakai variabel nama x. Kalau tidak dipisah (di-lokalisasi), programmu akan hancur berantakan karena nilai x saling tumpang tindih.
print("==============================")

# NOTE - usecase sederhana
print("Ini usecase sederhana")
# 1. Function menghitung pajak (10%)
def hitung_pajak(harga):
    return harga * 0.1

# 2. Function utama
def hitung_total_bayar(harga_barang):
    pajak = hitung_pajak(harga_barang) # Memanggil function di atas
    total = harga_barang + pajak
    return total

# Uji coba
harga_laptop = 5000000
yang_harus_dibayar = hitung_total_bayar(harga_laptop)

print(f"Total yang harus dibayar: Rp {yang_harus_dibayar}")