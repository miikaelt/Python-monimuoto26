sanat = ["omena", "banaani", "auto", "mansikka", "tietokone", "kissa"]

maara = 0

for sana in sanat:
    if len(sana) > 5:
        maara = maara + 1

print("Yli 5 kirjaimen sanoja:", maara)