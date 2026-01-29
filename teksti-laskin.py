#Kysytään laskutyyppi,
lasku = input("Valitse lasku (+ tai - tai / tai *): ")

#Kysytään luvut,
a = float(input("Anna ensimmäinen luku: "))
b = float(input("Anna toinen luku: "))

#Tehdään lasku valinnan mukaan,
if lasku == "-":
    tulos = a - b
elif lasku == "+":
    tulos = a + b
elif lasku == "/":
    if b == 0:
        print("Nollalla ei voi jakaa")
        exit()
    tulos = a / b
elif lasku == "*":
    tulos = a * b
else:
    print("Virheellinen valinta")
    exit()

#Tulostetaan tulos,
print("Tulos on:", tulos)
