#variabel
a = "Lamda Pratama Aprilliansyah"
def func():
    a = "any"
    print ("selamat "+ a)
func()
print (a)

#definisi
def tambah():
    a = 5 
    b= 3 
    c= a+b
    print (c)

tambah()

#parameter
def data(nama,nim):
    print(f"nama saya {nama} dan nim {nim}")
data ("Lamda Pratama Aprilliansyah","20210801056")

#contoh
def total(sisi):
    return sisi*sisi

total()
def segitiga(alas,tinggi):
    return 0.5*alas*tinggi

segitiga()