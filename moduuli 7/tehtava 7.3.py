lentoasemat = {}

while True:
    print("\n1. Lisää uusi lentoasema")
    print("2. Hae lentoaseman tiedot")
    print("3. Lopeta")

    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        icao = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")

        lentoasemat[icao] = nimi

        print("Lentoasema tallennettu.")

    elif valinta == "2":
        icao = input("Anna haettavan lentoaseman ICAO-koodi: ")

        if icao in lentoasemat:
            print("Lentoaseman nimi:", lentoasemat[icao])
        else:
            print("Lentoasemaa ei löydy.")

    elif valinta == "3":
        print("Ohjelma lopetetaan.")
        break

    else:
        print("Virheellinen valinta.")