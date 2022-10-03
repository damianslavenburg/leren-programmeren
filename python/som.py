cijfer = 50
aantal = 0
som = str(cijfer)
totaal = cijfer

while totaal <=1000:
    cijfer = cijfer +1
    totaal = totaal + cijfer
    som = som + "+" + str(cijfer)
    print( som + "=" + str(totaal))
    aantal = aantal + 1
print("",aantal,"sommen")