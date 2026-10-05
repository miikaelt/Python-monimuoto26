syote = input("Anna luku: ")

if syote != "":
    luku = float(syote)
    pienin = luku
    suurin = luku

    while syote != "":
        syote = input("Anna luku: ")

        if syote != "":
            luku = float(syote)

            if luku < pienin:
                pienin = luku

            if luku > suurin:
                suurin = luku

    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")