#Function
print("Hasil fungsi")
def Tambah(num1, num2):
    print(num1, " + ", num2, " = ", num1+num2)

Tambah(5, 6)

print("========================")
#Recurisve Function
print("Hasil rekursif")
def Faktorial(angka):
    if angka == 1:
        return 1
    else:
        return angka * Faktorial(angka-1)

print(Faktorial(5))

