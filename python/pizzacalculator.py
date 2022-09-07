#damian slavenburg 99072083
#naam en voorstellen
from tkinter import N


naam_res = "pizzaria mamaia"
print("hallo welcome bij", naam_res , "wat is u naam?")
naam = input()
print("hallo" ,naam, "hoe kan ik je helpen vandaag?")
#pizza menu
pizza_menu = ["small{€5}", "medium{€6,95}", "large{€10}"]
print(pizza_menu)
#pizza grote en aantal bestellen
repeat = True

while repeat == True:
    pizza_size = input()

    if pizza_size == 'small':
        repeat = False
        prijs=5 
    elif pizza_size == 'medium':
        repeat = False
        prijs= 6,95
    elif pizza_size == 'large':
        repeat = False 
        prijs= 10
    
    else:
        print(pizza_menu)

pizza_aantal= input('hoeveel pizzas wilt u? ' '')
#bonnetje
totaal= int(pizza_aantal) * prijs  

if int(pizza_aantal) == 1 :
    print('---------------------------------')
    print('       ', naam_res)
    print("   ")
    print("u heeft " + str(pizza_aantal) + " " + str(pizza_size) + ' pizza besteld')
else:
    print('---------------------------------')
    print('       ', naam_res)
    print('  ')
    print("u heeft " + str(pizza_aantal) + " " + str(pizza_size) + " pizza's besteld")
print('het totaal bedrag is €' ,totaal ,)
print(" ")
print('bestelling geplaats door:', naam)
print("---------------------------------")