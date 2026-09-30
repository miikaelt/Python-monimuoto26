import random

koodi1 = str(random.randint(0, 9))
koodi1 = koodi1 + str(random.randint(0, 9))
koodi1 = koodi1 + str(random.randint(0, 9))

koodi2 = str(random.randint(1, 6))
koodi2 = koodi2 + str(random.randint(1, 6))
koodi2 = koodi2 + str(random.randint(1, 6))
koodi2 = koodi2 + str(random.randint(1, 6))

print(f"Kolmenumeroinen koodi: {koodi1}")
print(f"Nelinumeroinen koodi: {koodi2}")