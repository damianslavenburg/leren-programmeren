import random

kleuren = ("oranje", "blauw", "groen", "bruin")
zakvullen = {}
aantal = int(input('hoeveel m&ms wil je?'))
for x in range(aantal):
    choice = random.choice(kleuren)
    if choice in zakvullen:
            zakvullen[choice] = zakvullen[choice] + 1


    else:
            zakvullen[choice] = 1
print(zakvullen)




