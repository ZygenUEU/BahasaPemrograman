# contoh cara coding sederhana 
def tambah():
    a = int(input("angka 1: "))
    b = int(input("angka 2: "))
    c = a + b
    print(c)
def kurang():
    a = int(input("angka 1: "))
    b = int(input("angka 2: "))
    c = a - b
    print(c)
def kali():
    a = int(input("angka 1: "))
    b = int(input("angka 2: "))
    c = a * b
    print(c)

def pilihan():
    print("1. Tambah")
    print("2. Kurang")
    print("3. Exit")

while True:
    pilihan()
    pil = int(input("Pilihan : "))
    if pil == 1:
        tambah()
    elif pil == 2:
        kurang()
    elif pil == 3:
        kali()
    else:
        break
