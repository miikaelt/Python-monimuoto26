lista = []

luku = int(input("Anna luku (0 lopettaa): "))

while luku != 0:
    lista.append(luku)

    print("Lisäysjärjestyksessä:", lista)
    print("Järjestettynä:", sorted(lista))

    luku = int(input("Anna luku (0 lopettaa): "))

print("Ohjelma lopetettu")