from data import *

## Functies
## Welkomstscherm
def intro():
    print("Welkom bij Papi Gelato")
## Error messages
def error():
    print("Sorry dat is geen optie.")

def errorbakje():
    print("Sorry, een bakje kan maximaal 8 bolletjes bevatten.")
## Afscheidsboodschap
def doei():
    print("Bedankt voor het bestellen bij Papi Gelato.")

## Bestellen van aantal bolletjes minimaal 1 maximaal 8
def bolletjes() -> int:
    herhalen =  True
    while herhalen == True:
        try:
                bolletjes = int(input('Hoeveel bolletjes wilt u? '))
                if bolletjes >= 1 and bolletjes <= 3:
                    aantalbolletjes = bolletjes
                    herhalen = False
                    return aantalbolletjes
                elif bolletjes >= 4 and bolletjes <= 8:
                    aantalbolletjes = bolletjes
                    herhalen = False 
                    return aantalbolletjes
                elif bolletjes > 8:
                    errorbakje()
                    herhalen = True
                elif bolletjes <=0:
                    error()
                    herhalen = True

        except:
            error()
            herhalen = True


    return bolletjes
## Kiezen van verpakking bakje of hoorntje
def verpakking(aantalbolletjes) -> str:
    herhalen = True
    while herhalen == True:
        try:
            if aantalbolletjes <4:
                bakje = input('Wilt u deze '+ str(aantalbolletjes) +' bolletje(s) in een hoorntje of een bakje?  ').lower()
                if bakje == 'bakje':
                    verpakking = 'bakje'
                    herhalen = False
                    return verpakking
                elif bakje == 'hoorntje':
                    verpakking = 'hoorntje'
                    herhalen = False
                    return verpakking
            else:
                print("U krijgt een bakje met "+str(aantalbolletjes)+" bolletje(s).  ")
                verpakking = 'bakje'
                herhalen = False
                return verpakking
        except:
            error()
            herhalen = True

## Keuze van meerbestellen ja of nee
def meerbestellen() -> bool:
    try:
        doorgaan = input("Wilt u meer bestellen?  ").lower()
        if doorgaan == 'ja':
            nognkeer = True
        elif doorgaan == 'nee':
            nognkeer = False
        else:
            error()
            meerbestellen()
            
    except:
        error()
    return nognkeer

## Berekening van de prijs
def prijsberekening():
    totaalprijs = (bonnetje["bolletjes"] * prijs["bolletjes"]) + (bonnetje["hoorntjes"] * prijs["hoorntjes"]) + (bonnetje["bakjes"] * prijs["bakjes"])
    return totaalprijs
## kassabon
def kassabon():
    #prijsen
    prijsBolletjes = bonnetje["bolletjes"] * prijs["bolletjes"]
    prijsbakjes = bonnetje["bakjes"] * prijs["bakjes"]
    prijsHoorntjes = bonnetje["hoorntjes"] * prijs["hoorntjes"]
    #bonnetje

    print("-=-=-=-=-=-=-=-=-=-=-Papi Gelato-=-=-=-=-=-=-=-=-=-=-=-")

    if bonnetje["bolletjes"] > 0:
        print(f"bolletjes {bonnetje['bolletjes']} x € {prijs['bolletjes']:.2f} = € {prijsBolletjes:.2f}")

    if bonnetje["hoorntjes"] > 0:
     print(f"hoorntjes {bonnetje['hoorntjes']} x € {prijs['hoorntjes']:.2f} = € {prijsHoorntjes:.2f}")

    if bonnetje["bakjes"] > 0:
     print(f"bakjes {bonnetje['bakjes']} x € {prijs['bakjes']:.2f} = € {prijsbakjes:.2f}")
    print("------------------------- +")
    print(f"totaal = € {prijsberekening():.2f}")
    print("Bedankt en tot ziens!")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    
