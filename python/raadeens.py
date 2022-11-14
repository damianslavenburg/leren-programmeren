import random
print("raad het nummer tussen 1 en 1000")
getal = random.randint(1,1000)
keergeraden = 0
ronde = 0
raad = input("getal: ")
repeat = True
while repeat == True:
    if raad == getal:
        print("dat is goed geraden")
        repeat = False
        keergeraden = keergeraden + 1
    elif int(raad) < getal:
        print("lager")
        ronde = ronde + 1
        repeat = True
    elif int(raad) < getal:
        print("hoger")
        repeat = True
        keergeraden = keergeraden + 1