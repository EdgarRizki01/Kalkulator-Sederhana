print("---------------------------------------------")
print("            kalkulator sederhana            ")
print("---------------------------------------------")
print("Pilihan operasi hitung")
print("1. Penjumplahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
input_user = int(input("Pilih dari 1-4: "))
s = "y"

if input_user < 5:
    while True:
        if s == "y":
            a = (int(input("Masukan angka: ")))
            b = (int(input("Masukan angka: ")))
            if input_user == 1:
                print(f"Hasil dari {a} + {b} = {a + b}")
            elif input_user == 2:
                print(f"Hasil dari {a} - {b} = {a - b}")
            elif input_user == 3:
                print(f"Hasil dari {a} x {b} = {a * b}")
            elif input_user == 4:
                print(f"Hasil dari {a} : {b} = {a / b}")
        elif s == "n":
            print("program berhenti") 
            break
        s = str(input("Apakah ingin lanjut? y/n: "))
else:
    print("jangan masukan angka selain di atas")