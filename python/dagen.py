dagen = input("welke dag is het? ")
ma = "maandag"
di = "dinsdag"
wo = "woensdag"
do = "donderdag"
vrij = "vrijdag"
za = 'zaterdag'
zo = 'zondag'

while dagen == ma:
    print("dinsdag , woensdag , donderdag , vrijdag , zaterdag , zondag")
    break
while dagen == di:
    print(" woensdag , donderdag , vrijdag , zaterdag , zondag , maandag")    
    break
while dagen == wo:
    print("   donderdag , vrijdag , zaterdag , zondag , maandag , dinsdag") 
    break
while dagen == do:
    print(" vrijdag , zaterdag , zondag , maandag dinsdag , woensdag") 
    break
while dagen == vrij:
    print("zaterdag , zondag , maandag dinsdag , woensdag , donderdag") 
    break
while dagen == za:
    print("  zondag , maandag dinsdag , woensdag , donderdag , vrijdag")
    break
while dagen == zo:
    print(" aandag dinsdag , woensdag , donderdag , vrijdag , zaterdag")
    break
