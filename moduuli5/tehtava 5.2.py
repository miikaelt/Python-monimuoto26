luvut = []

syote = input("Anna luku: ")

while syote != "":
    luvut.append(float(syote))
    syote = input("Anna luku: ")

luvut.sort(reverse=True)

print("Viisi suurinta lukua:")

for luku in luvut[:5]:
    print(luku)