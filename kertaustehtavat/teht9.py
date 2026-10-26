tuotteet = []
maarat = []

jatketaanko = "Kyllä"

while jatketaanko == "Kyllä":
    tuote = input("Mitä tuotetta valmistetaan? ")
    maara = int(input("Kuinka monta valmistetaan? "))

    tuotteet.append(tuote)
    maarat.append(maara)

    jatketaanko = input("Jatketaanko tuotantoa? ")

print("Tuotanto lopetettu!")
print("Valmistetut tuotteet:")

for i in range(len(tuotteet)):
    print(tuotteet[i] + ":", maarat[i], "kpl")