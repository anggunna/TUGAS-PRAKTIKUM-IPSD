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