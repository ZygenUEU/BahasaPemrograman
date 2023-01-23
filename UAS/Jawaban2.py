try:
    num1 = 7
    num2 = int(input("Masukan angka: "))
    print(num1 / num2)
except ZeroDivisionError:
    print("Error: Angka tidak dapat dibagi nol")
except ValueError:
    print("Error: Masukan angka valid")
