# <h1 align="center">TUGAS PRAKTIKUM IPDS 1</h1>
<p align="center">Anggun Dewanti (2311110022)</p>

## Unguided 

### 1. Memecahkan Masalah Unik dengan Loop dan If-Else

### Buatlah program yang dapat menghasilkan pola berbentuk angka seperti di bawah ini, dengan syarat angka yang ditampilkan adalah hasil dari penjumlahan bilangan prima sebelumnya:
```
1
2 3
5 7 11
13 17 19 23
...
```
### Jumlah angka pada setiap baris bertambah 1, dan bilangan yang ditampilkan adalah bilangan prima.



```python
def is_prime(n): 
    if n < 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_pattern(n):
    primes = []
    num = 2
    while len(primes)< n * (n + 1) // 2 :
        if is_prime(num):
            primes.append(num)
        num +=1
    
    result = []
    for i in range(n):
        row = primes[:i+1]
        result.append(row)
        primes = primes[i+1:]
    return result

# Contoh penggunaan
n = 4
pattern = generate_pattern(n)
for row in pattern:
    print(' '.join(map(str, row)))
```

#### Output :
![1](https://github.com/user-attachments/assets/65eeb477-5ad7-4c0e-813a-ad143cf3e61f)

```


#### Interpretasi
Kode di atas mengimplementasikan algoritma pencarian biner untuk menemukan indeks elemen genap dalam daftar; jika elemen ditemukan, indeksnya dikembalikan, sedangkan jika tidak ditemukan dan target adalah bilangan ganjil, akan dicetak pesan bahwa nilai tersebut tidak ada dalam daftar.
```


### 2. Membuat Fungsi dengan Syarat Spesifik

### Buatlah sebuah fungsi yang menerima dua input berupa list angka. Fungsi ini harus mengembalikan sebuah list baru yang berisi elemen dari dua list input yang memiliki indeks ganjil. List baru tersebut juga harus diurutkan secara menurun berdasarkan nilai elemen.



```python
def extract_odd_elements(list1, list2):
    result = []
    for i in range(1, len(list1), 2):
        result.append(list1[i])
    for i in range(1, len(list2), 2):
        result.append(list2[i])
    return sorted(result, reverse=True)

# Contoh penggunaan
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print(extract_odd_elements(list1, list2))
```

#### Output :
![2](https://github.com/user-attachments/assets/3e461eb1-de95-4ccd-8b78-0af2a1d556b9)

```


#### Interpretasi
Fungsi extract_odd_elements mengambil elemen-elemen dari indeks ganjil (dimulai dari 1) dari dua daftar, kemudian menggabungkannya, mengurutkannya secara menurun, dan mengembalikan hasilnya sebagai daftar baru.
```
### 3. Exception Handling dalam Konteks Nyata

### Buat sebuah program untuk mensimulasikan transaksi ATM. Program harus:
1. Meminta pengguna memasukkan PIN (dibatasi 3 kali percobaan).
2. Setelah PIN benar, meminta jumlah penarikan.
3. Jika saldo kurang dari jumlah yang ditarik, munculkan pesan kesalahan.
4. Jika penarikan berhasil, tampilkan saldo akhir.




```python
def atm_transaction():
    pin = 1234  # Anggap saldo awal adalah 1000
    balance = 1000
    attempt = 0

    while attempt < 3:
        user_pin = int(input("Masukkan PIN Anda: "))
        if user_pin == pin:
            amount = int(input("Masukkan jumlah penarikan: "))
            if amount > balance:
                print("Maaf, saldo Anda tidak mencukupi.")
            else:
                balance -= amount
                print(f"Penarikan berhasil. Saldo akhir: {balance}")
            return
        else:
            attempt += 1
            print("PIN yang Anda masukkan salah. Silakan coba lagi.")

    print("Maaf, Anda telah mencapai batas percobaan. Kartu Anda terblokir.")

# Contoh penggunaan
atm_transaction()

```
#### Output :
![3](https://github.com/user-attachments/assets/95184803-2462-410e-90d4-66c248a71df8)

```


#### Interpretasi
Kode di atas adalah implementasi sederhana dari transaksi ATM, di mana pengguna harus memasukkan PIN dengan maksimal 3 kali percobaan. Jika PIN benar, pengguna dapat menarik sejumlah uang selama saldo mencukupi, dan saldo akan diperbarui. Jika PIN salah sebanyak 3 kali, kartu akan terblokir.
```

### 4. Studi Kasus Pengelolaan Data

### Anda diberikan file CSV berisi data nilai ujian mahasiswa. Tugas Anda adalah menulis sebuah program yang:
1. Membaca file CSV dan menyimpan datanya ke dalam dictionary.
2. Menghitung rata-rata nilai tiap mahasiswa.
3. Menampilkan mahasiswa dengan nilai tertinggi dan terendah


```python
import csv
from statistics import mean

def baca_data_csv(nama_file):
    data_siswa = {}
    with open(nama_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Lewati baris header
        for row in csv_reader:
            nama, nilai = row
            data_siswa[nama] = int(nilai)
    return data_siswa

def hitung_rata_rata(data_siswa):
    return mean(data_siswa.values())

def cari_nilai_tertinggi_terendah(data_siswa):
    nilai_tertinggi = max(data_siswa.values())
    nilai_terendah = min(data_siswa.values())
    siswa_tertinggi = [nama for nama, nilai in data_siswa.items() if nilai == nilai_tertinggi]
    siswa_terendah = [nama for nama, nilai in data_siswa.items() if nilai == nilai_terendah]
    return siswa_tertinggi, siswa_terendah

def main():
    nama_file = 'nilai_siswa.csv'  # Ganti dengan nama file CSV Anda
    
    # 1. Membaca file CSV dan menyimpan datanya ke dalam dictionary
    data_siswa = baca_data_csv(nama_file)
    
    # 2. Menghitung rata-rata nilai
    rata_rata = hitung_rata_rata(data_siswa)
    
    # 3. Menampilkan mahasiswa dengan nilai tertinggi dan terendah
    siswa_tertinggi, siswa_terendah = cari_nilai_tertinggi_terendah(data_siswa)
    
    # Menampilkan hasil
    print(f"Rata-rata nilai: {rata_rata:.2f}")
    print(f"Siswa dengan nilai tertinggi ({max(data_siswa.values())}): {', '.join(siswa_tertinggi)}")
    print(f"Siswa dengan nilai terendah ({min(data_siswa.values())}): {', '.join(siswa_terendah)}")

if __name__ == "__main__":
    main()

```
#### Output :
![4](https://github.com/user-attachments/assets/103f6419-1506-4af2-9e99-fc1877c24649)

```


#### Interpretasi
Kode di atas adalah program Python yang membaca data nilai siswa dari file CSV, menghitung rata-rata nilai, dan menemukan siswa dengan nilai tertinggi dan terendah. Program menggunakan modul csv untuk membaca file CSV dan menyimpan data dalam bentuk dictionary, di mana nama siswa menjadi kunci dan nilai mereka sebagai nilai. Kemudian, program menghitung rata-rata nilai siswa menggunakan fungsi mean, dan mencari siswa dengan nilai tertinggi serta terendah. Hasilnya ditampilkan di terminal, termasuk rata-rata nilai, nama siswa dengan nilai tertinggi, dan nama siswa dengan nilai terendah.
```
### 5. Kombinasi Logika dan Kreativitas

### Buatlah permainan sederhana menggunakan Python, di mana komputer akan memilih sebuah angka secara acak antara 1 hingga 100, dan pengguna harus menebak angka tersebut. Setiap tebakan yang salah akan memberikan petunjuk apakah angka yang ditebak lebih besar atau lebih kecil dari angka sebenarnya. Batasi jumlah percobaan menjadi 5 kali. Setelah permainan selesai, tampilkan apakah pemain menang atau kalah.

```python
import random

def tebak_angka():
    print("Selamat datang di permainan Tebak Angka!")
    print("Komputer akan memilih sebuah angka acak antara 1 dan 100.")
    print("Kamu punya 5 kali kesempatan untuk menebak.")

    angka_rahasia = random.randint(1, 100)
    percobaan = 0

    while percobaan < 5:
        tebakan = int(input("Masukkan tebakan Anda: "))
        percobaan += 1

        if tebakan == angka_rahasia:
            print(f"Selamat, Anda menebak dengan benar! Angka rahasia adalah {angka_rahasia}.")
            return
        elif tebakan < angka_rahasia:
            print("Tebakan Anda terlalu kecil.")
        else:
            print("Tebakan Anda terlalu besar.")

    print(f"Maaf, Anda gagal menebak angka rahasia. Angka rahasia adalah {angka_rahasia}.")

# Menjalankan permainan
tebak_angka()

```
#### Output :
![5](https://github.com/user-attachments/assets/9d5cf7df-55d4-42a3-bed2-7009dbda10bb)

```


#### Interpretasi
Kode di atas adalah implementasi dari permainan "Tebak Angka" di mana komputer memilih angka acak antara 1 hingga 100, dan pemain memiliki 5 kesempatan untuk menebak angka tersebut. Jika tebakan pemain sesuai dengan angka rahasia, permainan selesai dengan pesan kemenangan; jika tebakan terlalu besar atau kecil, petunjuk diberikan. Jika pemain gagal menebak setelah 5 percobaan, permainan berakhir dengan pengungkapan angka rahasia.
```
### 6. Rekursi yang Tidak Biasa

### Buat fungsi rekursif yang menerima input bilangan bulat `n` dan menghasilkan urutan bilangan seperti berikut ini:
```
Input: n = 4
Output: 1, 1, 2, 6, 24
```
Fungsi ini harus menggunakan konsep rekursi untuk menghitung faktorial setiap angka hingga `n`.


```python
def calculate_sequence(n):
    if n == 1:
        return [1]
    else:
        prev_sequence = calculate_sequence(n - 1)
        current_factorial = 1
        for i in range(1, n + 3):
            current_factorial *= i
        return prev_sequence + [current_factorial]

# Contoh penggunaan
n = 4
print(', '.join(map(str, calculate_sequence(n)))) 

```
#### Output :
![6](https://github.com/user-attachments/assets/e60fcb13-bf99-4db8-ad4d-e2f577ded053)

```


#### Interpretasi
Kode di atas merupakan sebuah fungsi rekursif yang menghasilkan deret bilangan, di mana setiap elemen dalam deret tersebut merupakan hasil faktorial dari n + 2, dengan n merupakan urutan elemen tersebut dalam deret. Fungsi ini memulai dengan basis kasus n == 1 yang mengembalikan daftar berisi angka 1, lalu untuk setiap n berikutnya, ia menghitung faktorial dari n + 2 dan menambahkannya ke deret hasil sebelumnya.
```

### 7. Pemrograman dengan Algoritma Greedy

### Buatlah program untuk memecahkan masalah "minimum coin change". Diberikan jumlah uang dan daftar nilai koin yang tersedia (misalnya, 1, 5, 10, 25), tentukan kombinasi minimum koin yang diperlukan untuk mencapai jumlah uang tersebut. Namun, program Anda harus bisa menangani koin-koin yang nilai dan jumlahnya ditentukan pengguna.



```python
def minimum_coin_change(amount, coins):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        count = amount // coin
        result.extend([coin] * count)
        amount -= coin * count
    return result

# Contoh penggunaan
amount = 90
coins = [1, 5, 10, 25]
print(minimum_coin_change(amount, coins))

```
#### Output :
![7](https://github.com/user-attachments/assets/3466e089-989d-43bd-80aa-907010be91b1)

```


#### Interpretasi
Kode di atas mengimplementasikan algoritma untuk menentukan jumlah koin minimum yang diperlukan untuk mencapai nilai tertentu (amount) menggunakan denominasi koin yang tersedia. Fungsi minimum_coin_change pertama-tama mengurutkan koin dalam urutan menurun, lalu membagi jumlah yang dibutuhkan dengan nilai koin terbesar, dan menambahkan koin tersebut ke hasil sebanyak mungkin hingga nilai yang tersisa menjadi nol. Hasilnya adalah daftar koin yang mewakili kombinasi optimal untuk mencapai nilai amount.
```
### 8. Kombinasi String dan Manipulasi List

### Buat sebuah program yang menerima string dari pengguna dan mengonversi string tersebut menjadi sebuah list berisi kata-kata terbalik. Misalnya:
```
Input: "Saya suka Python"
Output: ["ayaS", "akus", "nohtyP"]
```

```python
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return reversed_words

# Contoh penggunaan
input_sentence = "Kata Kata Hari Ini Paham?!"
output_list = reverse_words(input_sentence)
print(output_list)

```
#### Output :
![8](https://github.com/user-attachments/assets/c636ed2b-e685-49ef-9770-e09095da311e)

```


#### Interpretasi
Kode di atas mendefinisikan fungsi reverse_words yang membalikkan setiap kata dalam kalimat yang diberikan, kemudian mengembalikan daftar kata yang telah dibalik.
```

### 9. Konsep Class dan Object-Oriented Programming

### Buat class bernama `Buku` yang memiliki atribut `judul`, `penulis`, dan `tahun_terbit`. Buat method dalam class untuk menampilkan informasi buku, serta method untuk menghitung usia buku berdasarkan tahun saat ini. Buatlah 3 objek dari class `Buku` dan tampilkan informasi serta usia masing-masing buku.

```python
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

```
#### Output :
![9](https://github.com/user-attachments/assets/0dd48b5e-1313-4c5b-b4ff-6e828841654b)
```


#### Interpretasi
Kode di atas mendefinisikan kelas Buku yang memiliki atribut untuk judul, penulis, dan tahun terbit, serta metode untuk menampilkan informasi buku dan menghitung usia buku berdasarkan tahun terbitnya, dengan contoh penggunaan untuk tiga buku yang berbeda.
```

### 10. Algoritma dengan Persyaratan Logika Khusus

### Buatlah program yang mengimplementasikan algoritma pencarian biner, namun dengan modifikasi: algoritma harus bisa mencari nilai di list yang hanya berisi angka genap, dan jika nilai yang dicari adalah angka ganjil, program harus menampilkan pesan bahwa nilai tersebut tidak bisa ditemukan.
```

```
```python
def binary_search_even(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:   
            right = mid - 1

    if target % 2 != 0:
        print(f"Maaf, nilai {target} tidak ditemukan dalam daftar.")
    return -1

# Contoh penggunaan
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(binary_search_even(numbers, 6))  
print(binary_search_even(numbers, 16))   

```
#### Output :
![10](https://github.com/user-attachments/assets/2f563dea-6e5f-4dcf-bde6-31c77b65dd3f)

```

#### Interpretasi
Kode di atas mengimplementasikan algoritma pencarian biner untuk menemukan indeks elemen genap dalam daftar; jika elemen ditemukan, indeksnya dikembalikan, dan jika tidak ditemukan serta target adalah bilangan ganjil, program mencetak pesan bahwa nilai tersebut tidak ada dalam daftar.
```