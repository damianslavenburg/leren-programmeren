import random
kleuren = ("oranje", "blauw", "groen", "bruin")
zakvullen = []
aantal = int(input('hoeveel m&ms wil je?'))
for x in range(aantal):
    choice = random.choice(kleuren)
    zakvullen.append(choice)
print(zakvullen)






