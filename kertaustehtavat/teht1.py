tuntipalkka = float(input("Anna tuntipalkka: "))
tunnit = float(input("Anna tehdyt tunnit: "))
paiva = input("Anna viikonpäivä: ")

if paiva.lower() == "sunnuntai":
    paivapalkka = tuntipalkka * 2 * tunnit
else:
    paivapalkka = tuntipalkka * tunnit

print("Päiväpalkka:", paivapalkka, "euroa")