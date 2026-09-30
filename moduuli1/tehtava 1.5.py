leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

leiviska_grammoina = 20 * 32 * 13.3
naula_grammoina = 32 * 13.3
luoti_grammoina = 13.3

grammat = (leiviskat * leiviska_grammoina +
           naulat * naula_grammoina +
           luodit * luoti_grammoina)

kilogrammat = int(grammat // 1000)
loput_grammat = grammat % 1000

print(f"Massa on {kilogrammat} kilogrammaa ja {loput_grammat:.1f} grammaa.")