leeftijd = input("hoe oud bent u?")
if int(leeftijd) >= 18:
    print("u mag naar binnen veel plezier")
    naam = input("wat is u naam?")
    if leeftijd == 21 and naam == "rudi" or naam == 'arnold' or naam == 'jeroen' or naam == 'kjeld':
        print("u krijgt een sticker")
        
    if int(leeftijd) < 21:
        print("u bent onder 21 u krijgt geen bandje voor alchol")
    else:
        print("u bent 21 jaar of ouder dus u krijgt een bandje voor alchol")
    drankje = input("welk drankje wilt u (a cola (b bier ")
    if drankje == "b" and int(leeftijd) < 21:
        print("u heeft geen bandje u mag geen bier")
    else:
        print("u heeft een bandje hier is u bier")
else:
    print("sorry u bent jonger dan 18")

