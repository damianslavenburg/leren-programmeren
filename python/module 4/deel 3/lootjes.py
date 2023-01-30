import random
repeat = True
deelnemers = []

while repeat == True:

    naam = input ("Voer een naam in:").lower()

    if naam in deelnemers:
        print ("deze naam bestaat al!")

    else: 
        deelnemers.append(naam)
        meernamen = input ("wil je meer namen toevoegen?").lower()

        if meernamen == "ja":
            repeat = True

        elif meernamen == "nee":
            lengtelijst = len(deelnemers)
            repeat = False

            if int(lengtelijst) >= 3:
                repeat = False

            else:
                print ("je moet minimaal 3 namen invoeren: ")
                repeat = True


random.shuffle(deelnemers)


print("Hier is je lijst met lootjes:\n")

for i in range (len(deelnemers)-1):
    print("'" + deelnemers[i] + "'" + " heeft " + "'" + deelnemers[i + 1] + "'")
print("'" + deelnemers[-1] + "'" + " heeft " + "'" + deelnemers[0] + "'")
