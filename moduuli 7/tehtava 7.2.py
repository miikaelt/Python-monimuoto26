nimet = set()

while True:
    nimi = input("Anna nimi: ")

    if nimi == "":
        break

    if nimi not in nimet:
        print("Uusi nimi")
        nimet.add(nimi)
    else:
        print("Aiemmin syötetty nimi")

print("Syötetyt nimet:")

for nimi in nimet:
    print(nimi)