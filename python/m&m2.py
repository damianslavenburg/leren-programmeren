import random
oranje = 0
blauw = 0
groen = 0
bruin = 0
kleuren = ("oranje", "blauw", "groen", "bruin")
zakvullen = {}
aantal = int(input('hoeveel m&ms wil je?'))
for x in range(aantal):
    choice = random.choice(kleuren)
    if choice == "oranje":
     oranje = oranje + 1
     zakvullen.update({choice:oranje})
    if choice == "blauw":
        blauw = blauw + 1
        zakvullen.update({choice:blauw})
    if choice == "groen":
        groen = groen + 1
        zakvullen.update({choice:groen})
    if choice == "bruin":
        bruin = bruin + 1
        zakvullen.update({choice:bruin})
print(zakvullen)




