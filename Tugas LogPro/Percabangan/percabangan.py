# if biasa
nilai = 50

if nilai < 50 :
    print("kamu remidi")

if nilai >= 50:
    print("kamu lulus")

print("======================================")

# if - else 
passwordHP = "iloveyou"

if passwordHP == "ihateyou":
    print("password benar!")
else :
    print("password salah")

print("=======================================")

# if-elif-else
grade = 78

if grade >= 100 :
    print("COngratulation")
elif grade >= 90:
    print("Good")
elif grade >= 80:
    print("Ok")
elif grade >= 70:
    print("Bad")
elif grade <70:
    print("worse")

print("============================================")

# Nested if
age = 20
haveCard = False

if age >= 17:
    if haveCard :
        print("boleh masuk")
    else :
        print("tunjukkan kartu terlebih dahulu")

else :
    print("tidak boleh masuk, belum cukup umur.")

print("===============================================")

# Real Case - Kasus kasir
totalBelanja = 50000
memberToko = False

# Kita ingin membuat sistem kasir dengan 
