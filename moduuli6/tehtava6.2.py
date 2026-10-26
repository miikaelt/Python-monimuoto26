import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

maksimi = int(input("Anna nopan tahkojen määrä: "))

luku = 0

while luku != maksimi:
    luku = heita_noppaa(maksimi)
    print(luku)