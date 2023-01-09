class Karyawan:
    # Konstruktor
    def __init__(self, nama, gaji, projek):
        self.nama = nama
        self.gaji = gaji
        self.projek = projek


    # Menampilkan detail karyawan
    def tampil(self):
        # Mengakses public data
        print("Nama: ", self.nama)
        print('Gaji:', self.gaji)

    def kerja(self):
        print(self.nama, 'Sedang bekerja', self.projek)

# Membuat objek dari class
karyawan = Karyawan('Reza', 78000, 'APP')
karyawan2 = Karyawan('Bakhari', 727, 'OS')

# Memanggil method dari class
karyawan.tampil()
karyawan.kerja()

karyawan2.tampil()
karyawan2.kerja()