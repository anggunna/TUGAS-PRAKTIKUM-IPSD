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