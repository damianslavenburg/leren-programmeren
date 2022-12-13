import random
from fruitmand import fruitmand
lijst= []
vraag = int(input("hoeveel fruit wil je?"))
for fruit in range(len(fruitmand)):
    lijst.append(fruitmand[fruit]["name"])
    for x in range(vraag):
        print(random.choice(lijst))
