import random
print("raad het nummer tussen 1 en 1000")
getal = random.randint(1,1000)
keergeraden = 0
ronde = 0
repeat = True
score = 0

while repeat == True:
    # print(getal)
    raad = int(input("getal: "))
    verschill = raad - getal

    if abs(int(verschill)) <= 20 and abs(int(verschill)) != 0 :
        print("je bent heel warm")
        repeat = True

    elif abs(int(verschill)) <= 50 and abs(int(verschill)) != 0 :
        print("je bent warm")
        repeat = True

    if raad  < getal:
            print("hoger")
            keergeraden = keergeraden + 1
            repeat = True

    elif raad > getal:
            print("lager")
            keergeraden = keergeraden + 1
            repeat = True
        

    if keergeraden == 10:
        keergeraden = 0
        opnieuw = input('je hebt teveel keer geraden wil je een nieuwgetal? ').lower()

        if opnieuw == ("yes"): 
            repeat = True
            getal = random.randint(1,1000)
        elif opnieuw == "no":
            repeat = False 
            quit

    if raad == getal:
        print("dat is goed geraden")
        ronde = ronde + 1
        keergeraden = keergeraden - keergeraden
        score = score + 1
        print("u bent bij ronde",ronde)
        nogeenronde = input("wilt u nog een ronde(yes of no)").lower()  
        if nogeenronde == "yes" or "ja":
            getal = random.randint(1,1000)
            repeat = True
        
        elif nogeenronde == "no" or "nee" or ronde == 20:
            print('u heb',score,'punten')
            repeat = False
            quit
