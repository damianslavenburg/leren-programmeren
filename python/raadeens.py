import random
print("raad het nummer tussen 1 en 1000")
getal = random.randint(1,1000)
keergeraden = 0
ronde = 0
repeat = True
while repeat == True:
    print(getal)
    raad = input("getal: ")

    if int(raad) < getal:
        print("hoger")
        keergeraden = keergeraden + 1
        repeat = True
    elif int(raad) > getal:
        print("lager")
        keergeraden = keergeraden + 1
        repeat = True
    else: 
        print("dat is goed geraden")
        repeat = False
        ronde = ronde + 1
        keergeraden = keergeraden - keergeraden

    if keergeraden == 10:
        opnieuw = input('je hebt teveel keer geraden wil je een nieuwgetal? ').lower()
        if opnieuw == ("ja"): 
            repeat = True
            keergeraden = keergeraden - keergeraden
    else: 
        quit