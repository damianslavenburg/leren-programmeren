#croisantjes
# stokbrood
#2.78

croisant = input("hoeveel croisant wil je: ")
prijs_croisant = 0.39
stokbrood = input("hoeveel stokbrooden wil je: ")
prijs_stokbrood= 2.78
kortingsbon = input("hoeveel kortingsbonnen heb je: ")
kortingsbonnen_prijs = 0.50

y = int(croisant) * prijs_croisant + int(stokbrood) * prijs_stokbrood - int(kortingsbon) * kortingsbonnen_prijs
print (y)
print("nog te betalen")
