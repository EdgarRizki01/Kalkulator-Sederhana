import os

def aritmatika(a, b, operasi_hitung):
    if operasi_hitung == "+":
        print(f"hasil dari {a} + {b} = {a+ b}")
    elif operasi_hitung == "-":
        print(f"hasil dari {a} - {b} = {a- b}")
    elif operasi_hitung == "*":
        print(f"hasil dari {a} * {b} = {a* b}")
    elif operasi_hitung == "/":
        print(f"hasil dari {a} / {b} = {a/ b}")
    else:
        raise ValueError("Simbol operasi tidak dikenal!")

s = "y"

try:
    while True:
        os.system('clear')
        print("---------------------------------------------")
        print("            kalkulator sederhana            ")
        print("---------------------------------------------")
        if s == "y":
            input1 = int(input("masukan angka Pertama: "))
            operator = (input("masukan operasi hitung (+,-,*,/): "))
            input2 = int(input("masukan angka Kedua: "))

            hasil = aritmatika(input1, input2, operator)
        elif s == "n":
            print("keluar dari program")
            break
        
        s = str(input("apakah mau lagi? y/n  ")) 

except ValueError as e:
    if "Simbol" in str(e):
        print(f"Error: {e}")
    else:
        print("Error: Masukan angka yang benar")

except ZeroDivisionError:
    print("Error: angka tidak bisa di bagi dengan nol")