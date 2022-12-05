import random
kleuren = ("oranje", "blauw", "groen", "bruin")
zakvullen = []
aantal = int(input('hoeveel m&ms wil je?'))
for x in range(aantal):
    zakvullen.append(random.choice(kleuren))
print(zakvullen)






