import datetime

class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def tampilkan_info(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")

    def hitung_usia(self):
        tahun_ini = datetime.datetime.now().year
        return tahun_ini - self.tahun_terbit

# Contoh penggunaan
buku1 = Buku("Seni Menjadi Bodoamat", "Mark Manson", 2016)
buku2 = Buku("Harry Potter", "J.K. Rowling", 1997)
buku3 = Buku("Atomic Habits", "James Clear", 2018)

buku1.tampilkan_info()
print(f"Usia buku: {buku1.hitung_usia()} tahun")
print()

buku2.tampilkan_info()
print(f"Usia buku: {buku2.hitung_usia()} tahun")
print()

buku3.tampilkan_info()
print(f"Usia buku: {buku3.hitung_usia()} tahun")