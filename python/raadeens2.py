import random
print("raad het nummer tussen 1 en 1000")
getal = random.randint(1,1000)
keergeraden = 0
ronde = 0
repeat = True
print(getal)
raad = int(input("getal: "))
while repeat == True:
    if raad == getal:
       print('geraden')
    
