tickets= 7.45 # ticket prijs persoon
personen= input("hoeveel personen: ")
vip= 0.074  #per minute
min= input("hoeveel minuten wil je in de vip lounce: ")
person_vip= input("hoeveel personen willen jullie in de vip: ")
print('Dit geweldige dagje-uit met ',personen, " mensen in de speelhal met ", min , " minuten vr kost je maar ",tickets * int(personen) + vip * int(min) * int(person_vip) )
