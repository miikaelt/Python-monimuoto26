import math

def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2 / 100
    pinta_ala = math.pi * sade ** 2
    return hinta / pinta_ala

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))

yksikko1 = yksikkohinta(halkaisija1, hinta1)
yksikko2 = yksikkohinta(halkaisija2, hinta2)

print("Ensimmäisen pizzan yksikköhinta:", round(yksikko1, 2), "€/m²")
print("Toisen pizzan yksikköhinta:", round(yksikko2, 2), "€/m²")

if yksikko1 < yksikko2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif yksikko2 < yksikko1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Molemmat pizzat antavat yhtä hyvän vastineen rahalle.")