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

    #verpakking
    verpakkingsoort = verpakking(totaalbolletjes)
    bonnetje[verpakkingsoort + "s"] += 1
    #smaak
    smaakkeuze(totaalbolletjes)
    print(bonnetje)
    #meer bestellen
    herhalen = meerbestellen()
doei()
kassabon()

