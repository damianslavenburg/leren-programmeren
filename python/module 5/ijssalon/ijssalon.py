#import
from function import *
from data import *
#gedag zeggen
intro()
#loop voor meer bestellen
while herhalen:
    #aantal bolletjes
    totaalbolletjes = bolletjes()
    bonnetje["bolletjes"] += totaalbolletjes
    #smaak
    #verpakking
    verpakkingsoort = verpakking(totaalbolletjes)
    bonnetje[verpakkingsoort + "s"] += 1
    smaaken(totaalbolletjes)
    print(bonnetje)
    #meer bestellen
    herhalen = meerbestellen()
doei()
kassabon()

