tickets= 7.45 # ticket prijs persoon
personen= input("hoeveel personen: ")
print (tickets * int(personen) )
vip= 0.074  #per minute
min= input("hoeveel minuten wil je in de vip lounce: ")
person_vip= input("hoeveel personen willen jullie in de vip")

print( 'dat word dan',tickets * int(personen) + vip * int(min) * int(person_vip) )
