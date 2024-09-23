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