import os

def aritmatika(a, b, operasi_hitung):
    if operasi_hitung == "+":
        print(f"hasil dari {a:g} + {b:g} = {a+ b :g}")
    elif operasi_hitung == "-":
        print(f"hasil dari {a:g} - {b:g} = {a- b :g}")
    elif operasi_hitung == "*":
        print(f"hasil dari {a:g} * {b:g} = {a* b :g}")
    elif operasi_hitung == "/":
        print(f"hasil dari {a:g} / {b:g} = {a/ b :g}")
    else:
        raise ValueError("Simbol operasi tidak dikenal!")

s = "y"

try:
    while True:
        os.system("clear" or "cls")
        print("---------------------------------------------")
        print("            kalkulator sederhana            ")
        print("---------------------------------------------")
        if s == "y":
            input1 = float(input("masukan angka Pertama: "))
            operator = str(input("masukan operasi hitung (+,-,*,/): "))
            input2 = float(input("masukan angka Kedua: "))

            print(aritmatika(input1, input2, operator))
        elif s == "n":
            print("keluar dari program")
            break
        else:
            break
        
        s = str(input("apakah mau lagi? y/n  ")) 

except ValueError as e:
    if "Simbol" in str(e):
        print(f"Error: {e}")
    else:
        print("Error: Masukan angka yang benar!")
       

except ZeroDivisionError:
    print("Error: angka tidak bisa di bagi dengan nol!")