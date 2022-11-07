def jualan():
    a = "capucino"
    b = "teh"
    print ("Pilihan")
    print ("1.", a)
    print ("2.", b)
    print ("3. Exit")
    
def welcome():
    nim = 1234567
    nama = "QWERTY"
    print ("NIM : ", nim)
    print ("NAMA : ", nama)

def teh():
    te = "memilih TEH"
    print(te)
    hTeh = int(input("masukkan harga : "))
    ppn = hTeh * 10/100
    total = hTeh+ppn
    print("Jumlah yang harus di bayarkan", total)

def capucino():
    cap = "memilih capucino"
    print(cap)
    hCapucino = int(input("masukkan harga : "))
    ppn = hCapucino * 10/100
    total = hCapucino+ppn
    print("Jumlah yang harus di bayarkan", total)
    
while True:
    welcome()
    jualan()
    pil = int(input("masukkan pilihan : "))
    if pil == 1:
        capucino()
    elif pil == 2:
        teh()
    elif pil == 3:
        break
    else:
        print ("pilihan salah")