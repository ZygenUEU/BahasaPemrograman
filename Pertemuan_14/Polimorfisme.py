class Kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.age = umur
    def info(self):
        print(f"Saya kucing bernama {self.nama}. Saya {self.age} tahun.")
    def bersuara(self):
        print("Meow")

class Anjing:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Saya anjing bernama {self.name}. Saya {self.age} tahun.")
    def bersuara(self):
        print("Guk")

kucing1 = Kucing("Lulu", 2)
anjing1 = Anjing("Jack", 5)

for hewan in (kucing1, anjing1):
    hewan.bersuara()
    hewan.info()
    hewan.bersuara()
