from concurrent.futures.process import _ThreadWakeup


repeat = True

while repeat == True:
    print("wat is een variable? ")
    antwoord = input("a = iets wat je kan laten onthouden , b = een functie , c een programmer taal , d = ik weet t niet ").lower()
    if antwoord == 'a':
        print("dat is goed")
        repeat = False
    else:
        print('dat is fout')
        repeat = True